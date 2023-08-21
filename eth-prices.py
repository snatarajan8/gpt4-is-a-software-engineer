import requests
import time
import csv
import os
from datetime import datetime
from flask import Flask, send_from_directory
import threading

COINGECKO_ETH_PRICE_ENDPOINT = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
CSV_FILE = "eth-prices.csv"

app = Flask(__name__)

@app.route('/get-eth-prices', methods=['GET'])
def get_eth_prices():
    return send_from_directory(directory=os.getcwd(), filename=CSV_FILE, as_attachment=True)

def get_ethereum_price():
    response = requests.get(COINGECKO_ETH_PRICE_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        return data['ethereum']['usd']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def notify(price):
    """
    Placeholder function to notify you about the current price of Ethereum.
    Implement your notification logic here.
    """
    print(f"Ethereum price is: ${price}")

def check_and_initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Time', 'Price'])

def append_to_csv(time, price):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time, price])

def fetch_prices_loop():
    check_and_initialize_csv()
    while True:
        price = get_ethereum_price()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if price:
            notify(price)
            append_to_csv(current_time, price)

        time.sleep(3600)

def start_server():
    t = threading.Thread(target=fetch_prices_loop)
    t.start()
    app.run(port=5000, debug=True)

if __name__ == "__main__":
    start_server()
