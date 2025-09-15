📊 Customer Churn Prediction

Predicting customer churn is critical for businesses to retain valuable customers and improve revenue. This project demonstrates a complete pipeline—from data analysis to building a web application for churn prediction using machine learning.

🔹 Project Overview

Customer churn occurs when a customer stops using a company's product or service. Predicting churn helps businesses proactively retain customers through targeted interventions.

Objectives:

Analyze customer data to identify patterns of churn.

Build machine learning models to predict churn.

Deploy an interactive web app for real-time predictions.

🗂️ Dataset

Source: Telco Customer Churn Dataset

Features: Customer demographics, account information, services subscribed, usage patterns.

Target Variable: Churn (Yes/No)

🛠️ Tools & Technologies

Data Analysis: Python, Pandas, NumPy, Matplotlib, Seaborn

Machine Learning: Scikit-learn

Web Deployment: Flask

Version Control: Git & GitHub

Visualization & Reporting: Jupyter Notebook

📈 Exploratory Data Analysis (EDA)

Checked for missing values and cleaned dataset.

Visualized correlations between features and churn.

Observed key patterns:

Customers with shorter tenure are more likely to churn.

Monthly charges and contract type influence churn probability.

Services like Internet, Phone, and Tech Support impact retention.

🤖 Machine Learning Model

Algorithms Used:

Logistic Regression

Random Forest Classifier

XGBoost (optional)

Evaluation Metrics:

Accuracy

Precision & Recall

ROC-AUC Score

Best Model: Random Forest achieved highest accuracy and balanced performance.

🌐 Web Application

Built using Flask to enable real-time predictions.

Users can input customer details to predict churn probability.

Simple and user-friendly interface for quick decision-making.

Screenshot of Web App:

🚀 How to Run

Clone the repository:

git clone https://github.com/satyajit2506/Customer-Churn.git


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open your browser and go to http://127.0.0.1:5000/

📊 Insights & Business Recommendations

Offer incentives for long-term contracts to reduce churn.

Focus on high-risk customers identified by the model.

Enhance services that influence retention (Tech Support, Online Security).

📂 Project Structure
customer-churn-prediction/
│
├── data/                # Dataset CSV files
├── notebooks/           # EDA & model training notebooks
├── app.py               # Flask web app
├── templates/           # HTML templates for web app
├── static/              # CSS & JS files
├── requirements.txt     # Python dependencies
└── README.md

🔗 Live Demo

http://127.0.0.1:5000

💡 Future Work

Integrate additional datasets for richer insights.

Implement advanced ML models like Neural Networks.

Deploy on cloud platforms for wider access.

📬 Contact

Email: tekawadesatyajeet@gmail.com

LinkedIn: www.linkedin.com/in/satyajit-tekawade-583748282
