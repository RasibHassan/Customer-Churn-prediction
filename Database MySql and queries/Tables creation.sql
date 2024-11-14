CREATE TABLE telco_churn.Customers (
    customerID VARCHAR(50) PRIMARY KEY,
    gender VARCHAR(10),
    SeniorCitizen VARCHAR(20),
    Partner VARCHAR(20),
    Dependents VARCHAR(20),
    tenure INT
);

CREATE TABLE telco_churn.Services (
    customerID VARCHAR(50),
    PhoneService VARCHAR(20),
    MultipleLines VARCHAR(20),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(20),
    OnlineBackup VARCHAR(20),
    DeviceProtection VARCHAR(20),
    TechSupport VARCHAR(20),
    StreamingTV VARCHAR(20),
    StreamingMovies VARCHAR(20),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);


CREATE TABLE telco_churn.Billing (
    customerID VARCHAR(50),
    Contract VARCHAR(20),
    PaperlessBilling VARCHAR(20),
    PaymentMethod VARCHAR(50),
    MonthlyCharges FLOAT,
    TotalCharges FLOAT,
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

CREATE TABLE telco_churn.ChurnPredictions (
    customerID VARCHAR(50) PRIMARY KEY,
    Churn VARCHAR(10),
	FOREIGN KEY (customerID) REFERENCES Customers(customerID)

);
