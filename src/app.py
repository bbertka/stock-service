#!/usr/bin/python3
#
from flask import Flask, jsonify, request, render_template
import yfinance as yf
import os, re

app = Flask(__name__, template_folder=os.getcwd()+'/templates')

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
    stock_symbol = request.args.get('symbol').upper()
    pattern = r'^[A-Z0-9][A-Z0-9.]{0,7}[A-Z0-9]$'
    if not re.match(pattern, stock_symbol):
        return jsonify({"error": "Invalid stock symbol. Valid examples: AAPL, GOOGL, MSFT2."}), 400
    price = get_stock_price(stock_symbol)
    if price:
        return jsonify({'symbol': stock_symbol, 'price': price}), 200
    else:
        return jsonify({'error': 'Stock symbol not found or no price available.'}), 404


@app.route('/ask', methods=['POST'])
def ask():
    stock_symbol = request.form.get('stock_symbol', '').upper() 
    pattern = r'^[A-Z0-9][A-Z0-9.]{0,7}[A-Z0-9]$'
    if not re.match(pattern, stock_symbol):
        return jsonify({"error": "Invalid stock symbol. Valid examples: AAPL, GOOGL, MSFT2."}), 400
    price = get_stock_price(stock_symbol)
    if price:
        return jsonify({'symbol': stock_symbol, 'price': price}), 200
    else:
        return jsonify({'error': 'Stock symbol not found or no price available.'}), 404


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/')
def home():
    return "Hello GitLab!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
