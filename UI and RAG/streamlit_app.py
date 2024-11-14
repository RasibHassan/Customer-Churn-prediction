import streamlit as st
import requests

# Set up the Streamlit page configuration for a wide layout
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.markdown(
'''    
  <style>
    p {
        font-size: 20px!important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Define the URL of your Flask API
API_URL = "http://127.0.0.1:5000/predict"

# Set up the Streamlit interface
st.title("Customer Churn Prediction")
st.write("Fill in the details below to get a prediction on customer churn.")

# Use two columns for an evenly divided layout
col1, col2 = st.columns(2, gap="large")

# First column - numerical and some categorical inputs
with col2:
    st.header("Customer Details")
    gender = st.selectbox("Gender", ["Female", "Male"], help="Gender of the customer.")
    SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"], help="Is the customer a senior citizen?")
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, step=1 , help="Customer's tenure in months.")
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, step=0.1, help="Monthly charges for the customer.")
    TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, step=0.1, help="Total amount billed to the customer.")
    Partner = st.selectbox("Partner", ["Yes", "No"], help="Does the customer have a partner?")
    Dependents = st.selectbox("Dependents", ["Yes", "No"], help="Does the customer have dependents?")

    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], help="Type of customer contract.")
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ], help="Customer's chosen payment method.")

# Second column - remaining categorical inputs
with col1:
    st.header("Service & Contract Details")
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"], help="Does the customer subscribe to device protection?")
    TechSupport = st.selectbox("Tech Support", ["Yes", "No"], help="Does the customer subscribe to tech support?")
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"], help="Does the customer subscribe to streaming TV?")
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"], help="Does the customer subscribe to streaming movies?")
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"], help="Does the customer subscribe to online security?")
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"], help="Does the customer subscribe to online backup?")
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"], help="Is the customer enrolled in paperless billing?")
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"], help="Does the customer have phone service?")
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"], help="Does the customer have multiple phone lines?")
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], help="Type of internet service.")

# Prepare data for API request, including one-hot encoding for categorical features
data = {
    "SeniorCitizen": 1 if SeniorCitizen == "Yes" else 0,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "gender_Female": 1 if gender == "Female" else 0,
    "gender_Male": 1 if gender == "Male" else 0,
    "PhoneService_No": 1 if PhoneService == "No" else 0,
    "PhoneService_Yes": 1 if PhoneService == "Yes" else 0,
    "MultipleLines_No": 1 if MultipleLines == "No" else 0,
    "MultipleLines_Yes": 1 if MultipleLines == "Yes" else 0,
    "InternetService_DSL": 1 if InternetService == "DSL" else 0,
    "InternetService_Fiber optic": 1 if InternetService == "Fiber optic" else 0,
    "InternetService_No": 1 if InternetService == "No" else 0,
    "Partner_No": 1 if Partner == "No" else 0,
    "Partner_Yes": 1 if Partner == "Yes" else 0,
    "Dependents_No": 1 if Dependents == "No" else 0,
    "Dependents_Yes": 1 if Dependents == "Yes" else 0,
    "DeviceProtection_No": 1 if DeviceProtection == "No" else 0,
    "DeviceProtection_Yes": 1 if DeviceProtection == "Yes" else 0,
    "TechSupport_No": 1 if TechSupport == "No" else 0,
    "TechSupport_Yes": 1 if TechSupport == "Yes" else 0,
    "StreamingTV_No": 1 if StreamingTV == "No" else 0,
    "StreamingTV_Yes": 1 if StreamingTV == "Yes" else 0,
    "StreamingMovies_No": 1 if StreamingMovies == "No" else 0,
    "StreamingMovies_Yes": 1 if StreamingMovies == "Yes" else 0,
    "OnlineSecurity_No": 1 if OnlineSecurity == "No" else 0,
    "OnlineSecurity_Yes": 1 if OnlineSecurity == "Yes" else 0,
    "OnlineBackup_No": 1 if OnlineBackup == "No" else 0,
    "OnlineBackup_Yes": 1 if OnlineBackup == "Yes" else 0,
    "PaperlessBilling_No": 1 if PaperlessBilling == "No" else 0,
    "PaperlessBilling_Yes": 1 if PaperlessBilling == "Yes" else 0,
    "PaymentMethod_Bank transfer (automatic)": 1 if PaymentMethod == "Bank transfer (automatic)" else 0,
    "PaymentMethod_Credit card (automatic)": 1 if PaymentMethod == "Credit card (automatic)" else 0,
    "PaymentMethod_Electronic check": 1 if PaymentMethod == "Electronic check" else 0,
    "PaymentMethod_Mailed check": 1 if PaymentMethod == "Mailed check" else 0,
    "Contract_Month-to-month": 1 if Contract == "Month-to-month" else 0,
    "Contract_One year": 1 if Contract == "One year" else 0,
    "Contract_Two year": 1 if Contract == "Two year" else 0
}

# Using Streamlit's button to trigger prediction
with col2:
    st.write("Predict the outcome using the button below.")

    if st.button("Predict"):
        # Make a POST request to the API with the input data
        try:
            response = requests.post(API_URL, json=data)
            prediction = response.json().get("prediction")

            result = "Churn" if prediction == 1 else "No Churn"
            st.success(f"The predicted outcome is: **{result}**")
        except:
            st.error("Error: Could not retrieve prediction from the API.")
