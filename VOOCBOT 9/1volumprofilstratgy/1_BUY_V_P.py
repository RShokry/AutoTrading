#from market_profile import MarketProfile
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
		try:
			#price_DOGE['error'] = True 
			print("error price") 
			
		except:
			print("error price ")
			
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
#{"tiker" :0 ,"teak_time":0  , percentage_%:0 ,"ALL_ORDERS":0,"ORDERS_ENded":0,"lostes":0}
DF_ = []
enter_trealling = 0
N_tickers = []
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
NOW = []
NOW_2 = []
lens = 0
xlist = ["BTCUSDT"]
N = []
SFTY_ORDER = {}
dbuyn ={}
lostess = {}
PROFITS = {}
DSTOPLOSING ={}
DSFITY_ORDER = {}
average_qty = {}
average_price = {}
sefty_order1 = {}
sefty_order2 = {}
xllist =[]

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
##print(price)

bnbusdt = balance*price
##print(bnbusdt)
if bnbusdt<=5:
		price =df.loc["BNBUSDT"]
		qty = Get_BNB_Orders/price
		minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
		qty = format_value(qty,minQty)
		try:
			#order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
			print('BNB Order is done')
		except:
			print("Balance is not enough to buy BNB for fees")

print("VOLUM PROFIL BOT WORKING")

print(" ================ loding...... =====================")	
while True:
						

						if i > lens :
							i=0
						if i == 0 :


									#####  x list
									try:
										now = datetime.datetime.now()
										
										df = pd .read_csv("x_coins.csv")

										df["time"] = pd.to_datetime(df["time"])
										df["tikers"] =df["tikers"].tolist()

										ixl = 0

										for xlee in df["tikers"].tolist():
											
											a =now - df["time"][ixl]
											if a.days >= 1 :
												linesxlx = len(xlist)-1
												xx = 0
												while xx < linesxlx:

													
													if xlee == xllist[xx]["tikers"]:
														try:

															#xllist = xllist.drop([xx])
															del xllist[xx]
														except:
															aaaa= 687896
													
													
													if  xlee == xlist[xx]:
														try:
															dfxx = pd.read_csv("x_coins.csv", index_col=0)
															dfxx = dfxx.drop(xlee, axis=0)

															dfxx.to_csv("x_coins.csv")
															print(xlee," removed from csv fill after 48 H")
															
															dfxxx = pd .read_csv("x_coins.csv")
															xlist = df["tikers"].tolist()
															print(xlist)
														except:
															aaaa= 687896







														
													xx += 1
											ixl +=1
									
									except:
										
											aaaaaa= 1122							
									
									if lens <= 8 :
										try:
											try:
												datiker = pd.read_csv("NEW_COINS.csv")
											except:
												aaaa=111
											
											if not datiker["ticker"].empty:
												N = datiker["ticker"].tolist()
												datiker["OR_2"] = datiker["OR_2"].tolist()
												datiker["OR_3"] = datiker["OR_3"].tolist() 
												sifty_1 = datiker["OR_2"][0]

												sifty_2 = datiker["OR_3"][0]
												NOW=returnNotMatches(N,N_tickers+xlist)
										
										except:
											#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")	
											aaaaaaaa=1111111
													
										try :
										
											if not datiker["ticker"].empty:
												linsNOW = len(NOW)
												if lens <= 8 :
														
													if linsNOW > 0:
														for ticker in NOW :
															#print(" ================ loding tikers n ...... =====================")
															conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
															time.sleep(5)
															lostess["lostess_{0}".format(ticker)] = 0
															PROFITS["PROFITS_{0}".format(ticker)] = 0
															dtraling_list["traling_list{0}".format(ticker)] = [0]
															dbuy["B1 {0}".format(ticker)] = 0
															DSTOPLOSING["STOPLOSING_{0}".format(ticker)] = 0
															
															dsell1["sell1{0}".format(ticker)] =0
															dstop_traling["stop_traling{0}".format(ticker)]=0
															pricess["price_{0}".format(ticker)] = 0
															percent_d["percent{0}".format(ticker)] = 0
															now = datetime.datetime.now()
															tims_start["percent{0}".format(ticker)] = now

															lostes["lostes{0}".format(ticker)]=[0]
															qtyD["qty_{0}".format(ticker)] = 0
															
															
															#sfty order
															DSFITY_ORDER["sifty_order{0}".format(ticker)] = 0
															sefty_order1["sifty_order_1{0}".format(ticker)]= sifty_1
															sefty_order2["sifty_order_2{0}".format(ticker)]= sifty_2
															# avredg
															average_qty["average_qty1{0}".format(ticker)] = 0
															average_price["average_price1{0}".format(ticker)] = 0
															
															average_qty["average_qty2{0}".format(ticker)] = 0
															average_price["average_price2{0}".format(ticker)] = 0									

															average_qty["average_qty3{0}".format(ticker)] = 0
															average_price["average_price3{0}".format(ticker)] = 0										
															N_tickers.append(ticker)
														print(N_tickers)
														NOW = []
														
														try:
															
															os.remove('NEW_COINS.csv')
														except:
															aaaa= 4442544
									
										except:
											aaaa= 1255
									if lens > 8 :
											try:
												datiker = pd.read_csv("NEW_COINS.csv")
										
											
												if not datiker["ticker"].empty:
													try:
														N = datiker["ticker"].tolist()
														NOW=returnNotMatches(N,N_tickers+xlist)
														
														
														if NOW != []:
															xNow = NOW[0]
															
													
															xl = {"tikers":xNow,"time":now}
															xllist.append(xl)
															dfx = pd.DataFrame(xllist)
															dfx.to_csv("x_coins.csv",index=False)
															df = pd.read_csv("x_coins.csv")
															xlist = df["tikers"].tolist()
															
															print("del  ",xNow , "becos we have so meny orders")
															print("xlist ========",xlist)
													except:
															aaaa= 4442544
												
												os.remove('NEW_COINS.csv')
											except:
												aaaa= 4442544

							
				
						if N_tickers != []:			
							lens = len(N_tickers)-1
							ticker = N_tickers[i]


						#### ORDER BUY AND SELL ##########		
						if pricess["price_{0}".format(ticker)]!= 0 and ticker != "BTCUSDT" :

							############## ORDER BUY 1 ###############
							if dbuy["B1 {0}".format(ticker)] == 0  and ticker != "BTCUSDT":	
									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)
									
									segnal_list = [{"ticker":ticker,"FROM":"VP","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")									
									"""									
									try :
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
										##print(price)

										bnbusdt = balance*price
										##print(bnbusdt)
										if bnbusdt<=5:
												price =df.loc["BNBUSDT"]
												qty = Get_BNB_Orders/price
												minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
												qty = format_value(qty,minQty)
												try:
													#order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
													print('BNB Order is done')
												except:
													print("Balance is not enough to buy BNB for fees")
									except:
											print("Balance is not enough to buy BNB for fees")
									
									"""
												
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									


									

							
											
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											print("qty = " , qty  )
										
									except:
											print("Error buy Balance is not enough to buy bnb")

											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													print("qty = " , qty)
													
											except:
												
												
												print("Error buy Balance is not enough to buy",ticker)
												print("==============loding......")
												dbuy["B1 {0}".format(ticker)] = 0
												xl = {"tikers":ticker,"time":now}
												xllist.append(xl)
												dfx = pd.DataFrame(xllist)
												dfx.to_csv("x_coins.csv",index=False)
												df = pd .read_csv("x_coins.csv")
												xlist = df["tikers"].tolist()  
												del N_tickers[i]
												lens = len(N_tickers)-1
												print("delete ",ticker)	
												i += 1
												continue


									
											
											
											

									
									
									dbuy["B1 {0}".format(ticker)] = 1
									qtyD["qty_{0}".format(ticker)] = qty

									tims_start["percent{0}".format(ticker)] = datetime.datetime.now()
									ORDERS += 1
									
									

									d["BUY1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]

									average_qty["average_qty1{0}".format(ticker)] = qty
									average_price["average_price1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
									
									try:
											
							

										dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")
										BAS =returnNotMatches(N_tickers,dfdata["tickers"])
										print(BAS)
										for tcoine in BAS :
											
												
													DATABE = {"tickers":tcoine, "FROM":"VP", "qty" :qty , "price_of_buy":average_price["average_price1{0}".format(ticker)] }
													dfdata =dfdata.append(DATABE,ignore_index=True)
													pd.set_option('chained',None)
													
													dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv",index=False)									

													print("data bais")

			
																	
									except:
										print("error data bais")								

						
									#tikers_lests = {"tikers":ticker,"time":now}
									#DATA SELL TREALLING
																	


									dtreal["T1 {0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t1)
									dtreal["T2{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t2)
									dtreal["T3{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t3)
									dtreal["T4{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t4)
									dtreal["T5{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t5)
									
									
									
									if pricess["price_{0}".format(ticker)]>= dtreal["T1 {0}".format(ticker)]:
										dsell1["sell1{0}".format(ticker)] = dtreal["T1 {0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS1)
										#print("sell 1")

									if pricess["price_{0}".format(ticker)]>= dtreal["T2{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T2{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS2)
										#print("sell 2")
									if pricess["price_{0}".format(ticker)]>= dtreal["T3{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T3{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS3)
										#print("sell 3")

									if pricess["price_{0}".format(ticker)]>= dtreal["T4{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T4{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS4)
										#print("sell 4")
									if pricess["price_{0}".format(ticker)]>= dtreal["T5{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T5{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS5)
										#print("sell 5")
								
############################################sfty order #########################################

							############## ORDER BUY 2 ###############
							
							
							if dbuy["B1 {0}".format(ticker)] == 1  and ticker != "BTCUSDT"	:
								
								if DSFITY_ORDER["sifty_order{0}".format(ticker)] == 0 and pricess["price_{0}".format(ticker)] <= sefty_order1["sifty_order_1{0}".format(ticker)]: 			
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)

									segnal_list = [{"ticker":ticker,"FROM":"VP","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")									
									
									try :
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
										##print(price)

										bnbusdt = balance*price
										##print(bnbusdt)
										if bnbusdt<=5:
												price =df.loc["BNBUSDT"]
												qty = Get_BNB_Orders/price
												minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
												qty = format_value(qty,minQty)
												try:
													#order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
													print('BNB Order is done')
												except:
													print("Balance is not enough to buy BNB for fees")
									except:
											print("Balance is not enough to buy BNB for fees")
									
									
									
									
									

						
									
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT sfty order 1  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											print("qty = " , qty )
										
									except:
											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT sfty order 1  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													print("qty = " , qty)
													
											except:
												
												
												print("Error buy Balance is not enough to buy sfty order 1",ticker)
												print("==============loding......")
												dbuy["B1 {0}".format(ticker)] = 1
												i += 1
												continue


											
								
											


									dbuy["B1 {0}".format(ticker)] = 1
									DSFITY_ORDER["sifty_order{0}".format(ticker)] = 1

									tims_start["percent{0}".format(ticker)] = datetime.datetime.now()
									
									# avredg
									average_qty["average_qty2{0}".format(ticker)] = qty
									average_price["average_price2{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
									qtyD["qty_{0}".format(ticker)] = qty + qtyD["qty_{0}".format(ticker)]
									d["BUY1{0}".format(ticker)] = ((average_price["average_price1{0}".format(ticker)] * average_qty["average_qty1{0}".format(ticker)]) + (average_price["average_price2{0}".format(ticker)] * average_qty["average_qty2{0}".format(ticker)]))/ (average_qty["average_qty1{0}".format(ticker)] + average_qty["average_qty2{0}".format(ticker)])
									print("average_price of ",ticker,"  = ",d["BUY1{0}".format(ticker)])
									#DATA SELL TREALLING
									

																	
									
									

									dtreal["T1 {0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t1)
									dtreal["T2{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t2)
									dtreal["T3{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t3)
									dtreal["T4{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t4)
									dtreal["T5{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t5)
									
									
									
									if pricess["price_{0}".format(ticker)]>= dtreal["T1 {0}".format(ticker)]:
										dsell1["sell1{0}".format(ticker)] = dtreal["T1 {0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS1)
										#print("sell 1")

									if pricess["price_{0}".format(ticker)]>= dtreal["T2{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T2{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS2)
										#print("sell 2")
									if pricess["price_{0}".format(ticker)]>= dtreal["T3{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T3{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS3)
										#print("sell 3")

									if pricess["price_{0}".format(ticker)]>= dtreal["T4{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T4{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS4)
										#print("sell 4")
									if pricess["price_{0}".format(ticker)]>= dtreal["T5{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T5{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS5)
										#print("sell 5")
							############## ORDER BUY 3 ###############
							if dbuy["B1 {0}".format(ticker)] == 1  and ticker != "BTCUSDT"	:
								if DSFITY_ORDER["sifty_order{0}".format(ticker)] == 1 and pricess["price_{0}".format(ticker)] <= sefty_order2["sifty_order_2{0}".format(ticker)]: 			
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									
									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)

									segnal_list = [{"ticker":ticker,"FROM":"VP","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")									
									
									try :
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
										##print(price)

										bnbusdt = balance*price
										##print(bnbusdt)
										if bnbusdt<=5:
												price =df.loc["BNBUSDT"]
												qty = Get_BNB_Orders/price
												minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
												qty = format_value(qty,minQty)
												try:
													#order = client.order_market_buy(symbol="BNBUSDT",quantity=qty)
													print('BNB Order is done')
												except:
													print("Balance is not enough to buy BNB for fees")
									except:
											print("Balance is not enough to buy BNB for fees")
									
																		
									qty = USDT/pricess["price_{0}".format(ticker)]



							
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT sfty order 2 : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											print("qty = " , qty )
										
									except:
											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT sfty order 2  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													print("qty = " , qty)
													
											except:
												
												print("Error buy Balance is not enough to buy sfty order 2",ticker)
												print("==============loding......")
												dbuy["B1 {0}".format(ticker)] = 1
												i += 1
												continue


									
											
									try:
											
										DATABES =[]
										for tcoine in N_tickers :
											DATABE = {"tickers":tcoine , "qty" :qtyD["qty_{0}".format(tcoine)] , "price_of_buy":d["BUY1{0}".format(tcoine)] }
											DATABES.append(DATABE)
											databes = pd.DataFrame(DATABES)
											databes.to_csv("databas_vooc.csv",index=False)									
									except:
										print("error data bais")									

										
											

									dbuy["B1 {0}".format(ticker)] = 1
									DSFITY_ORDER["sifty_order{0}".format(ticker)] = 2

									tims_start["percent{0}".format(ticker)] = datetime.datetime.now()
									
									# avredg
									average_qty["average_qty3{0}".format(ticker)] = qty
									average_price["average_price3{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
									qtyD["qty_{0}".format(ticker)] = qty + qtyD["qty_{0}".format(ticker)]
									d["BUY1{0}".format(ticker)] = ((average_price["average_price3{0}".format(ticker)]*average_qty["average_qty3{0}".format(ticker)])+( average_price["average_price1{0}".format(ticker)] * average_qty["average_qty1{0}".format(ticker)]) + (average_price["average_price2{0}".format(ticker)] * average_qty["average_qty2{0}".format(ticker)]))/ (average_qty["average_qty1{0}".format(ticker)] + average_qty["average_qty2{0}".format(ticker)] + average_qty["average_qty3{0}".format(ticker)])
																		
									qtyD["qty_{0}".format(ticker)] = qty + qtyD["qty_{0}".format(ticker)]
									
									

							
									#DATA SELL TREALLING
																	


									dtreal["T1 {0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t1)
									dtreal["T2{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t2)
									dtreal["T3{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t3)
									dtreal["T4{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t4)
									dtreal["T5{0}".format(ticker)] = d["BUY1{0}".format(ticker)]+(d["BUY1{0}".format(ticker)]*t5)
									
									
									
									if pricess["price_{0}".format(ticker)]>= dtreal["T1 {0}".format(ticker)]:
										dsell1["sell1{0}".format(ticker)] = dtreal["T1 {0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS1)
										#print("sell 1")

									if pricess["price_{0}".format(ticker)]>= dtreal["T2{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T2{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS2)
										#print("sell 2")
									if pricess["price_{0}".format(ticker)]>= dtreal["T3{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T3{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS3)
										#print("sell 3")

									if pricess["price_{0}".format(ticker)]>= dtreal["T4{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T4{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS4)
										#print("sell 4")
									if pricess["price_{0}".format(ticker)]>= dtreal["T5{0}".format(ticker)] :
										dsell1["sell1{0}".format(ticker)] = dtreal["T5{0}".format(ticker)]
										
										dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS5)
										#print("sell 5")
										


							############## ORDER sell ###############


							if dbuy["B1 {0}".format(ticker)] == 1 :
								############# PRICE OF TRALING ###########
								if pricess["price_{0}".format(ticker)]>= dsell1["sell1{0}".format(ticker)] :
									if pricess["price_{0}".format(ticker)]> dtraling_list["traling_list{0}".format(ticker)][0] :
										del dtraling_list["traling_list{0}".format(ticker)][0]
										dtraling_list["traling_list{0}".format(ticker)].insert(0,pricess["price_{0}".format(ticker)])


								##########SELL######
								
								if pricess["price_{0}".format(ticker)]>= dtreal["T1 {0}".format(ticker)]:
									dsell1["sell1{0}".format(ticker)] = dtreal["T1 {0}".format(ticker)]
									
									dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS1)
									#print("sell 1")
								
								
								if pricess["price_{0}".format(ticker)]>= dtreal["T2{0}".format(ticker)] :
									dsell1["sell1{0}".format(ticker)] = dtreal["T2{0}".format(ticker)]
									
									dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS2)
									#print("sell 2")
								if pricess["price_{0}".format(ticker)]>= dtreal["T3{0}".format(ticker)] :
									dsell1["sell1{0}".format(ticker)] = dtreal["T3{0}".format(ticker)]
									
									dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS3)
									#print("sell 3")

								if pricess["price_{0}".format(ticker)]>= dtreal["T4{0}".format(ticker)] :
									dsell1["sell1{0}".format(ticker)] = dtreal["T4{0}".format(ticker)]
									
									dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS4)
									#print("sell 4")
								if pricess["price_{0}".format(ticker)]>= dtreal["T5{0}".format(ticker)] :
									dsell1["sell1{0}".format(ticker)] = dtreal["T5{0}".format(ticker)]
									
									dstop_traling["stop_traling{0}".format(ticker)] =dtraling_list["traling_list{0}".format(ticker)][0]+(dtraling_list["traling_list{0}".format(ticker)][0]*TS5)
									#print("sell 5")



								################## $$$$$$$  order sell  $$$$$$$ #################

								if dstop_traling["stop_traling{0}".format(ticker)] > 0 and ticker != "BTCUSDT" :		
									


									if dstop_traling["stop_traling{0}".format(ticker)] > 0 :		
										
										
										################## $$$$$$$  order sell  $$$$$$$ #################
										
										
										if pricess["price_{0}".format(ticker)]<= dstop_traling["stop_traling{0}".format(ticker)] : 
											
											qty = qtyD["qty_{0}".format(ticker)]
											minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
											qty = format_value(qty,minQty)
																						
											segnal_list = [{"ticker":ticker,"FROM":"VP","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

											SIGNALS = pd.DataFrame(segnal_list)
											SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")											
											

										
											try :
												

													#order = client.order_market_sell(symbol=ticker,quantity=qty)
													
													
													print("order sell MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													#print("qty = " , qty, "for api number =",se)
													print(" ================ loding...... =====================")

											except:
													try :
														#order = client.order_market_sell(symbol=ticker,quantity=qty)
														
														print("order sell MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])								
														#print("qty = " , qty, "for api number =",se)
														print(" ================ loding...... =====================")	
													except:
														
														print("Error sell",ticker)
														print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",ticker)


											
											
											



											
											
											dtraling_list["traling_list{0}".format(ticker)][0] = 0
											dsell1["sell1{0}".format(ticker)] = 0
											dstop_traling["stop_traling{0}".format(ticker)] = 0
											#print("price of sell", ticker, "=",pricess["price_{0}".format(ticker)])
											
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
												
												#now = datetime.datetime.now()
												#teak_time = now - tims_start["percent{0}".format(ticker)]
												resulting = "LOSE"
												if d["BUY1{0}".format(ticker)] > pricess["price_{0}".format(ticker)]:
													percent_diff = percent_diff-percent_diff-percent_diff
													resulting = "LOSE"
												if percent_diff > 0 :
													resulting = "profit"


												lostes["lostes{0}".format(ticker)]=0
												DF_.append({"tiker" :ticker ,"SELL_FROM":"TRALLING"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":percent_diff ,"resulting":resulting ,"ALL_ORDERS":ORDERS,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + percent_diff })
												DF= pd.DataFrame(DF_)
												SUM_PROFITS=sum(DF["percentage_%"])
												
												DF.to_csv("volum_profil_sefty.csv",index=False)
												DF.to_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\volum_profil_sefty.csv",index=False)
												
												files = {"document":open("volum_profil_sefty.csv")}
												#file_data =requests.post('https://api.telegram.org/bot1761051650:AAFw9h1XUWLd3b9F2jcyMljFZWf_GsoPWGg/sendDocument?chat_id=-565871494&caption=volum_profil_sefty',files=files)
												xl = {"tikers":ticker,"time":now}
												xllist.append(xl)
												dfx = pd.DataFrame(xllist)
												dfx.to_csv("x_coins.csv",index=False)
												df = pd .read_csv("x_coins.csv")
												xlist = df["tikers"].tolist()
												print("xlist ========",xlist) 											
												
												

											except:
												sssss= 0000
												print("erorr sell locatione")
											lostes["lostes{0}".format(ticker)]=0
											dbuy["B1 {0}".format(ticker)] = 6
											lostess["lostess_{0}".format(ticker)] = 0

																

									
							try:
								if dbuy["B1 {0}".format(ticker)] == 6:

												del N_tickers[i]
												lens = len(N_tickers)-1
												print("delete ",ticker)
												try:

													dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv" ,index_col=0)
													dfdata =dfdata.drop(index=ticker)
													dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")	

						
																				
												except:
													print("error data bais")						


																									

							except:
								mo = 1										
										


						

						i += 1





