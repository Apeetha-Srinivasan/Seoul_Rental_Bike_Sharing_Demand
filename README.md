<div align="center">

# 🚲 Seoul Bike Rental Prediction using Machine Learning

### Predicting hourly bike rental demand using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)

</div>

---

## 📌 Project Overview

A machine learning project for predicting hourly bike rental demand in Seoul using environmental, seasonal, temporal, and operational factors.

This project develops a regression-based machine learning solution to predict the number of bikes rented in Seoul using historical bike-sharing data.

### 🔄 Complete Machine Learning Workflow

```text
Data Loading
      ↓
Data Exploration
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Feature Selection
      ↓
Data Splitting
      ↓
Feature Scaling
      ↓
Model Development
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Deployment
```

Multiple regression algorithms were trained and compared to identify the best-performing model. The final optimized **XGBoost Regressor** was deployed as a **Flask web application** and containerized using **Docker**.

Detailed implementation code, visualizations, and analytical observations are available in the accompanying Jupyter Notebook.

---

# 🎯 Problem Statement

Bike rental demand varies depending on several factors, including weather conditions, seasonal variations, holidays, and time-related patterns. Accurately predicting demand can help bike-sharing operators improve resource allocation, reduce shortages and surpluses, and enhance operational efficiency.

The objective of this project is to develop a machine learning regression model capable of predicting the number of bikes rented based on historical rental and environmental data.

---

# 🎯 Objectives

- Analyze the Seoul Bike Rental dataset and identify factors influencing rental demand.
- Perform data preprocessing and data quality assessment.
- Conduct exploratory data analysis to identify trends and relationships.
- Engineer and select relevant features for model training.
- Train and compare multiple regression algorithms.
- Improve model performance through hyperparameter tuning.
- Evaluate models using appropriate regression metrics.
- Select the best-performing model for deployment.
- Develop a Flask-based web application for real-time predictions.
- Containerize the application using Docker.

---

# 📊 Dataset

The project uses the **Seoul Bike Sharing Demand Dataset**, which contains hourly bike rental records collected from the Seoul public bike-sharing system.

## Dataset Characteristics

| Property | Value |
|-----------|-------|
| Problem Type | Supervised Machine Learning – Regression |
| Target Variable | `Rented Bike Count` |
| Number of Records | 8,760 hourly observations |
| File Format | CSV |

### Key Features

- Date
- Hour
- Temperature (°C)
- Humidity (%)
- Wind Speed (m/s)
- Visibility (10 m)
- Dew Point Temperature (°C)
- Solar Radiation (MJ/m²)
- Rainfall (mm)
- Snowfall (cm)
- Seasons
- Holiday
- Functioning Day

---

# ⚙️ Machine Learning Workflow

<details>
<summary><b>1️⃣ Data Loading and Initial Exploration</b></summary>

The dataset was loaded using Pandas and examined to understand its structure, dimensions, feature types, statistical characteristics, and data quality.

The following checks were performed:

- Dataset preview
- Dataset dimensions
- Data types
- Descriptive statistics
- Missing value analysis
- Duplicate record detection
- Date format conversion

</details>

<details>
<summary><b>2️⃣ Exploratory Data Analysis</b></summary>

Exploratory Data Analysis was performed to understand feature distributions, trends, relationships, and potential outliers.

The analysis included:

- Univariate analysis
- Numerical feature distribution analysis
- Categorical feature analysis
- Skewness analysis
- Outlier analysis
- Bivariate analysis
- Scatter plots
- Correlation heatmap analysis

</details>

<details>
<summary><b>3️⃣ Feature Engineering</b></summary>

Additional time-based features were created to capture temporal patterns in bike rental demand.

The project includes:

- Month extraction from the Date column
- Weekend indicator creation
- Analysis of rental demand by month and day of the week

</details>

<details>
<summary><b>4️⃣ Categorical Feature Encoding</b></summary>

Categorical variables were converted into numerical representations suitable for machine learning.

- Label Encoding was applied to binary categorical variables such as `Holiday` and `Functioning Day`.
- One-Hot Encoding was applied to categorical variables such as `Seasons` and `Day_of_Week`.

</details>

<details>
<summary><b>5️⃣ Outlier Detection</b></summary>

The Interquartile Range (IQR) method was used to identify potential outliers in selected numerical features, including weather variables and bike rental demand.

</details>

<details>
<summary><b>6️⃣ Feature Selection</b></summary>

The `SelectKBest` method with `f_regression` was used to identify the most relevant features for predicting bike rental demand.

The top 12 relevant features were selected for model development.

</details>

<details>
<summary><b>7️⃣ Data Splitting and Scaling</b></summary>

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

A random state of **42** was used to ensure reproducibility.

Numerical features were standardized using `StandardScaler`. The scaler was fitted only on the training data to prevent data leakage.

</details>

---

# 🤖 Models Used

The following regression models were implemented and compared:

- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

# 🎛 Hyperparameter Tuning

Hyperparameter tuning was performed using `GridSearchCV`.

The tuning process explored important XGBoost parameters such as:

- `n_estimators`
- `max_depth`
- `learning_rate`
- `subsample`
- `colsample_bytree`

A **5-fold cross-validation** strategy was used with **R² Score** as the evaluation metric.

---

# 📈 Results

The tuned XGBoost Regressor achieved the best overall performance.

## R² Score Improvement

| Model | Before Tuning | After Tuning |
|---------|--------------:|-------------:|
| Decision Tree | 0.6956 | **0.8015** |
| Random Forest | 0.7324 | **0.8676** |
| XGBoost | **0.8698** | **0.8749** |

🏆 The tuned **XGBoost Regressor** achieved an **R² Score of 0.8749** and was selected as the final model for deployment.

---

# 🚀 Deployment

The final model was deployed as a web application using **Flask**.

Deployment steps include:

1. Saving the trained model using Joblib.
2. Saving the preprocessing components required for consistent predictions.
3. Creating a web interface for user input.
4. Processing input data using the same preprocessing workflow used during training.
5. Generating real-time bike rental predictions.
6. Containerizing the application using Docker.

---

# 📁 Project Structure

```text
SEOUL_RENTAL_BIKE_SHARING_DEMAND/
│
├── templates/
│   └── index.html
│
├── .dockerignore
├── app.py
├── Dockerfile
├── feature_names.pkl
├── main.ipynb
├── requirements.txt
├── SeoulBikeData.csv
└── xgboost_bike_model.pkl
```

> The exact file and folder names may vary depending on the final project implementation.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Flask
- Joblib
- Docker
- Jupyter Notebook

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd Seoul-Bike-Rental-Prediction
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Flask Application

```bash
python app.py
```

The application can then be accessed through the local Flask server.

---

## 4️⃣ Run Using Docker

Build the Docker image:

```bash
docker build -t seoul-bike-rental-prediction .
```

Run the container:

```bash
docker run -p 5000:5000 seoul-bike-rental-prediction
```

---

# 🔮 Future Scope

The project can be further enhanced by:

- Integrating real-time weather data through external APIs.
- Deploying the application on cloud platforms such as AWS, Azure, or Render.
- Developing a more interactive user interface with advanced visualizations.
- Experimenting with advanced machine learning and deep learning models.
- Implementing automated model retraining as new bike rental data becomes available.

---

# 📝 Conclusion

This project demonstrates the complete development of a machine learning solution for predicting bike rental demand. The workflow includes data exploration, preprocessing, feature engineering, feature selection, model development, hyperparameter tuning, evaluation, and deployment.

Among the models evaluated, the tuned **XGBoost Regressor** achieved the best performance with an **R² Score of 0.8749**. The final model was deployed through a Flask web application and containerized using Docker, providing a practical solution for real-time bike rental demand prediction.

---

<div align="center">

# 👨‍💻 Author

### Apeetha S

⭐ **If you find this project helpful, consider giving it a star!**

</div>
