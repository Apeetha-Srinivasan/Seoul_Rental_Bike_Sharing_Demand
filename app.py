from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("xgboost_bike_model.pkl")

# Load feature names
feature_names = joblib.load("feature_names.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    data = pd.DataFrame({
        'Hour': [float(request.form['Hour'])],
        'Temperature(°C)': [float(request.form['Temperature'])],
        'Humidity(%)': [float(request.form['Humidity'])],
        'Wind speed (m/s)': [float(request.form['WindSpeed'])],
        'Visibility (10m)': [float(request.form['Visibility'])],
        'Solar Radiation (MJ/m2)': [float(request.form['SolarRadiation'])],
        'Rainfall(mm)': [float(request.form['Rainfall'])],
        'Snowfall (cm)': [float(request.form['Snowfall'])],
        'Functioning Day': [int(request.form['FunctioningDay'])],
        'Month': [int(request.form['Month'])],
        'Seasons_Summer': [int(request.form['Summer'])],
        'Seasons_Winter': [int(request.form['Winter'])]
    })

    data = data[feature_names]

    prediction = model.predict(data)

    return render_template(
        'index.html',
        prediction_text=f"Predicted Bike Rental Count : {prediction[0]:.2f}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)