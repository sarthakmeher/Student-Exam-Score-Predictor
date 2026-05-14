import streamlit as st
import numpy as np
import pandas as pd
import joblib
import warnings

warnings.filterwarnings("ignore")

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("best_model.pkl")

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Exam Score Predictor",
    page_icon="📘",
    layout="centered"
)

# ============================================================
# TITLE
# ============================================================

st.title("📘 Student Exam Score Predictor")

st.markdown(
    """
    Predict student exam scores using Machine Learning.
    """
)

# ============================================================
# USER INPUTS
# ============================================================

study_hours = st.slider(
    "📚 Study Hours Per Day",
    0.0,
    12.0,
    4.0
)

attendance = st.slider(
    "🏫 Attendance Percentage",
    0.0,
    100.0,
    75.0
)

sleep_hours = st.slider(
    "😴 Sleep Hours",
    0.0,
    12.0,
    7.0
)

exercise_frequency = st.slider(
    "🏃 Exercise Frequency Per Week",
    0,
    7,
    3
)

mental_health = st.slider(
    "🧠 Mental Health Rating",
    1,
    10,
    5
)

social_media_hours = st.slider(
    "📱 Social Media Hours",
    0.0,
    12.0,
    2.0
)

netflix_hours = st.slider(
    "🎬 Netflix Hours",
    0.0,
    12.0,
    1.0
)

part_time_job = st.selectbox(
    "💼 Part-Time Job",
    ["No", "Yes"]
)

# ============================================================
# ENCODING
# ============================================================

ptj_encoded = 1 if part_time_job == "Yes" else 0

# ============================================================
# PREDICTION
# ============================================================

if st.button("Predict Exam Score"):

    # Create dataframe
    input_data = pd.DataFrame({

        "study_hours_per_day": [study_hours],

        "attendance_percentage": [attendance],

        "sleep_hours": [sleep_hours],

        "exercise_frequency": [exercise_frequency],

        "mental_health_rating": [mental_health],

        "social_media_hours": [social_media_hours],

        "netflix_hours": [netflix_hours],

        "part_time_job": [ptj_encoded]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Limit score range
    prediction = max(0, min(100, prediction))

    # ========================================================
    # OUTPUT
    # ========================================================

    st.success(
        f"🎯 Predicted Exam Score: {prediction:.2f}"
    )

    # Performance category
    if prediction >= 85:
        st.balloons()
        st.info("Excellent Performance 🚀")

    elif prediction >= 70:
        st.info("Good Performance 👍")

    elif prediction >= 50:
        st.warning("Average Performance 📖")

    else:
        st.error("Needs Improvement ⚠️")