from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

expected_columns = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',  
    'gender_Female', 'gender_Male', 'Partner_No', 'Partner_Yes',
    'Dependents_No', 'Dependents_Yes', 'PhoneService_No',
    'PhoneService_Yes', 'MultipleLines_No',
    'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_DSL', 'InternetService_Fiber optic',
    'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_Yes',
    'OnlineBackup_No', 'OnlineBackup_Yes', 'DeviceProtection_No',
    'DeviceProtection_Yes', 'TechSupport_No', 'TechSupport_Yes',
    'StreamingTV_No', 'StreamingTV_Yes', 'StreamingMovies_No',
    'StreamingMovies_Yes', 'Contract_Month-to-month', 'Contract_One year',
    'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes',
    'PaymentMethod_Bank transfer (automatic)',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  
    df = pd.DataFrame([data]) 
    
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0 

    df = df[expected_columns]

    prediction = model.predict(df)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
