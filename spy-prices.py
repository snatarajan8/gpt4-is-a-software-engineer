import yfinance as yf
import pandas as pd

def get_spy_data():
    # Fetch data for SPY. The period="max" parameter fetches all available data.
    spy = yf.Ticker("SPY")
    hist = spy.history(period="max")

    # Write the data to spy-prices.csv
    hist.to_csv("spy-prices.csv")

    print("Data saved to spy-prices.csv")

if __name__ == "__main__":
    get_spy_data()
