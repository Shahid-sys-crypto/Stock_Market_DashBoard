# 📈 Stock Market Dashboard (Python + Tkinter + Matplotlib)

A simple desktop **Stock Market Dashboard** application built using **Python**, **Tkinter**, **Pandas**, and **Matplotlib**.

This application allows users to:
- 📊 Select a stock
- 📈 Visualize stock price trends
- 🔄 Load data from a CSV file
- 🖥️ Display graphs inside a GUI window

---

## 🚀 Features

- Dropdown selection for stocks
- Dynamic graph plotting
- Embedded Matplotlib charts inside Tkinter
- CSV-based data loading
- Clean and simple GUI layout

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- Pandas (Data Handling)
- Matplotlib (Data Visualization)

---

## 📂 Project Structure

Stock_Market_Dashboard.py
stock_data.csv
README.md


---

## 📄 Required CSV Format (`stock_data.csv`)

Your CSV file should look like this:

```csv
date,stock,price
2025-01-01,AAPL,145
2025-01-02,AAPL,150
2025-01-03,AAPL,147
2025-01-01,MSFT,240
2025-01-02,MSFT,245
2025-01-03,MSFT,243
▶️ How to Run the Project
1️⃣ Install Required Libraries
pip install pandas matplotlib
2️⃣ Run the Application
python Stock_Market_Dashboard.py
The Stock Market Dashboard window will open.

📝 How It Works
🔹 Load Data
The application reads stock data from stock_data.csv using Pandas.

🔹 Select Stock
Choose a stock from the dropdown menu (AAPL or MSFT).

🔹 Plot Data
Click Plot Stock Data

A line graph will appear showing stock prices over time.
