#!/usr/bin/python3
#
from flask import Flask, jsonify, request, render_template
import yfinance as yf
import os, re

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

def get_stock_price(symbol):
    try:
        stock_data = yf.Ticker(symbol)
        history = stock_data.history(period='1d')
        if 'Close' in history and not history['Close'].empty:
            stock_price = history['Close'].iloc[-1]
            return stock_price
        else:
            raise ValueError("No closing price data available for " + symbol)
    except ValueError as ve:
        print("Value Error:", str(ve))
        return None
    except Exception as e:
        print("Unexpected Error:", str(e))
        return None


@app.route('/stock-price', methods=['GET'])
def stock_price():
    stock_symbol = request.args.get('symbol')
    if not stock_symbol:
        return jsonify({"error": "No stock symbol provided. Please include a 'symbol' query parameter."}), 400
    stock_symbol = stock_symbol.upper()
    pattern = r'^[A-Z0-9][A-Z0-9.]{0,7}[A-Z0-9]$'
    if not re.match(pattern, stock_symbol):
        return jsonify({"error": "Invalid stock symbol. Valid examples: AAPL, GOOGL, MSFT2."}), 400
    try:
        price = get_stock_price(stock_symbol)
        if price is not None:
            return jsonify({'symbol': stock_symbol, 'price': price}), 200
        else:
            return jsonify({'error': 'Stock symbol not found or no price available.'}), 404
    except Exception as e:
        print(f"Error retrieving stock price for {stock_symbol}: {str(e)}")
        return jsonify({'error': 'Internal server error when retrieving stock price.'}), 500


@app.route('/ask', methods=['POST'])
def ask():
    stock_symbol = request.form.get('stock_symbol', '')
    if not stock_symbol:
        return jsonify({"error": "No stock symbol provided. Please include a 'symbol' query parameter."}), 400
    stock_symbol = stock_symbol.upper()
    pattern = r'^[A-Z0-9][A-Z0-9.]{0,7}[A-Z0-9]$'
    if not re.match(pattern, stock_symbol):
        return jsonify({"error": "Invalid stock symbol. Valid examples: AAPL, GOOGL, MSFT2."}), 400
    try:
        price = get_stock_price(stock_symbol)
        if price is not None:
            return jsonify({'symbol': stock_symbol, 'price': price}), 200
        else:
            return jsonify({'error': 'Stock symbol not found or no price available.'}), 404
    except Exception as e:
        print(f"Error retrieving stock price for {stock_symbol}: {str(e)}")
        return jsonify({'error': 'Internal server error when retrieving stock price.'}), 500


@app.route('/chat')
def chat():
    version = os.getenv('SOFTWARE_VERSION', 'v0.0.0')
    return render_template('chat.html', version=version)


@app.route('/')
def home():
    return ("Hello GitLab!\nSoftware version: %s" % os.getenv('SOFTWARE_VERSION') )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
