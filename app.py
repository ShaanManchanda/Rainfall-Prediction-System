from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import pickle

app = Flask(__name__, template_folder="template")
model = pickle.load(open("./models/cat.pkl", "rb"))
print("Model Loaded")

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        # DATE
        date = request.form['date']
        try:
            date_dt = pd.to_datetime(date, infer_datetime_format=True)
            day = float(date_dt.day)
            month = float(date_dt.month)
        except ValueError:
            # Handle the case when the format doesn't match
            
            day = None
            month = None

        # MinTemp
        minTemp = convert_to_float(request.form['mintemp'])
        # MaxTemp
        maxTemp = convert_to_float(request.form['maxtemp'])
        # Rainfall
        rainfall = convert_to_float(request.form['rainfall'])
        # Evaporation
        evaporation = convert_to_float(request.form['evaporation'])
        # Sunshine
        sunshine = convert_to_float(request.form['sunshine'])
        # Wind Gust Speed
        windGustSpeed = convert_to_float(request.form['windgustspeed'])
        # Wind Speed 9am
        windSpeed9am = convert_to_float(request.form['windspeed9am'])
        # Wind Speed 3pm
        windSpeed3pm = convert_to_float(request.form['windspeed3pm'])
        # Humidity 9am
        humidity9am = convert_to_float(request.form['humidity9am'])
        # Humidity 3pm
        humidity3pm = convert_to_float(request.form['humidity3pm'])
        # Pressure 9am
        pressure9am = convert_to_float(request.form['pressure9am'])
        # Pressure 3pm
        pressure3pm = convert_to_float(request.form['pressure3pm'])
        # Temperature 9am
        temp9am = convert_to_float(request.form['temp9am'])
        # Temperature 3pm
        temp3pm = convert_to_float(request.form['temp3pm'])
        # Cloud 9am
        cloud9am = convert_to_float(request.form['cloud9am'])
        # Cloud 3pm
        cloud3pm = convert_to_float(request.form['cloud3pm'])
        # Cloud 3pm
        location = convert_to_float(request.form['location'])
        # Wind Dir 9am
        winddDir9am = convert_to_float(request.form['winddir9am'])
        # Wind Dir 3pm
        winddDir3pm = convert_to_float(request.form['winddir3pm'])
        # Wind Gust Dir
        windGustDir = convert_to_float(request.form['windgustdir'])
        # Rain Today
        rainToday = convert_to_float(request.form['raintoday'])

        input_lst = [location, minTemp, maxTemp, rainfall, evaporation, sunshine,
                     windGustDir, windGustSpeed, winddDir9am, winddDir3pm, windSpeed9am, windSpeed3pm,
                     humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm,
                     rainToday, month, day]
        pred = model.predict([input_lst])
        output = pred[0]

        if output == 0:
            return render_template("after_sunny.html")
        else:
            return render_template("after_rainy.html")

    return render_template("predictor.html")

if __name__ == '__main__':
    app.run(debug=True)
