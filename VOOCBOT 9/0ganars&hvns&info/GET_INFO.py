from operator import index
import binance.client 
from binance.client import Client 
import pandas as pd 
import numpy as np 
import csv
import time
from APISS import*
client = Client(Pkey, Skey)
	
dec={}
tickers =[]
prices = client.get_all_tickers()
prices = pd.DataFrame(prices)
tickers_1 = prices["symbol"]
print(prices)
print(tickers_1)
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
