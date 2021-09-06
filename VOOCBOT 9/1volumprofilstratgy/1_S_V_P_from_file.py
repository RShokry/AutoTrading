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
#bsm.symbol_mark_price_socket
bsm.start()
df = pd.read_csv("VOLUM_PROFIL_90_DAYS.csv")

for ticker in df["coins"]:
				print("=====loding.......",ticker)
				pricess["price_{0}".format(ticker)]= 0
				

				conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
				
time.sleep(20)
list_data = []
while True:
		df = pd.read_csv("VOLUM_PROFIL_90_DAYS.csv")
		
		A = 0


				

		for ticker in df["coins"] :               
							#print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
							if pricess["price_{0}".format(ticker)]!= 0 :
								if pricess["price_{0}".format(ticker)] > df["HVN__1"][A] and pricess["price_{0}".format(ticker)] < df["HVN__2"][A] :


									t1 = -25/100

									OR_2 = df["HVN__1"][A]+(df["HVN__1"][A]*t1)
									t2 = -50/100

									OR_3 = df["HVN__1"][A]+(df["HVN__1"][A]*t2)

									Ncoin = {"tickers":ticker , "OR_1" :df["HVN__1"][A],"OR_2":OR_2,"OR_3":OR_3} 
									
									list_data.append(Ncoin)

								if pricess["price_{0}".format(ticker)] > df["HVN__2"][A] and pricess["price_{0}".format(ticker)] < df["HVN__3"][A] :

									t1 = -25/100
									OR_3 = df["HVN__1"][A]+(df["HVN__1"][A]*t1)
									Ncoin = {"tickers":ticker , "OR_1" :df["HVN__2"][A],"OR_2":df["HVN__1"][A],"OR_3":OR_3} 
									list_data.append(Ncoin)
							
								if  pricess["price_{0}".format(ticker)] > df["HVN__3"][A] :
									Ncoin = {"tickers":ticker , "OR_1" :df["HVN__3"][A],"OR_2":df["HVN__2"][A],"OR_3":df["HVN__1"][A]} 
									list_data.append(Ncoin)
							

								#print(Ncoin)
							
						

							A += 1

		dfr = pd.DataFrame(list_data)
		dfr.to_csv("z.csv")
		#print(dfr)
		
		B = 0
		UP = 3/100
		DOWN = -3/100
		


		try:
			for ticker in dfr["tickers"] :
				print("=====loding.......",ticker )
				try:
					OR_1_up = dfr["OR_1"][B]+(dfr["OR_1"][B]*UP)
					OR_1_dow =dfr["OR_1"][B]+(dfr["OR_1"][B]*DOWN)
					if  pricess["price_{0}".format(ticker)] > OR_1_dow and pricess["price_{0}".format(ticker)] < OR_1_up:
						list_n_coin =[{"ticker":ticker,"OR_2":dfr["OR_2"][B],"OR_3":dfr["OR_3"][B]}]
						list_N = pd.DataFrame(list_n_coin)
						list_N.to_csv("NEW_COINS.csv")
						print("YOU CAN BUY ", ticker)
						time.sleep(15)
				except:
					print("error")
				B += 1

		except:
			print(os.error)





