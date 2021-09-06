import pandas as pd
import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import numpy as np 
import csv
import time
from pandas.core.frame import DataFrame
import requests
from pandas.core import api
from APISS import*
from scipy import stats
import datetime
import os
import datetime
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
api_key = os.environ.get(Pkey)
api_secret = os.environ.get(Skey)
clien = Client(api_key, api_secret)

client = Client(Pkey, Skey)
now = datetime.datetime.now()
pricess = {}

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


def DOGE_trade_history(msg):
	''' define how to process incoming WebSocket messages '''
	if msg['e'] != 'error':
		#print(msg)
		pricess["price_{0}".format(msg['s'])] = pd.to_numeric(msg['c'])

		
		
		
		

	else:
		try:
			#price_DOGE['error'] = True 
			print("error price") 
			
		except:
			print("error price ")
			
bsm = BinanceSocketManager(clien)

bsm.start()
df = pd.read_csv("databas_vooc.csv")
price_of_buy ={}
pr =0
report =[]
for ticker in df["tickers"] :
	print("=====loding PRICE .......",ticker)
	price_of_buy["price_buy{0}".format(ticker)]= df["price_of_buy"][pr]
	pricess["price_{0}".format(ticker)]= 0
	

	conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
	
	pr +=1

time.sleep(60)


for ticker in df["tickers"] :
	print (ticker," =" , pricess["price_{0}".format(ticker)])
	if pricess["price_{0}".format(ticker)] !=0:
			
		segnal_list = [{"ticker":ticker,"FROM":"VP","side":"SELL","price":pricess["price_{0}".format(ticker)]}]
		SIGNALS = pd.DataFrame(segnal_list)
		SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")
		time.sleep(10) 
		segnal_list = [{"ticker":ticker,"FROM":"ZC","side":"SELL","price":pricess["price_{0}".format(ticker)]}]
		SIGNALS = pd.DataFrame(segnal_list)
		SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")
		time.sleep(10)
		dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv" ,index_col=0)
		dfdata =dfdata.drop(index=ticker)
		dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")	   
try:
	first_number = pricess["price_{0}".format(ticker)]
	second_number = price_of_buy["price_buy{0}".format(ticker)]
	percent_diff = ((second_number - first_number)/first_number) * 100
	reportsheet = {"ticker":ticker,
					"price_of_buy":price_of_buy["price_buy{0}".format(ticker)],
					"price_of_sell":pricess["price_{0}".format(ticker)],

					"percentage_%":percent_diff}
	
	report.append(reportsheet)
	dfreport = pd.DataFrame(report)

	dfreport.to_csv("reportsheet.csv")

except:
	print("error repot")	