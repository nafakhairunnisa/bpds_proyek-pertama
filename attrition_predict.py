import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model dan encoders
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('label_encoders.pkl', 'rb') as le_file:
    label_encoders = pickle.load(le_file)

st.title("Attrition Prediction")

job_role = st.selectbox(
    "Job Role",
    ("Human Resources", "Healthcare Representative", "Research Scientist",
    "Sales Executive", "Manager", "Laboratory Technician", "Research Director",
    "Manufacturing Director", "Sales Representative"),
)
over_time = st.checkbox("Over Time")
marital_status = st.selectbox(
    "Marital Status",
    ("Married", "Single", "Divorced"),
)
job_satisfaction = st.radio(
    "Job Satisfaction",
    ["1", "2", "3", "4"],
    index=None,
    horizontal=True,
)
distance_from_home = st.number_input("Distance from Home (km)")
monthly_income = st.slider("Monthly Income", 0, 30000, 4000)
years_at_company = st.number_input("Years at Company")

# Mapping untuk "Over Time" sebagai checkbox
over_time_mapping = {"Yes": 1, "No": 0}

predict = st.button("Predict Attrition")

if predict:
    # OverTime dengan checkbox
    over_time_value = "Yes" if over_time else "No"

    # Transform categorical features
    job_role_encoded = label_encoders['JobRole'].transform([job_role])[0]
    over_time_encoded = over_time_mapping[over_time_value] # Mapping untuk OverTime
    marital_status_encoded = label_encoders['MaritalStatus'].transform([marital_status])[0]

    # JobSatisfaction
    job_satisfaction_value = int(job_satisfaction) if job_satisfaction is not None else 0 # Default to 0 atau handle sesuai kebutuhan

    features = pd.DataFrame({
        'JobRole': [job_role_encoded],
        'OverTime': [over_time_encoded],
        'MaritalStatus': [marital_status_encoded],
        'JobSatisfaction': [job_satisfaction_value],
        'DistanceFromHome': [distance_from_home],
        'MonthlyIncome': [monthly_income],
        'YearsAtCompany': [years_at_company]
    })

    prediction = model.predict(features)
    probability = model.predict_proba(features)

    if prediction[0] == 1: # 1 artinya "resign"
        st.write(f":warning: The employee is predicted to resign (Probability: {probability[0][1]:.2f})")
    else: # 0 artinya "stay"
        st.write(f":heavy_check_mark: The employee is predicted to stay (Probability: {probability[0][0]:.2f})")
else:
    st.write("Click 'Predict Attrition' to see the prediction.")

st.caption("© 2025 Attrition Prediction")