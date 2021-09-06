print("Welcome MR AHMED SHADED")
import pyttsx3
engine = pyttsx3.init() 
rate = engine.getProperty('rate')  
engine.setProperty('rate', 150)
engine.say("hi sur")
D = "my name is math "
b = "Welcome mistar AHMED SADIED "
a = " i am hear to trade for you  "
cc="go to sllip"
aa = [D,b,a,cc]
engine.say(aa )
engine.runAndWait()
engine.stop()
             
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
from A__APISS import*

from scipy import stats

import os
from datetime import datetime
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

Pkey = list_apis[0]
Skey = list_secrit[0]
api_key = os.environ.get(Pkey)
api_secret = os.environ.get(Skey)
clien = Client(api_key, api_secret)

client = Client(Pkey, Skey)
now = datetime.now()
print(now)



try:

	os.remove('C__alertes.csv')	
except:
	aaaaaaaaaaaaaaaa=12545
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



def returnNotMatches(a, b):
	a = set(a)
	b = set(b)
	return list(a - b)

pricess = {}
def DOGE_trade_history(msg):
	''' define how to process incoming WebSocket messages '''
	if msg['e'] != 'error':
		#print(msg)
		pricess["price_{0}".format(msg['s'])] = pd.to_numeric(msg['c'])

		
		
		
		

	else:
		 
		print("The currency is not placed in N_tickers") 
			
		
			
bsm = BinanceSocketManager(clien)
#bsm.symbol_mark_price_socket
bsm.start()
#time.sleep(10) 
SUM_ALL_LOSTES = 0
SUM_PROFITS = 0
ALL_lostes = 0
BUY1 = 0
percent_diff =0
d = {}
dstop_traling = {}
dtraling_list = {}
dtreal = {}
dsell1 = {}
dbuy = {}
tims_start={}
i = 0
#{"tiker" :0 ,"teak_time":0  , "percentage_%":0 ,"ALL_ORDERS":0,"ORDERS_ENded":0,"lostes":0}
DF_ = []
enter_trealling = 0


ticker = "BTCUSDT"
pricess["price_{0}".format(ticker)] = 0
ORDERS = 0
ORDERS_ENded = 0
lostes = {}
percent_d = {}
BTC_STOPING = [0]
BTC_STOPING_2 = [0]
sum_rell_loses = 0
STOP_LOSE = []
lostes_coins = []
price_stop = 0
stop_2 = 0
stop = 0
qtyD = {}
price_of_buy={}
price_of_buy_low = {}										
#price_of_buy["price_buyhvn{0}".format(ticker)] = 0
#price_of_buy_low["price_buylow{0}".format(ticker)] = 0
BUY_PRICE ={}
N_tickers= []
NOW = []
NOW_2 = []
lens = 0
xlist = [0]
N = []
SFTY_ORDER = {}
dbuyn ={}
lostess = {}
PROFITS = {}
Dside = {}
DSTOPLOSING = {}
###############

#####################
samPROFITS_DF =0

side = "nan"

#########
balance = client.get_asset_balance(asset='BNB')

balance = pd.to_numeric(balance["free"])

##print(balance)
data = client.get_all_tickers()
df = pd.DataFrame(data)
df = pd.DataFrame(data, index = df["symbol"])
df ["price"] = pd.to_numeric(df["price"])
df = df["price"]
price =df.loc["BNBUSDT"]
print("price = ",price)

bnbusdt = balance*price
print("YOUR FREE BNB  =", bnbusdt)
if bnbusdt<=5:
        price =df.loc["BNBUSDT"]
        qty = Get_BNB_Orders/price
        minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
        qty = format_value(qty,minQty)
        try:
            order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
            print('BNB Order is done')
        except:
            print("Balance is not enough to buy BNB for fees")

###########################
print("ALLART BOT STARTING mr AHMED ")
print(" ================ loding...... =====================")	
while True:

						if N_tickers != []:

							for ticker in N_tickers :
								
								
								try:

									conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
								except:
									print("error pric")
									aaaaaaaaaa = 1455211455
						if i > lens :
							i=0
						if i ==0 :
									try:
										
										datiker = pd.read_csv("C__alertes.csv")
										
										datiker["side"]=datiker["side"].tolist()
										print(datiker)
										if datiker["side"][0]==1 :
											
												N = datiker["ticker"].tolist()
												NOW=returnNotMatches(N,N_tickers)
										
										
									
									except:	
										aaaaaaaa=1111111
										#print("ERROR RED FILL")
												
									try:
										if datiker["side"][0]==1 :

											if NOW :
												for ticker in NOW :
													#print(" ================ loding tikers n ...... =====================")
													
													lostess["lostess_{0}".format(ticker)] = 0
													PROFITS["PROFITS_{0}".format(ticker)] = 0
													dtraling_list["traling_list{0}".format(ticker)] = [0]
													dbuy["B1 {0}".format(ticker)] = 1 
													DSTOPLOSING["STOPLOSING_{0}".format(ticker)] = 0
													Dside["side{0}".format(ticker)] = 1
													dsell1["sell1{0}".format(ticker)] =0
													dstop_traling["stop_traling{0}".format(ticker)]=0
													pricess["price_{0}".format(ticker)] = 0
													percent_d["percent{0}".format(ticker)] = 0
													tims_start["percent{0}".format(ticker)] = 0
													lostes["lostes{0}".format(ticker)]=[0]
													qtyD["qty_{0}".format(ticker)] = 0
													N_tickers.append(ticker)
													
													
											
												
												
												print(N_tickers)
												NOW=[]
												os.remove('C__alertes.csv')
												print("remove csv 1")	
										
										
									except:	
										aaaaaaaa=1111111
										#print("ERROR ADD N TICKER")
						if N_tickers != []:			
							lens = len(N_tickers)-1
							ticker = N_tickers[i]
						
						try:
							ALERT = pd.read_csv("C__alertes.csv")
							for ttt in N_tickers :

								if ttt == ALERT["ticker"][0] :
									if ALERT["side"][0] ==2 :
										if dbuy["B1 {0}".format(ttt)] == 2:
										
											Dside["side{0}".format(ttt)] = 2
											os.remove('C__alertes.csv')
											print("remove csv 2")
									if ALERT["side"][0] ==1 :	
										os.remove('C__alertes.csv')
										print("remove csv 3")
							if ALERT["side"][0] ==2 :	
								os.remove('C__alertes.csv')
								print("remove csv 4")


													
						except:
							sssssss=111111111	

						
						#### ORDER BUY AND SELL ##########		
						if pricess["price_{0}".format(ticker)]!= 0 :



						
						
							############## ORDER BUY 1 ###############
							if dbuy["B1 {0}".format(ticker)] == 1 and Dside["side{0}".format(ticker)]==1 :	

									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)

									
									qtyD["qty_{0}".format(ticker)] = qty


											
									
									try :
										order = client.order_market_buy(symbol=ticker,quantity=qty)
										
										print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
										print("qty = " , qty )
										print(" ================ loding...... =====================")
									except:
										try :
												
													order = client.order_market_buy(symbol=ticker,quantity=qty)
													
												
													print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													print("qty = " , qty)
													print(" ================ loding...... =====================")
													
										except:
												
												print("Error buy ")
												print("Balance is not enough to buy or not have BNB enough ")
												dbuy["B1 {0}".format(ticker)] = 0
												Dside["side{0}".format(ticker)] = 0
											
												del N_tickers[i]
												lens = len(N_tickers)-1


												i= 0
												continue
												




											

									dbuy["B1 {0}".format(ticker)] = 2
									Dside["side{0}".format(ticker)] = 0
									
							
									ORDERS += 1
									
									

									d["BUY1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
									
									try:
										balance = client.get_asset_balance(asset='BNB')

										balance = pd.to_numeric(balance["free"])

										#print(balance)
										data = client.get_all_tickers()
										df = pd.DataFrame(data)
										df = pd.DataFrame(data, index = df["symbol"])
										df ["price"] = pd.to_numeric(df["price"])
										df = df["price"]
										price =df.loc["BNBUSDT"]
										#print(price)

										bnbusdt = balance*price
										#print(bnbusdt)
										if bnbusdt<=5:
												price =df.loc["BNBUSDT"]
												qty = Get_BNB_Orders/price
												minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
												qty = format_value(qty,minQty)
												try:
													order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
													print('BNB Order is done')
												except:
													print("Balance is not enough to buy BNB for fees")
									except:
												print("Balance is not enough to buy BNB for fees")

									

							############## ORDER sell ###############

							if dbuy["B1 {0}".format(ticker)] == 2 :
								

								################## $$$$$$$  order sell atr  $$$$$$$ #################
								
								tack_p = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*TACK_PROFIT)


								if Dside["side{0}".format(ticker)]==2 or pricess["price_{0}".format(ticker)] >= tack_p: 
								
									qty = qtyD["qty_{0}".format(ticker)]


									
									try :

											order = client.order_market_sell(symbol=ticker,quantity=qty)
									
											if pricess["price_{0}".format(ticker)] >= tack_p:
												print("tack profit order is   : ",ticker,"=",pricess["price_{0}".format(ticker)])

											if Dside["side{0}".format(ticker)]==2 :
													print("Target achieved  : ",ticker,"=",pricess["price_{0}".format(ticker)])
											
											print(" ================ loding...... =====================")
											
									except:
											try :
												order = client.order_market_sell(symbol=ticker,quantity=qty)
									
												if pricess["price_{0}".format(ticker)] >= tack_p:
													print("tack profit order is   : ",ticker,"=",pricess["price_{0}".format(ticker)])

												if Dside["side{0}".format(ticker)]==2 :
														print("Target achieved  : ",ticker,"=",pricess["price_{0}".format(ticker)])
												#print("qty = " , qty, "for api number =",se)
												print(" ================ loding...... =====================")

											except:
												
												print("Error sell")
												print("not have BNB enough or not buyed it ")


											
											
											
									

									
									
									dtraling_list["traling_list{0}".format(ticker)][0] = 0
									dsell1["sell1{0}".format(ticker)] = 0
									dstop_traling["stop_traling{0}".format(ticker)] = 0
									#print("price of sell", ticker, "=",pricess["price_{0}".format(ticker)])
									try:
										balance = client.get_asset_balance(asset='BNB')

										balance = pd.to_numeric(balance["free"])

										#print(balance)
										data = client.get_all_tickers()
										df = pd.DataFrame(data)
										df = pd.DataFrame(data, index = df["symbol"])
										df ["price"] = pd.to_numeric(df["price"])
										df = df["price"]
										price =df.loc["BNBUSDT"]
										#print(price)

										bnbusdt = balance*price
										#print(bnbusdt)
										if bnbusdt<=5:
												price =df.loc["BNBUSDT"]
												qty = Get_BNB_Orders/price
												minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
												qty = format_value(qty,minQty)
												try:
													order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
													print('BNB Order is done')
												except:
													print("Balance is not enough to buy BNB for fees")
									except:
												print("Balance is not enough to buy BNB for fees")
									
									try:
										ORDERS_ENded += 1

										first_number = pricess["price_{0}".format(ticker)]
										second_number = d["BUY1{0}".format(ticker)]
										percent_diff = ((second_number - first_number)/first_number) * 100
										if percent_diff < 0 :
											first_number = d["BUY1{0}".format(ticker)]
											second_number = pricess["price_{0}".format(ticker)]
											percent_diff = ((second_number - first_number)/first_number) * 100
											percent_diff = percent_diff - 0.15											

										percent_d["percent{0}".format(ticker)] = percent_diff
										


										resulting = "LOSE"
										if d["BUY1{0}".format(ticker)] > pricess["price_{0}".format(ticker)]:
											percent_diff = percent_diff-percent_diff-percent_diff
											resulting = "LOSE"
										if percent_diff > 0 :
											resulting = "profit"										

										lostes["lostes{0}".format(ticker)]=0
										DF_.append({"tiker" :ticker ,"SELL_FROM":"ALERT"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":percent_diff ,"resulting":resulting ,"ALL_ORDERS":ORDERS,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + percent_diff })
										DF= pd.DataFrame(DF_)
										SUM_PROFITS=sum(DF["percentage_%"])
										
										DF.to_csv("Results.csv",index=False)
										
							

									

									except:
										ssssssss = 00000
									
									lostes["lostes{0}".format(ticker)]=0
									dbuy["B1 {0}".format(ticker)] = 6
									Dside["side{0}".format(ticker)] = 0
									del N_tickers[i]
									lens = len(N_tickers)-1
									i = 0
									continue
								if STOPING != 0 :
									SL_Price = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*STOPING)
									if  pricess["price_{0}".format(ticker)] <= SL_Price : 
									
										qty = qtyD["qty_{0}".format(ticker)]


										
										try :

												order = client.order_market_sell(symbol=ticker,quantity=qty)
												
												print("Stop lose order is placed  : ",ticker,"=",pricess["price_{0}".format(ticker)])
												
												print(" ================ loding...... =====================")
												
										except:
												try :
													order = client.order_market_sell(symbol=ticker,quantity=qty)
													
													print("Stop lose order is placed  : ",ticker,"=",pricess["price_{0}".format(ticker)])
													
													print(" ================ loding...... =====================")

												except:
													
													print("Error sell")
													print("not have BNB enough or not buyed it ")


										dtraling_list["traling_list{0}".format(ticker)][0] = 0
										dsell1["sell1{0}".format(ticker)] = 0
										dstop_traling["stop_traling{0}".format(ticker)] = 0
										#print("price of sell", ticker, "=",pricess["price_{0}".format(ticker)])
										try:
											balance = client.get_asset_balance(asset='BNB')

											balance = pd.to_numeric(balance["free"])

											#print(balance)
											data = client.get_all_tickers()
											df = pd.DataFrame(data)
											df = pd.DataFrame(data, index = df["symbol"])
											df ["price"] = pd.to_numeric(df["price"])
											df = df["price"]
											price =df.loc["BNBUSDT"]
											#print(price)

											bnbusdt = balance*price
											#print(bnbusdt)
											if bnbusdt<=5:
													price =df.loc["BNBUSDT"]
													qty = Get_BNB_Orders/price
													minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
													qty = format_value(qty,minQty)
													try:
														order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
														print('BNB Order is done')
													except:
														print("Balance is not enough to buy BNB for fees")
										except:
													print("Balance is not enough to buy BNB for fees")
										
										try:
											ORDERS_ENded += 1

											first_number = pricess["price_{0}".format(ticker)]
											second_number = d["BUY1{0}".format(ticker)]
											percent_diff = ((second_number - first_number)/first_number) * 100
											if percent_diff < 0 :
												first_number = d["BUY1{0}".format(ticker)]
												second_number = pricess["price_{0}".format(ticker)]
												percent_diff = ((second_number - first_number)/first_number) * 100
												percent_diff = percent_diff - 0.15											

											percent_d["percent{0}".format(ticker)] = percent_diff
											
				

											resulting = "LOSE"
											if d["BUY1{0}".format(ticker)] > pricess["price_{0}".format(ticker)]:
												percent_diff = percent_diff-percent_diff-percent_diff
												resulting = "LOSE"
											if percent_diff > 0 :
												resulting = "profit"										

											lostes["lostes{0}".format(ticker)]=0
											DF_.append({"tiker" :ticker ,"SELL_FROM":"stop_lose"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":percent_diff ,"resulting":resulting ,"ALL_ORDERS":ORDERS,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + percent_diff })
											DF= pd.DataFrame(DF_)
											SUM_PROFITS=sum(DF["percentage_%"])
											
											DF.to_csv("Results.csv",index=False)
											
									

										except:
											ssssssss = 00000
										
										lostes["lostes{0}".format(ticker)]=0
										dbuy["B1 {0}".format(ticker)] = 6
										Dside["side{0}".format(ticker)] = 0
										del N_tickers[i]
										lens = len(N_tickers)-1
										i = 0
										continue



						i += 1


						


