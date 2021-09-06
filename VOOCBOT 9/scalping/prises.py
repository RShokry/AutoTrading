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

import threading
import datetime
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from APISS import*

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
				#print("=====loding.......",ticker)
				pricess["price_{0}".format(ticker)]= 0


				conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)