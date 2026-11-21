# 🎓 AI Exam Score Predictor & Study Coach

An end-to-end Machine Learning web application built with **Python**, **Pandas**, **Scikit-Learn**, **Matplotlib**, and **Streamlit** that predicts a student's exam score based on daily study habits and provides actionable AI coaching recommendations.

---

## 📌 Project Overview

Using a dataset of **20,000 student records** (`Exam_Score_Prediction.csv`), this project walks through the complete data science lifecycle:

1. **Exploratory Data Analysis (EDA):** Correlation heatmaps, regression plots, and categorical group comparisons to separate real score drivers from noise.
2. **Feature Selection:** Reduced 13 raw columns down to the **6 highest-impact features** without losing predictive accuracy.
3. **Data Preprocessing:** Pure Pandas ordinal mapping (`.map()`) and one-hot encoding (`pd.get_dummies()`).
4. **Model Training & Evaluation:** Trained a **Linear Regression** model evaluated via $R^2$, Adjusted $R^2$, and Mean Absolute Error (MAE).
5. **Interactive Web Application:** Built a Streamlit UI with real-time sliders, metric cards, Matplotlib comparison charts, and automated study advice.

---

## 📊 Key Exploratory Data Analysis (EDA) Findings

| Feature                                                                       | Type        | Relationship with `exam_score`                                               | Decision            |
| :---------------------------------------------------------------------------- | :---------- | :--------------------------------------------------------------------------- | :------------------ |
| **`study_hours`**                                                             | Numerical   | Strong positive correlation ($r = +0.72$)                                    | **Kept**            |
| **`class_attendance`**                                                        | Numerical   | Moderate positive correlation ($r = +0.31$)                                  | **Kept**            |
| **`study_method`**                                                            | Categorical | `coaching` (68.6) vs. `self-study` (58.7) — **9.8 pt spread**                | **Kept**            |
| **`sleep_quality`**                                                           | Categorical | `good` (67.1) vs. `poor` (57.9) — **9.2 pt spread**                          | **Kept**            |
| **`facility_rating`**                                                         | Categorical | `high` (66.2) vs. `low` (58.6) — **7.6 pt spread**                           | **Kept**            |
| **`sleep_hours`**                                                             | Numerical   | Weak positive correlation ($r = +0.13$)                                      | **Kept**            |
| `student_id`, `age`, `gender`, `course`, `internet_access`, `exam_difficulty` | Mixed       | Zero correlation ($r \approx 0.00$) or flat group averages (< 0.9 pt spread) | **Dropped (Noise)** |

---

## 📈 Model Performance

Evaluated on an unseen **20% test split (4,000 students)**:

- **$R^2$ Score:** `0.7333` (`73.33%` of exam score variance explained)
- **Adjusted $R^2$ Score:** `0.7327` (confirms zero overfitting across the 9 encoded features)
- **Mean Absolute Error (MAE):** `7.86 points` (cuts baseline guessing error of `15.54 points` nearly in half)

---

## 🗂️ Project Structure

```text
exam_score_ai/
├── Exam_Score_Prediction.csv   # Raw dataset (20,000 rows, 13 columns)
├── train_model.py              # Data cleaning, encoding, model training & evaluation script
├── exam_score_model.joblib     # Saved Linear Regression model
├── model_columns.joblib        # Saved feature column order for inference alignment
├── app.py                      # Interactive Streamlit web application
├── requirements.txt            # Python dependencies for deployment
└── README.md                   # Project documentation
```
