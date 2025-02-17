# ☔ Weather Alert System

Stay prepared with **Weather Alert System**! This Python script fetches weather forecasts and sends an SMS notification via **Twilio** if rain is expected.

## 🚀 Features

✅ **Weather Forecasting** – Fetches hourly weather data for the next few hours.
✅ **Rain Detection** – Analyzes weather conditions and checks for rain.
✅ **SMS Notification** – Sends an alert via Twilio if rain is expected.
✅ **Customizable Location** – Modify latitude/longitude for different locations.

## 🔧 How It Works

### 1️⃣ Fetch Weather Data
The script uses **OpenWeatherMap API** to fetch the next **4-hour** weather forecast.

### 2️⃣ Detect Rain Conditions
If the weather condition code is below `700` (indicating rain, snow, or storms), the script triggers an SMS alert.

### 3️⃣ Send SMS Notification
The Twilio API is used to send an SMS notification with a rain alert.

## 🛠 Setup

### 🔑 API Keys Required
Before running the script, update `main.py` with your credentials:
```python
api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"
```

### 🌍 Choose Your Location
Modify the latitude (`lat`) and longitude (`lon`) in `weather_params` to monitor weather for your city:
```python
weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}
```

### 📩 Running the Script
Run the script to check for rain and receive SMS alerts:
```bash
python main.py
```
If rain is detected, an SMS will be sent to your verified Twilio number.

## 🌍 API Endpoints Used
- **Weather Data** → [OpenWeatherMap API](https://openweathermap.org/api)
- **SMS Alerts** → [Twilio API](https://www.twilio.com/)

## 🎨 Customization
🎯 **Change Notification Conditions** – Modify the threshold for rain detection.
📨 **Adjust Message Content** – Personalize the SMS alert text.
📍 **Track Multiple Locations** – Monitor weather for different cities by updating `lat` & `lon`.

## 📜 License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). Feel free to contribute and improve!

## 💡 Acknowledgments
✨ Powered by **OpenWeatherMap** for weather forecasts.
✨ Uses **Twilio API** for SMS alerts.

Stay prepared for any weather with real-time alerts! ☔📱
