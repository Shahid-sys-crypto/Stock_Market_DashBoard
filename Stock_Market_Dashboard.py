import tkinter as tk
import pandas as pd
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_data():
    return pd.read_csv("stock_data.csv")

data=load_data()
root=tk.Tk()
root.title("Stock Market Dashboard")
root.geometry("600x500")
current_canvas=None

def plot_stock_data(stock):
    global current_canvas
    if current_canvas:
        current_canvas.get_tk_widget().destroy()
    filtered_data=data[data["stock"]==stock]
    fig=Figure(figsize=(6,4),dpi=100)
    ax=fig.add_subplot(111)
    ax.plot(filtered_data["date"],filtered_data["price"],marker="o")
    ax.set_title(f"{stock} stock prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    current_canvas=FigureCanvasTkAgg(fig,master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

stock_label=tk.Label(root,text="select stock")
stock_label.pack(pady=5)
stock_dropdown=ttk.Combobox(root,values=["AAPL","MSFT"])
stock_dropdown.pack(pady=5)

plot_button=tk.Button(root,text="plot stock data",command=lambda: plot_stock_data(stock_dropdown.get()),font=("Arial",10))
plot_button.pack(pady=5)

root.mainloop()
