# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:14:39 2024

@author: Piero
"""

import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    return data['Close'].iloc[-1]

#Example usage
stock_symbol = 'MSFT'
price = get_stock_price(stock_symbol)
print(f'The current price of {stock_symbol} is ${price}')