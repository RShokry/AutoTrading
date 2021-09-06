



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


from scipy import stats
import datetime
import os


import datetime
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor





now = datetime.datetime.now()


		

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
pricess = {}

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
			


def buy_bnb_fees(Pkey,Skey,se):					




			try:
				client =Client(api_key=Pkey,api_secret=Skey)
			except:
				print("no api" )
				
									
			
			try:
				balance_1BNB = client.get_asset_balance(asset='BNB')

				balance_BNB = pd.to_numeric(balance_1BNB["free"])

				balance_1USDT = client.get_asset_balance(asset='USDT')

				balance_USDT = pd.to_numeric(balance_1USDT["free"])
				print("balance_FREE_USDT  =",balance_USDT)
				print("balance_FREE_BNB  =",balance_BNB)

				data = client.get_all_tickers()
				df = pd.DataFrame(data)
				df = pd.DataFrame(data, index = df["symbol"])
				df ["price"] = pd.to_numeric(df["price"])
				df = df["price"]
				priceBNB =df.loc["BNBUSDT"]
				##print(price)

				bnbusdt = balance_BNB*priceBNB
				##print(bnbusdt)
		
				priceBNB =df.loc["BNBUSDT"]
				qtybnb = 20/priceBNB
				minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
				qtybnb = format_value(qtybnb,minQty)
				try:
					order = client.order_market_buy(symbol="BNBUSDT",quantity=qtybnb)
					print('BNB Order is done')
					print("test okkkkkk")
				except:
					print("Balance_BNB is not enough to buy BNB for fees",se)
			except:
				print("error bnb")
			

DF_API = pd.read_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\APIS_1000.CSV")

print ("enter se")
se = int(input())
Pkey =DF_API["Pkey"][se]
Skey =DF_API["Skey"][se]
print("name is  ",DF_API["NAME"][se])
print ("enter   1   to get balance_FREE_USDT")
ww=int(input())
client =Client(api_key=Pkey,api_secret=Skey)
balance_1USDT = client.get_asset_balance(asset='USDT')
balance_USDT = pd.to_numeric(balance_1USDT["free"])
print("balance_FREE_USDT  =",balance_USDT)

print ("enter 1 to buy bnb")
ww=int(input())

buy_bnb_fees(Pkey,Skey,se)
print ("enter 1 to buy coins")
ww=int(input())

DF_DATA = pd.read_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")
api_key = os.environ.get(Pkey)
api_secret = os.environ.get(Skey)
clien = Client(api_key, api_secret)
bsm = BinanceSocketManager(clien)

bsm.start()

price_of_buy ={}
pr =0
for ticker in DF_DATA["tickers"] :
	print("=====loding PRICE .......",ticker)
	price_of_buy["price_buy{0}".format(ticker)]= DF_DATA["price_of_buy"][pr]
	pricess["price_{0}".format(ticker)]= 0
	

	conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
	
	pr +=1

time.sleep(60)
i = 0
for ticker in DF_DATA["tickers"] :
	
	

	first_number = price_of_buy["price_buy{0}".format(ticker)] 
	
	second_number = pricess["price_{0}".format(ticker)]
	percent_diff = ((second_number - first_number)/first_number) * 100
	print(percent_diff)
	
	if percent_diff <= 5 :
			DF_DATABAIS = pd.read_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\zdata.CSV")
			USDT = DF_API["CAPITAL_MANGAGEMENT"][se]
			qty = USDT/pricess["price_{0}".format(ticker)]
			minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
			qty = format_value(qty,minQty)
							
			print(" ================ ",ticker ,"BUY loding...... =====================")

			order = client.order_market_buy(symbol=ticker,quantity=qty)
			pd.set_option('chained',None)
			DF_DATABAIS["qty_{0}{1}{2}".format(se,ticker,DF_DATA["FROM"][i])]=qty
			DF_DATABAIS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\zdata.CSV")
			print("BUY ORDER FILD ",ticker)

	i +=1

#1002,RAMY,@mohamedramy1,1000,24,"pM7xtGnrWJdujTF13pmdGatv6fzZCknkZg2SwIuUTAuAJZm6W6GHzpeFxrhmevFQ","fU3yohHr9eAWIbL7eZEQtaTsWhmmYfpCkYyyiLtQqkdX4sBVCLNkYj8M4iK6nxM6","2021-08-21",80
