import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load dataset and drop regional column for global usability
df = pd.read_csv("Student_Depression_Dataset.csv")
X = df.drop(["Depression", "Home_division"], axis=1)
y = df["Depression"].map({"No": 0, "Yes": 1})

# 2. Stratified 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 3. One-Hot Encode categorical columns
X_train = pd.get_dummies(X_train, drop_first=True, dtype=int)
X_test = pd.get_dummies(X_test, drop_first=True, dtype=int).reindex(
    columns=X_train.columns, fill_value=0
)

# 4. Standardize numerical columns (fit on train only!)
scaler_cols = ["Age", "Current_semester", "CGPA", "Cost_without_study"]
scaler = StandardScaler()
X_train[scaler_cols] = scaler.fit_transform(X_train[scaler_cols])
X_test[scaler_cols] = scaler.transform(X_test[scaler_cols])

# 5. Train & Evaluate Logistic Regression (Baseline)
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

print("=== Logistic Regression ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred_log):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

# 6. Train & Evaluate Random Forest (Final Model)
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("=== Random Forest ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# 7. Save model + preprocessing artifacts for Streamlit app
artifact = {
    "model": rf_model,
    "scaler": scaler,
    "scaler_cols": scaler_cols,
    "feature_columns": X_train.columns.tolist(),
    "log_reg_acc": accuracy_score(y_test, y_pred_log),
    "rf_acc": accuracy_score(y_test, y_pred_rf),
}
joblib.dump(artifact, "depression_model.joblib")
print("Saved depression_model.joblib successfully!")