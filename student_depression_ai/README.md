# 🧠 Student Depression Risk Predictor

An end-to-end Machine Learning web application built during my internship at **Codomax Digital Solutions and Beyond** to assess student depression risk based on academic, financial, social, and health indicators.

## 📌 Project Overview

- **Problem Type:** Binary Classification (`Yes` / `No`)
- **Dataset:** 4,464 student records across 11 universal features (after dropping regional division data for global applicability)
- **Preprocessing:** Stratified 80/20 Train-Test Split, One-Hot Encoding (`pd.get_dummies`), and Feature Standardization (`StandardScaler`)
- **Models Compared:**
  - **Logistic Regression (Baseline):** `97.31%` Test Accuracy | `0.95` F1-Score
  - **Random Forest Classifier (Final Model):** `98.99%` Test Accuracy | `0.98` F1-Score

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, Joblib
- **Web Framework & Deployment:** Streamlit, Streamlit Cloud

## 🚀 How to Run Locally

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone [https://github.com/DevDasMeghwar/Internship_Tasks.git](https://github.com/DevDasMeghwar/Internship_Tasks.git)
   cd Internship_Tasks/student_depression_ai
   ```
