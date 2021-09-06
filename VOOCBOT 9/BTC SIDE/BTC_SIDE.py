

from operator import index
import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import numpy as np
from APISS import*
import time

import datetime
import os
import sys
from scipy import stats, signal
import plotly.express as px
import plotly.graph_objects as go

from telebot import sendmsg
client = Client(api_key=Pkey, api_secret=Skey) 

i = True

ticker = "BTCUSDT"
        
while True :

        raw = client.get_historical_klines(ticker, Client.KLINE_INTERVAL_1HOUR, "5 day ago UTC")
        raw = pd.DataFrame(raw)
        
        if not raw.empty:
            raw[0] =  pd.to_datetime(raw[0],unit='ms')    
            raw.columns = ['timestamp','Open','High','Low','Close','Volume','IGNORE','quoteVolume','SELLVolume','BUY_VOL','BUY_VOL_VAL','x']
            # convert to numbers 
            raw ["Open"] = pd.to_numeric(raw["Open"])
            raw ["High"] = pd.to_numeric(raw["High"])
            raw ["Low"] = pd.to_numeric(raw["Low"])
            raw ["Close"] = pd.to_numeric(raw["Close"])
            raw ["Volume"] = round(pd.to_numeric(raw["Volume"]))
            raw ["quoteVolume"] = round(pd.to_numeric(raw["quoteVolume"]))
            raw ['IGNORE'] = pd.to_numeric(raw['IGNORE'])
            raw ['BUY_VOL'] = pd.to_numeric(raw['BUY_VOL'])
            raw ['BUY_VOL_VAL'] = pd.to_numeric(raw['BUY_VOL_VAL'])
            
            #print(raw)

            raw['UpperBand'] = raw['Close'].rolling(period).mean() + raw['Close'].rolling(period).std() * multiplier
            raw['LowerBand'] = raw['Close'].rolling(period).mean() - raw['Close'].rolling(period).std() * multiplier

            raw['EMA'] = raw.Close.ewm(span=100, adjust=False).mean()

            raw['EMAFAST'] = raw.Close.ewm(span=6, adjust=False).mean()

            lenraw = len(raw)-1
            lenraw2 = lenraw-1
            
            print(raw['EMA'][lenraw2]  ,"VS", raw['EMAFAST'][lenraw])

            if raw['LowerBand'][lenraw] > raw ["Open"][lenraw] :
                if raw['EMA'][lenraw2] > raw['EMAFAST'][lenraw] and i :
                    print(" BTC DWEN")
                    sendmsg("تحذير ❌🛑  هبوط البيتكوين ")

                    i = False
                    time.sleep(3600) 


            if raw['EMA'][lenraw2] < raw['EMAFAST'][lenraw] and not i :
                i = True
                                
                                    
        time.sleep(120)                          
                                    
                              
                                    
                

        



