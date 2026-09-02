
# E-Commerce Product Analytics

## Project Overview
This project analyzes e-commerce business performance, digital funnel behavior, product performance, and refund patterns using SQL and Power BI. A machine learning model is also developed to predict whether a website session is likely to result in an order.

## Dataset
The project contains six main tables:

- Orders
- Order Items
- Order Item Refunds
- Products
- Website Sessions
- Website Pageviews

## Tools & Technologies
- SQL Server
- Python
- Pandas
- Scikit-learn
- Streamlit
- Power BI
- Jupyter Notebook

## SQL Data Validation & EDA
Data was validated for:
- Missing values
- Duplicate records
- Primary and foreign key consistency
- Data types
- Negative values
- Business-rule consistency

SQL EDA was performed to analyze revenue, orders, AOV, COGS, gross profit, sessions, conversion, products, refunds, marketing sources, devices, and trends.

## Power BI Dashboards

### 1. Business Performance Overview
Analyzes revenue, orders, AOV, COGS, gross profit, and product performance.

### 2. Digital Funnel & Conversion Analysis
Analyzes sessions, pageviews, orders, conversion rate, traffic sources, devices, and repeat sessions.

### 3. Product Performance & Refund Risk
Analyzes product revenue, COGS, refunds, refund rate, and product-level refund risk.

## Predictive Analytics

### Objective
Predict whether a website session will result in an order.

### Target Variable
`converted`

- 1 = Session resulted in an order
- 0 = Session did not result in an order

### Features
- is_repeat_session
- utm_source
- utm_campaign
- utm_content
- device_type
- http_referer

Categorical variables were processed using One-Hot Encoding and numerical variables were standardized.

### Models
- Logistic Regression
- Random Forest

### Final Model
Logistic Regression was selected as the final model because Random Forest did not provide an improvement over the baseline.

### Model Performance

- Accuracy: 36.90%
- Precision: 8.57%
- Recall: 85.19%
- F1 Score: 15.58%
- ROC-AUC: 0.6077

The model provides high recall, meaning it identifies most actual converting sessions, although precision remains low.

## Streamlit Application

A Streamlit web application was developed to accept session characteristics and generate:

- Conversion prediction
- Conversion probability

## Project Outcome

The project combines SQL analytics, Power BI visualization, predictive modeling, and a Streamlit application to provide an end-to-end e-commerce analytics solution.


## Live Application

Streamlit App:
https://e-commerce-business-analytics-izjxefgbmyyl73fozntsjy.streamlit.app/

## GitHub Repository

https://github.com/PritySingh1997/E-Commerce-Business-Analytics
