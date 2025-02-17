# Stock Price & News Alert System

Stay informed about your favorite stocks with this **Stock Price & News Alert System**! This Python script tracks stock price changes and sends relevant news alerts via SMS using **Twilio**.

## 🚀 Features

✅ **Real-Time Stock Tracking** – Monitors daily stock price fluctuations.
✅ **News Fetching** – Retrieves top news articles if a significant price change is detected.
✅ **SMS Notifications** – Sends alerts directly to your phone using Twilio.
✅ **Customizable Threshold** – Modify the percentage change trigger as needed.

## 🔧 How It Works

### 1️⃣ Stock Price Monitoring
The script fetches stock data from **Alpha Vantage** and calculates the percentage change in price between yesterday and the day before yesterday.

### 2️⃣ Fetching News Articles
If the stock price fluctuates beyond the set threshold (default: **5%**), the script retrieves the top 3 latest news articles related to the company using **NewsAPI**.

### 3️⃣ Sending SMS Alerts
Each news article is formatted and sent to the user's phone via **Twilio SMS**.

## 🛠 Setup

### 🔑 API Keys Required
Before running the script, update `main.py` with your credentials:
```python
STOCK_API_KEY = "YOUR ALPHAVANTAGE API KEY"
NEWS_API_KEY = "YOUR NEWSAPI API KEY"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "YOUR TWILIO NUMBER"
VERIFIED_NUMBER = "YOUR VERIFIED PHONE NUMBER"
```

### 📈 Choose Your Stock
Modify the stock symbol and company name in `main.py`:
```python
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

### 📩 Running the Script
Execute the script to start tracking:
```bash
python main.py
```
If a significant stock movement is detected, you will receive SMS alerts with relevant news updates.

## 🌍 API Endpoints Used
- **Stock Data** → [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- **News Retrieval** → [NewsAPI](https://newsapi.org/)
- **SMS Alerts** → [Twilio API](https://www.twilio.com/)

## 🎨 Customization
🎯 **Adjust Threshold** – Change the trigger percentage to fit your needs.
📊 **Track Multiple Stocks** – Modify `STOCK_NAME` to monitor different companies.
📨 **Enhance Notifications** – Format SMS messages for better readability.
