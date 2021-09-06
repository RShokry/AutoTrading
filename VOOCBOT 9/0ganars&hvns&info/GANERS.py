from operator import index
import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import numpy as np
import threading
import time

import datetime
import os
import sys
import requests

from APISS import*
client = Client(api_key=Pkey, api_secret=Skey) 


resalt =[]



print(" running at time: " + str(int(time.time())) + " seconds.")

def format_value(valuetoformatx,fractionfactorx):
		
		
		value = valuetoformatx
		fractionfactor = fractionfactorx
		Precision = abs(int(f"{fractionfactor:e}".split("e")[-1]))
		FormattedValue = float("{:0.0{}f}".format(value, Precision))
		return FormattedValue		

def pairPriceinfo(ticker,linss):
		iI = 0
		
		while iI <= linss :
			if ticker == info["ticker"][iI] :
				minPrice = info["minPrice"][iI]
			iI+=1 
		return minPrice


def pairQtyinfo(ticker,linss):
		iI = 0
		
		while iI <= linss :
			if ticker == info["ticker"][iI] :
				minQty = info["minQty"][iI]
			iI+=1  

		return minQty 
info = pd.read_csv('info.csv')





tickers =[]
prices = client.get_all_tickers()
prices = pd.DataFrame(prices)
tickers_1 = prices["symbol"]

print(tickers_1)
for ticker in tickers_1 :
    if ticker[-4:] == "USDT" :
        tickers.append(ticker)
print(tickers)



def returnNotMatches(a, b):
	a = set(a)
	b = set(b)
	return list(a - b)

xislamic_coins = pd.read_csv('xislamic_coins.csv')



tickers =returnNotMatches(tickers, xislamic_coins["tickers"])
print(tickers)

for ticker in tickers :
        print(ticker ,"loding......")

    
        raw2 =client.get_klines(symbol=ticker, interval=Client.KLINE_INTERVAL_1MONTH)
        raw2 = pd.DataFrame(raw2)

        if not raw2.empty:
            raw2[0] =  pd.to_datetime(raw2[0],unit='ms')    
            raw2.columns = ['timestamp','Open','High','Low','Close','Volume','IGNORE','quoteVolume','SELLVolume','BUY_VOL','BUY_VOL_VAL','x']
            # convert to numbers 
            raw2 ["Open"] = pd.to_numeric(raw2["Open"])
            raw2 ["High"] = pd.to_numeric(raw2["High"])
            raw2 ["Low"] = pd.to_numeric(raw2["Low"])
            raw2 ["Close"] = pd.to_numeric(raw2["Close"])
            raw2 ["Volume"] = pd.to_numeric(raw2["Volume"])
            raw2 ["quoteVolume"] = pd.to_numeric(raw2["quoteVolume"])
            #print(raw2)
            #print(raw2 ["Open"].tail(1))


            lenraw = len(raw2)-1   
            price = raw2 ["Close"][lenraw]
            lenraw_1 = lenraw-1
            time_now = raw2 ["timestamp"][lenraw] 

            
            
    
            

                            
            masg = {"ticker":ticker,"price__now":price,"High" :raw2 ["High"][lenraw] ,"Low" :raw2 ["Low"][lenraw] ,"time":time_now,"sumvolume":raw2 ["Volume"][lenraw],"sumqtyvolume" :raw2 ["quoteVolume"][lenraw] }
            
            resalt.append(masg)
           


            
df = pd.DataFrame(resalt)              
df.to_string(index=False)
dfvolum = df["sumqtyvolume"]

dfvolum = sorted(dfvolum, reverse=True)

se = 0
tickersgainar  = []
for ticker in df["ticker"]:
    if (df["sumqtyvolume"][se] >= dfvolum[150]) and (df["time"][se] == df["time"][0] ):
        #first_number = df["Low"][se]
        
        #second_number = df["High"][se]
        #percent_diff = ((second_number - first_number)/first_number) * 100
        #print(percent_diff)

        #if percent_diff > 2 :

            tickersgainar.append({"ticker":ticker})
    se +=1

dft = pd.DataFrame(tickersgainar)
dft.to_csv("TICAR_GANERS.CSV",index=False)

dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\TICAR_GANERS.CSV",index=False)
dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\0New\TICAR_GANERS.CSV",index=False)
dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\scalping\TICAR_GANERS.CSV",index=False)
dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\1volumprofilstratgy\TICAR_GANERS.CSV",index=False)
dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\1zscorvwap\TICAR_GANERS.CSV",index=False)
dft.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\2newcoins&pops\TICAR_GANERS.CSV",index=False)

dec={}
tickers =[]
prices = client.get_all_tickers()
prices = pd.DataFrame(prices)
tickers_1 = prices["symbol"]

for ticker in tickers_1 :
    if (ticker[-4:] == "USDT") and (ticker != "EURUSDT") and (ticker != "TUSDUSDT") :
        tickers.append(ticker)
        print(ticker)



info_d =[]
for ticker in tickers :
	print("================loding==============")
	print(ticker)
	try:
		info = client.get_symbol_info(ticker)
	except:
		time.sleep(5)
		try:
			info = client.get_symbol_info(ticker)
		except:
			print ("error")	
			exit

	#print(info)
	#print(info["filters"][2])
	#LOT_SIZE =float(info["filters"][2]["LOT_SIZE"])

	minPrice = float(info["filters"][0]["minPrice"])

	minQty = float(info["filters"][2]["minQty"])
	print({"ticker":ticker,"minPrice":minPrice,"minQty":minQty})#,"LOT_SIZE" :LOT_SIZE})
	info_d.append({"ticker":ticker,"minPrice":minPrice,"minQty":minQty})#,"LOT_SIZE" :LOT_SIZE})
	



	time.sleep(0.5)



info_d = pd.DataFrame(info_d)

info_d.to_csv("info.csv",index=False)

def format_value(valuetoformatx,fractionfactorx):
		
		
		value = valuetoformatx
		fractionfactor = fractionfactorx
		Precision = abs(int(f"{fractionfactor:e}".split("e")[-1]))
		FormattedValue = float("{:0.0{}f}".format(value, Precision))
		return FormattedValue		

def pairPriceinfo(ticker,linss):
		i = 0
		
		while i <= linss :
			if ticker == info["ticker"][i] :
				minPrice = info["minPrice"][i]
			i+=1 
		return minPrice


def pairQtyinfo(ticker,linss):
		i = 0
		
		while i <= linss :
			if ticker == info["ticker"][i] :
				minQty = info["minQty"][i]
			i+=1  

		return minQty 


info = pd.read_csv('info.csv')
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\info.CSV",index=False)
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\0New\info.CSV",index=False)
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\scalping\info.CSV",index=False)
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\1volumprofilstratgy\info.CSV",index=False)
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\1zscorvwap\info.CSV",index=False)
info.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\2newcoins&pops\info.CSV",index=False)
