import streamlit as st
import pandas as pd
import joblib

# Page setup
st.set_page_config(
    page_title="Student Depression Risk Predictor",
    page_icon="🧠",
    layout="centered"
)

# Load saved model and preprocessing objects
@st.cache_resource
def load_artifact():
    return joblib.load("depression_model.joblib")

artifact = load_artifact()
model = artifact["model"]
scaler = artifact["scaler"]
scaler_cols = artifact["scaler_cols"]
feature_columns = artifact["feature_columns"]

# Header
st.title("🧠 Student Depression Risk Predictor")
st.markdown(
    "Predict student depression risk using a **Random Forest Classifier** trained on "
    "4,464 student records across academic, financial, social, and health indicators."
)

# Model metrics banner
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Final Model", "Random Forest")
col_m2.metric("Test Accuracy", f"{artifact['rf_acc'] * 100:.2f}%")
col_m3.metric("Baseline (LogReg)", f"{artifact['log_reg_acc'] * 100:.2f}%")

st.divider()

# Input Form
st.subheader("Enter Student Details")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", min_value=17, max_value=30, value=22)
    family_bg = st.selectbox(
        "Family Economic Background",
        ["Lower Middle class", "Middle class", "Rich class"]
    )
    relationship = st.selectbox(
        "Relationship Status",
        ["Single", "In a Relationship", "Complicated"]
    )
    marital = st.selectbox(
        "Marital Status",
        ["Unmarried", "Married", "Separated"]
    )
    living = st.selectbox("Living Style", ["Bachelor", "Family"])

with col2:
    semester = st.slider("Current Semester", min_value=0, max_value=13, value=5)
    cgpa = st.slider("Current CGPA", min_value=2.00, max_value=4.00, value=3.40, step=0.01)
    friend_circle = st.selectbox("Do you have a supportive friend circle?", ["Yes", "No"])
    health = st.selectbox(
        "Overall Health Condition",
        ["Good", "Normal", "Abnormal", "Critical"]
    )
    cost = st.number_input(
        "Monthly Living Cost (Excluding Tuition)",
        min_value=0, max_value=50000, value=10000, step=500
    )

st.divider()

# Prediction Button
if st.button("Predict Depression Risk", type="primary", use_container_width=True):
    # 1. Create single-row DataFrame matching training columns
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Family_background": family_bg,
        "Relationship_status": relationship,
        "Marital_status": marital,
        "Living_style": living,
        "Current_semester": semester,
        "CGPA": cgpa,
        "friend_circle": friend_circle,
        "Health_condition": health,
        "Cost_without_study": cost
    }])

    # 2. Apply exact same One-Hot Encoding + Column Alignment
    input_encoded = pd.get_dummies(input_df, drop_first=True, dtype=int).reindex(
        columns=feature_columns, fill_value=0
    )

    # 3. Apply exact same Standardization
    input_encoded[scaler_cols] = scaler.transform(input_encoded[scaler_cols])

    # 4. Predict class and probability
    prediction = model.predict(input_encoded)[0]
    probabilities = model.predict_proba(input_encoded)[0]
    yes_prob = probabilities[1] * 100
    no_prob = probabilities[0] * 100

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ **High Risk of Depression Detected** (Confidence: **{yes_prob:.1f}%**)")
    else:
        st.success(f"✅ **Low Risk of Depression** (Confidence: **{no_prob:.1f}%**)")

    st.write(f"**Estimated Depression Probability:** `{yes_prob:.1f}%`")
    st.progress(int(round(yes_prob)))

    st.info(
        "**Note:** This tool is an educational machine learning project and not a medical diagnosis. "
        "If you or someone you know is struggling with mental health, please reach out to a university counselor or healthcare professional."
    )