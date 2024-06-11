# Telco_Customer_Churn
Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs

Idea 2: Customer Churn Prediction

Final Project : AI Engineering, QarirGenerator

I. Business Understanding
About Dataset:
Context "Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]
Content Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:
Customers who left within the last month – the column is called Churn Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges Demographic info about customers – gender, age range, and if they have partners and dependents Inspiration To explore this type of models and learn more about the subject.

New version from IBM: https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113

Data Sheet = WA_Fn-UseC_-Telco-Customer-Churn.csv
https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data?select=WA_Fn-UseC_-Telco-Customer-Churn.csv

7,043 rows × 21 columns

977.5 KB

II. Methods Used
Exploratory Data Analysis (EDA)
Data Preprocessing
Feature Engineering : One Hot Encoding, SMOTE (Synthetic Minority Over-sampling Technique)
Model Development : LogisticRegression, DecissionTreeClassifier, RandomForestClassifier
Model Evaluation
Web Interface Development (Streamlit)
API Development (fastAPI) (sedang Progress)
Containerization (Docker) (sedang Progress)

III. Project Structure
The project is organized as follows: https://github.com/Yendri-Kilauan/Telco_Customer_Churn/blob/main/source%20code/Edit_Telco_Customer_Churn.ipynb


├── EDA

│	└── Edit_Telco_Customer_Churn.ipynb    # Notebook for Exploratory Data Analysis
 
├── Model 

│	└── logistic.joblib        # Trained LogisticRegression model

│	└── dtree.joblib           # Trained DecissionTreeClassifier model

│   └── rforest.joblib         # Trained RandomForestClassifier model

├── Source

│	└── app1.py                 # Streamlit web application LogisticRegression

|	└── app2.py                 # Streamlit web application DecissionTreeClassifier

|	└── app3.py                 # Streamlit web application RandomForestClassifier

│└── fast-api.py             # api script (sedang Progress)

├── Dockerfile                  # Dockerfile for containerization (sedang progress)
│
├── requirements.txt            # Python dependencies
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv    # Dataset
│
└── README.md                   # Project documentation

IV. Results
The RandomForestClassifier model achieved an accuracy of 85%, LogisticRegression of 82%, DecissionTreeClassifier of 80% on the test dataset. 
#The model is deployed as a web service using FastAPI and Docker, allowing for easy integration with other systems. (Sedang Progress)

V. How to run Webapp
Navigate to the src directory and run the Streamlit app
cd source code, cd streamlit

streamlit run app1.py   #LogisticRegression
streamlit run app2.py   #DecissionTreeClassifier
streamlit run app3.py   #RandomForestClassifier

Open your browser and go to http://localhost:8501

VI. Conclusion
This project demonstrates an end-to-end machine learning workflow, from data analysis to model deployment. 
#The use of Docker ensures that the application can be easily deployed and scaled. (Sedang Progress)




