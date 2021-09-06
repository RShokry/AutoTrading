
import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import time
import datetime
import os
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
from APISS import*
client = Client(api_key=Pkey, api_secret=Skey) 
tckers = pd.read_csv('TICAR_GANERS.CSV')
tickers = tckers["ticker"]

def z(df, pd):
	mn = (df.Volume * df.Close).rolling(window=pd).sum() / (df.Volume).rolling(window=pd).sum()
	kkk = pow(df.Close - mn, 2)
	kk = kkk.rolling(window=pd).mean()
	vpd = np.sqrt(kk)
	return (df.Close - mn)/vpd


while True:
	for ticker in tickers:
		try:
			day1 = 20
			day = ("{} day ago UTC").format(day1)
			df = client.get_historical_klines(ticker , Client.KLINE_INTERVAL_30MINUTE, day)
			df = pd.DataFrame(df)
			if not df.empty:
				df[0] =  pd.to_datetime(df[0],unit='ms')    
				df.columns = ['timestamp','Open','High','Low','Close','Volume','IGNORE','quoteVolume','SELLVolume','BUY_VOL','BUY_VOL_VAL','x']
				# convert to numbers 
				df ["Open"] = pd.to_numeric(df["Open"])
				df ["High"] = pd.to_numeric(df["High"])
				df ["Low"] = pd.to_numeric(df["Low"])
				df ["Close"] = pd.to_numeric(df["Close"])
				df ["Volume"] = round(pd.to_numeric(df["Volume"]))
				df ["quoteVolume"] = round(pd.to_numeric(df["quoteVolume"]))
				df ['IGNORE'] = pd.to_numeric(df['IGNORE'])
				df ['BUY_VOL'] = pd.to_numeric(df['BUY_VOL'])
				df ['BUY_VOL_VAL'] = pd.to_numeric(df['BUY_VOL_VAL'])
				
				

				#df['Z1'] = z(df, 40)
				df['Z2'] = z(df, 200)
				len1=len(df)-1
				len2=len1-1
				len3=len2-1
				price = df ["Close"][len1]
				#print(df)
				#print("============{",ticker ,"} ",df['Z2'][len3], "Loading......============")
				if (df['Z2'][len1] > -2.5) and (df['Z2'][len2] < -2.5) and (df['Z2'][len3] < -2.5):
					
					
					segnal_list = [{"ticker":ticker}]

					SIGNALS = pd.DataFrame(segnal_list)
					SIGNALS.to_csv("NEW_COINS.csv")	
					
					print("YOU CAN BUY ", ticker)


		except:
			print("error")

	print("search again ...........")


