SELECT churn,
       COUNT(customerID) AS CustomerCount
FROM telco_churn.Churnpredictions
GROUP BY churn;


SELECT
    CASE
        WHEN tenure < 12 THEN 'Short-term'
        WHEN tenure BETWEEN 12 AND 24 THEN 'Mid-term'
        ELSE 'Long-term'
    END AS TenureSegment,
    COUNT(c.customerID) AS CustomerCount
FROM telco_churn.Customers AS c
GROUP BY TenureSegment;


SELECT b.Contract,
       cp.churn,
       COUNT(cp.customerID) AS CustomerCount
FROM telco_churn.Churnpredictions AS cp
JOIN telco_churn.Billing AS b ON cp.customerID = b.customerID
GROUP BY b.Contract, cp.churn
ORDER BY b.Contract, cp.churn;

SELECT b.Contract,
       cp.churn,
       COUNT(cp.customerID) AS CustomerCount
FROM telco_churn.churn_prediction AS cp
JOIN telco_churn.Billing AS b ON cp.customerID = b.customerID
GROUP BY b.Contract, cp.churn
ORDER BY b.Contract, cp.churn;

SELECT 
    s.InternetService,
    cp.churn,
    COUNT(cp.customerID) AS CustomerCount
FROM telco_churn.Churnpredictions AS cp
JOIN telco_churn.Services AS s ON cp.customerID = s.customerID
GROUP BY s.InternetService, cp.churn
ORDER BY s.InternetService, cp.churn;

