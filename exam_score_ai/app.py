import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI Exam Score Predictor", page_icon="🎓", layout="centered"
)

# 2. Load the Saved AI Model & Column Order (works from any working directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "exam_score_model.joblib"))
model_columns = joblib.load(os.path.join(BASE_DIR, "model_columns.joblib"))

st.title("🎓 AI Exam Score Predictor & Study Coach")
st.markdown(
    "Enter your study routine below to predict your exam score using a trained"
    " **Linear Regression** model ($R^2 = 0.73$, $\\text{MAE} = \\pm 7.9$"
    " points)."
)

st.divider()

# 3. Interactive User Inputs
col1, col2 = st.columns(2)

with col1:
  study_hours = st.slider(
      "📚 Daily Study Hours",
      min_value=0.0,
      max_value=8.0,
      value=4.0,
      step=0.1,
  )
  class_attendance = st.slider(
      "🏫 Class Attendance (%)",
      min_value=40.0,
      max_value=100.0,
      value=75.0,
      step=0.5,
  )
  sleep_hours = st.slider(
      "😴 Daily Sleep Hours",
      min_value=4.0,
      max_value=10.0,
      value=7.0,
      step=0.5,
  )

with col2:
  study_method = st.selectbox(
      "📝 Primary Study Method",
      ["coaching", "mixed", "group study", "online videos", "self-study"],
  )
  sleep_quality = st.selectbox(
      "🌙 Sleep Quality", ["poor", "average", "good"], index=1
  )
  facility_rating = st.selectbox(
      "🏛️ Study Facility Rating", ["low", "medium", "high"], index=1
  )

# 4. Prepare Input Row for Prediction
input_data = pd.DataFrame([{
    "study_hours": study_hours,
    "class_attendance": class_attendance,
    "sleep_hours": sleep_hours,
    "sleep_quality": {"poor": 0, "average": 1, "good": 2}[sleep_quality],
    "facility_rating": {"low": 0, "medium": 1, "high": 2}[facility_rating],
    "study_method": study_method,
}])

input_encoded = pd.get_dummies(input_data, columns=["study_method"], dtype=int)
input_aligned = input_encoded.reindex(columns=model_columns, fill_value=0)

# 5. Generate Prediction & Insights
if st.button("🚀 Predict My Exam Score", type="primary", use_container_width=True):
  raw_pred = model.predict(input_aligned)[0]
  final_score = float(np.clip(raw_pred, 0, 100))

  low_est = max(0.0, final_score - 7.9)
  high_est = min(100.0, final_score + 7.9)

  st.divider()

  # Display Metric Cards
  m1, m2, m3 = st.columns(3)
  m1.metric("🎯 Predicted Score", f"{final_score:.1f} / 100")
  m2.metric("📊 Expected Range", f"{low_est:.0f} – {high_est:.0f}")
  m3.metric("📈 vs. Class Avg (62.5)", f"{final_score - 62.5:+.1f} pts")

  st.progress(int(final_score))

  # Visual Comparison Bar Chart with Horizontal Labels
  fig, ax = plt.subplots(figsize=(6, 3.5))
  fig.patch.set_alpha(0.0)
  ax.patch.set_alpha(0.0)

  labels = ["Dataset Average", "Your Predicted Score"]
  values = [62.5, final_score]
  colors = ["#6c757d", "#1f77b4"]

  bars = ax.bar(labels, values, color=colors, width=0.45)
  ax.set_ylim(0, 110)
  ax.set_ylabel("Exam Score", color="white", fontsize=11)
  ax.tick_params(axis="x", colors="white", labelsize=11, rotation=0)
  ax.tick_params(axis="y", colors="white")
  ax.spines["top"].set_visible(False)
  ax.spines["right"].set_visible(False)
  ax.spines["left"].set_color("gray")
  ax.spines["bottom"].set_color("gray")

  for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:.1f}",
        xy=(bar.get_x() + bar.get_width() / 2, height + 2),
        ha="center",
        color="white",
        fontweight="bold",
        fontsize=11,
    )

  st.pyplot(fig)

  # Personalized AI Study Coach Advice
  st.subheader("💡 AI Study Coach Recommendations")
  tips = []
  if study_hours < 5.0:
    gain = (5.0 - study_hours) * 5.88
    tips.append(
        f"Increase daily study hours to **5.0 hrs** to gain roughly"
        f" **+{gain:.1f} points**."
    )
  if sleep_quality != "good":
    tips.append(
        "Improving **sleep quality to Good** adds **+4.7 to +9.3 points**."
    )
  if study_method == "self-study":
    tips.append(
        "Switching from pure self-study to **coaching or mixed study** adds"
        " **+4.5 to +9.5 points**."
    )
  if class_attendance < 85.0:
    tips.append(
        "Raising class attendance to **90%+** adds steady upward momentum."
    )

  if tips:
    for tip in tips:
      st.info(tip)
  else:
    st.success(
        "🔥 Your study habits are already optimized across all key drivers!"
    )
