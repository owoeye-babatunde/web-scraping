# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:22:00 2021

@author: user
"""

import pandas as pd
import sqlalchemy
from binance.client import client
from binance import BinanceSocketManager

client = Client(api_key, api_secret)
bsm = BinanceSocketManager(client)
socket = bsm.trade_socket('BTCUSDT')

while True:
   await socket.__aenter__()
   msg = await socket.recv()
   frame = createframe(msg)
   frame.to_sql('BTCUSDT', engine, if_exists = 'append', index=False)
   print(frame)

def createframe(msg):
    df = pd.FataFrame(msg)
    df = df.loc[:, ['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df

createframe(msg)
engine = sqlalchemy.create_engin('sqlite:///BTCUSDTstream.db')

"""
second script
"""
import sqlalchemy
import pandas as pd
from binance.client import Client

client = Client(api_key, api_secret)
engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')
df = pd.read_sql('BTCUSDT', engine)
df
df.price.plot

# Creating Trendfollowing Strategy
# if the crypto was rising by x%  Buy
## exit when profit is above 0.15% or loss is crossing -0.15%

def strategy(entry, lookback, qty, open_position=False):
    while True:
        df = pd.read_sql('BTCUSDT', engine)
        lookbackperiod = df.iloc [-lookback:]
        cumret = (lookbackperiod.Price.pct_change() +1).cumprod() - 1
        if not open_position:
            if cumret[cumret.last_valid_index()] > entry:
                order = client.create_order(symbol='BTCUSDT',
                                            side = 'BUY',
                                            type = 'Market',
                                            quantity=qty)
                print(order)
                open_position = True
                break
    if open_position:
         df = pd.read_sql('BTCUSDT', engine)
         sincebuy = df.loc[df.Time > 
                           pd.to_datetime(order['transactTime'],
                                                    unit='ms')]
    if len(sincebuy) > 1:
        sincebuyret = (sincebuy.Price.pct_change() + 1).cumprod() - 1
        last_entry = sincebuyret[sincebuyret.last_valid_index()]
        if last_entry > 0.0015 or last_entry < -0.0015:
            order = client.create_order(symbol='BTCUSDT',
                                            side = 'BUY',
                                            type = 'Market',
                                            quantity=qty)
            print(order)
            break
strategy(0.001, 60, 0.001)
