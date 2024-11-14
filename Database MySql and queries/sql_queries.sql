SELECT * FROM telco_churn.Customers WHERE tenure > 12 AND gender = 'Female';

SELECT customerID, MonthlyCharges
FROM telco_churn.Billing
WHERE MonthlyCharges > 50;

SELECT COUNT(customerID) AS TotalCustomers
FROM telco_churn.Customers;

SELECT AVG(tenure) AS AverageTenure
FROM telco_churn.customers;

SELECT customerID, Contract
FROM telco_churn.Billing
WHERE Contract = 'Month-to-month';