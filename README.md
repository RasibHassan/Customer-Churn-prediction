Customer Churn Prediction Project

Project Overview
This project is part of the 10Pearls Shine Internship Program, aimed at building a machine learning model to predict customer churn in a telecom company. The project involves data preprocessing, exploratory data analysis (EDA), model training, API development, a MySQL database for data management, and a user-friendly interface built with Streamlit. The final solution is integrated with a Retrieval-Augmented Generation (RAG) system that uses the Gemini Large Language Model (LLM) for natural language queries on the database.


Features
Data Preprocessing & EDA: Includes handling missing values, encoding categorical variables, scaling numerical features, and balancing classes.
Model Training & Evaluation: Multiple machine learning models were evaluated, including Random Forest, Gradient Boosting, and XGBoost, with XGBoost selected as the final model.
SQL Database: A MySQL relational database designed to store customer and churn data, allowing for complex queries and reporting.
API Development: Flask API to serve churn prediction results in real-time.
Streamlit UI: An intuitive interface for users to input customer details and view churn predictions.
RAG & Gemini LLM Integration: Allows users to ask questions about the data in plain English, with queries translated into SQL for database interrogation.
Technologies Used
Python (Pandas, NumPy, Scikit-Learn, XGBoost, Flask, Streamlit)
MySQL for database management
Postman for API testing
Gemini LLM for natural language processing and RAG implementation
Docker (optional, if you used it for containerization)
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
Install Requirements: Make sure you have Python 3.8+ installed. Install required Python packages:

Usage
Data Preprocessing and Model Training: The notebooks in the notebooks/ folder walk through data cleaning, EDA, and model training steps.
API for Predictions: The Flask API takes customer information as input and returns a churn prediction.
Streamlit Interface: The UI allows users to input customer data manually and see if a customer is likely to churn.
Natural Language Database Queries: Using the RAG system and Gemini LLM, users can ask questions like "What is the churn rate for month-to-month contracts?" and receive answers in plain English.
Key Findings
High Churn Rates in Certain Segments: Customers with month-to-month contracts and those paying by electronic check showed higher churn rates.
Significance of Tenure: Shorter-tenure customers (less than a year) were more likely to churn.
Predictive Performance: The XGBoost model performed best with an accuracy of 80% and AUC-ROC of 0.75, making it a strong choice for deployment.
Future Enhancements
Additional Data Sources: Integrating other customer interaction data could enhance prediction accuracy.
Enhanced UI: Implementing visualizations within the Streamlit UI to display individual risk factors for each prediction.
Model Retraining: Automating the model retraining process based on new customer data to keep the predictions up-to-date.
Dockerization: Containerizing the application for easier deployment.
Contributors
Raib Hassan - Project Developer 
