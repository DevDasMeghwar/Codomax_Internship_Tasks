import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Load & keep only the 6 meaningful features + target
df = pd.read_csv('Exam_Score_Prediction.csv')
keep_cols = [
    'study_hours',
    'class_attendance',
    'sleep_hours',
    'sleep_quality',
    'study_method',
    'facility_rating',
    'exam_score',
]
df_clean = df[keep_cols].copy()

# 2. Convert text columns to numbers using pure Pandas
df_clean['sleep_quality'] = df_clean['sleep_quality'].map(
    {'poor': 0, 'average': 1, 'good': 2}
)
df_clean['facility_rating'] = df_clean['facility_rating'].map(
    {'low': 0, 'medium': 1, 'high': 2}
)
df_encoded = pd.get_dummies(
    df_clean, columns=['study_method'], drop_first=True, dtype=int
)

# 3. Separate Features (X) and Target (y)
X = df_encoded.drop(columns=['exam_score'])
y = df_encoded['exam_score']

# 4. Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train the LinearRegression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Evaluate Accuracy (MAE, R2, and Adjusted R2)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

n = X_test.shape[0]
p = X_test.shape[1]
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

print(f'MAE: {mae:.2f} points')
print(f'R2 Score: {r2:.4f}')
print(f'Adjusted R2 Score: {adjusted_r2:.4f}')

# 7. Save the trained model and exact column order
joblib.dump(model, 'exam_score_model.joblib')
joblib.dump(list(X.columns), 'model_columns.joblib')
print('Success! Saved exam_score_model.joblib and model_columns.joblib')