import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("student_model.pkl")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #d0f0ff;
    }}
    .main-title {{
        text-align: center;
        color: #130f40;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        font-weight: bold;
    }}
    # .center-column {{
    #     background-color: #e6f7ff;
    #     padding: 2rem !important;
    #     border-radius: 20px;
    #     # box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    #     margin: 1rem;
    # }}
    .stSlider label {{
        color: #003366 !important;
        font-weight: bold !important;
        font-size: 2rem !important;
    }}
    .stSelectbox label {{
        color: #003366 !important;
        font-weight: bold !important;
        font-size: 1.3rem !important;
    }}
    .stButton > button {{
        background-color: #3399ff !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.8rem 2rem !important;
        font-weight: bold !important;
        width: 100% !important;
        font-size: 1.1rem !important;
        margin-top: 1rem !important;
    }}
    .stButton > button:hover {{
        background-color: #1a8cff !important;
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }}
    .stAlert {{
        background-color: rgba(76, 175, 80, 0.9) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📘 Student Exam Score Predictor</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown('<div class="center-column">', unsafe_allow_html=True)

    study_hours = st.slider("📚 Study hours per day", 0.0, 12.0, 4.0, step=0.5)
    attendance = st.slider("🏫 Attendance percentage", 0.0, 100.0, 70.0)
    mental_health = st.slider("🧠 Mental health rating (1-10)", 1, 10, 5)
    sleep_hours = st.slider("😴 Sleep hours per day", 0.0, 10.0, 7.0, step=0.5)
    part_time_job = st.selectbox("💼 Part-time job", ["no", "yes"])

    ptj = 1 if part_time_job == "yes" else 0

    if st.button("🎯 Predict Exam Score"):
        input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj]])
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))
        st.success(f"🎓 Predicted exam score: {prediction:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)
