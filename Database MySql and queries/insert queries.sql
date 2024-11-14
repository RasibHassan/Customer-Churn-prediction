INSERT INTO telco_churn.Customers (customerID, gender, SeniorCitizen, Partner, Dependents, tenure)
SELECT customerID, gender, SeniorCitizen, Partner, Dependents, tenure FROM telco_churn.dataset;

INSERT INTO telco_churn.Services (customerID, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies)
SELECT customerID, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies FROM telco_churn.dataset;

INSERT INTO telco_churn.Billing (customerID, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges)
SELECT customerID, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges FROM telco_churn.dataset;

INSERT INTO telco_churn.ChurnPredictions (customerID, Churn)
SELECT customerID, Churn FROM telco_churn.dataset;