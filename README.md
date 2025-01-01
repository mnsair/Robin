# 📈 **Robinhood - Automated Stock Trading Bot**

## 🚀 **Overview**

Welcome to the **Automated Stock Trading Bot**, a Python-based project designed to autonomously execute stock trades on Robinhood based on predefined technical indicators. This bot combines **live data analysis**, **dynamic trading strategies**, and **secure session management** to simplify trading workflows.

### 🛡️ **Disclaimer**
This bot is for **educational purposes only** and does **not constitute financial advice**. Use it responsibly and at your own risk.

---

## 🔑 **Core Features**

- **Secure Login:** Safe session management with encrypted credentials.
- **Trading Strategy:** Technical indicators like **9EMA**, **VWAP**, and **50SMA**.
- **Dynamic Order Execution:** Automated buy and sell based on preset conditions.
- **Error Handling:** Graceful retries and monitoring mechanisms.
- **Session Persistence:** Persistent sessions with minimal manual intervention.

---

## 📊 **How It Works**

### ✅ **Buy Conditions**
1. **5-Minute Chart:** **9EMA > VWAP**
2. **1-Minute Chart:** **9EMA crosses above 50SMA**

### 💵 **Sell Execution**
- Automatically sets a **Sell Limit Order** at **Buy Price + $1 Profit Margin**.

### 📅 **Market Hours**
- Operates only during **live trading hours** (Monday to Friday, 9:00 AM - 4:00 PM EST).

---

## 🛠️ **Technology Stack**

- **Python 3.x**
- **Robin Stocks API**
- **Yahoo Finance API**
- **Pandas** for data analysis
- **Pickle** for session storage

Install dependencies:
```bash
pip install robin_stocks pandas yfinance
```

---

## 💻 **Setup Guide**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/trading-bot.git
   cd trading-bot
   ```
2. **Create Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   .\env\Scripts\activate   # Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Bot**
   ```bash
   python trading_bot.py
   ```
---
## 🎯 **Project Documentation**
- 📚 [Robinhood Trading Bot](https://github.com/mnsair/Robin/blob/main/Trading%20Bot%20Documentation.md)
---

## 📚 **File Structure**
- **credentials.py:** Manages secure login and session storage.
- **strategy.py:** Defines the buy/sell logic using technical indicators.
- **trading_bot.py:** Orchestrates login, market validation, and trading strategy.

---

## 🎯 **Why Use This Bot?**
- 🚀 **Save Time:** Automate repetitive trading tasks.
- 📊 **Data-Driven Decisions:** Leverage technical indicators for better trades.
- 💻 **Customizable:** Modify strategies and parameters easily.

---

## 🤝 **Let's Connect!**

I'm excited to hear your feedback, ideas, and collaboration proposals! 

- 📧 **[Email Me](mailto:naumansair@outlook.com)**
- 🐦 [**X Profile**](https://x.com/NaumanSair)
- 📊 [**Kaggle Profile**](https://www.kaggle.com/muhammadsair)

Feel free to **open an issue** or **start a discussion** here on GitHub.

---

⭐ **If you find this project helpful, please consider giving it a star!** 🚀

Happy Trading! 📈💼

---

