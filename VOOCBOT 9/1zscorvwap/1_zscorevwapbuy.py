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
xlist = ["USDT"]
N = []
SFTY_ORDER = {}
dbuyn ={}
lostess = {}
PROFITS = {}
DSTOPLOSING ={}
DSFITY_ORDER = {}
average_qty = {}
average_price = {}
print("ZSCORE_sefty WORKING")
timer
print(" ================ loding...... =====================")	
while True:

						if i > lens :
							i=0
						if i == 0 :

												
									try :
										datiker = pd.read_csv("NEW_COINS.csv")
										
										
										if not datiker["ticker"].empty:
											N = datiker["ticker"].tolist()
											NOW=returnNotMatches(N,N_tickers)									
										
											linsNOW = len(NOW)
											if lens <= 3 :
													
												if linsNOW > 0:
													for ticker in NOW :
														#print(" ================ loding tikers n ...... =====================")
														conn_key = bsm.start_symbol_ticker_socket(ticker, DOGE_trade_history)
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
											elif lens > 2:
													try:
														
														os.remove('NEW_COINS.csv')
													except:
														aaaa= 4442544
									except:
										aaaa= 1255
									try:
										
										datiker = pd.read_csv("NEW_COINS.csv")
										
										
										if not datiker["ticker"].empty:
											N = datiker["ticker"].tolist()
											
											for TICK in N_tickers:
												if N[0] == TICK :
													if dbuy["B1 {0}".format(TICK)] == 1 :
														if DSFITY_ORDER["sifty_order{0}".format(TICK)] != 2  :
															#time
															now = datetime.datetime.now()
															tacks_time = now - tims_start["percent{0}".format(TICK)]

															minutes = tacks_time.total_seconds() / 60 
															tacks_time = tacks_time.seconds / 60
															if tacks_time > timer :
																TT = -10/100
																SFTY_CHIK = d["BUY1{0}".format(TICK)]+(d["BUY1{0}".format(TICK)]*TT)
																if pricess["price_{0}".format(TICK)] < SFTY_CHIK:
																	print("$$$$$$$$$$$$$$$ sfty $$$$$$$$$$$$$$$$$$$$$$$")
																	print("SFTY_CHIK =",SFTY_CHIK)
																	print(d["BUY1{0}".format(TICK)])

																	dbuy["B1 {0}".format(TICK)] = 2
															try:
																
																os.remove('NEW_COINS.csv')
															except:
																aaaa= 4442544 
																				

										
										
									
									except:
										#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")	
										aaaaaaaa=1111111										
						if N_tickers != []:			
							lens = len(N_tickers)-1
							ticker = N_tickers[i]


						#### ORDER BUY AND SELL ##########		
						if pricess["price_{0}".format(ticker)]!= 0 and ticker != "BTCUSDT" :

							############## ORDER BUY 1 ###############
							if dbuy["B1 {0}".format(ticker)] == 0  and ticker != "BTCUSDT":	
									segnal_list = [{"ticker":ticker,"FROM":"ZC","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")										
									print("buy order",ticker)

																					
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									
									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)
									
									

									
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											now = datetime.datetime.now()
											print(now )
										
									except:
											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													now = datetime.datetime.now()
													print(now)
													
											except:
												
												
												print("Error buy Balance is not enough to buy",ticker)
												print("==============loding......")
												dbuy["B1 {0}".format(ticker)] = 6
												i += 1
												continue


											
																		
					
											

									
									
																						
									try:
											
							

										dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")
										BAS =returnNotMatches(N_tickers,dfdata["tickers"])
										print(BAS)
										for tcoine in BAS :
											
												
													DATABE = {"tickers":tcoine,"FROM":"ZC" , "qty" :qty , "price_of_buy":pricess["price_{0}".format(tcoine)] }
													dfdata =dfdata.append(DATABE,ignore_index=True)
													pd.set_option('chained',None)
													
													dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv",index=False)									

													print("data bais")

			
																	
									except:
										print("error data bais")

									dbuy["B1 {0}".format(ticker)] = 1
									qtyD["qty_{0}".format(ticker)] = qty

									tims_start["percent{0}".format(ticker)] = datetime.datetime.now()
									ORDERS += 1
									
									

									d["BUY1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]

									average_qty["average_qty1{0}".format(ticker)] = qty
									average_price["average_price1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
									
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

							if dbuy["B1 {0}".format(ticker)] == 2  and ticker != "BTCUSDT"	:	
								if DSFITY_ORDER["sifty_order{0}".format(ticker)] == 0 : 			
									segnal_list = [{"ticker":ticker,"FROM":"ZC","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")										
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									
									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)

									

									
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT sfty order 1  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											now = datetime.datetime.now()
											print(now )
										
									except:
											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													now = datetime.datetime.now()
													print(now)
													
											except:
												
												
												print("Error buy Balance is not enough to buy",ticker)
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
							if dbuy["B1 {0}".format(ticker)] == 2  and ticker != "BTCUSDT"	:	
								if DSFITY_ORDER["sifty_order{0}".format(ticker)] == 1 : 
									segnal_list = [{"ticker":ticker,"FROM":"ZC","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

									SIGNALS = pd.DataFrame(segnal_list)
									SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")													
									#buy order BUY MARKIT				
									#minPrice =  pairPriceinfo(ticker,len(info["ticker"])-1)
									#pricess["price_{0}".format(ticker)] = format_value(pricess["price_{0}".format(ticker)],minPrice)
									
									qty = USDT/pricess["price_{0}".format(ticker)]


									minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
									qty = format_value(qty,minQty)

									

									
									try :
										if  ticker != "BTCUSDT":
											#order = client.order_market_buy(symbol=ticker,quantity=qty)
											print(" ================ loding...... =====================")
											print("buy order BUY MARKIT sfty order 2 : ",ticker,"=",pricess["price_{0}".format(ticker)])									
											now = datetime.datetime.now()
											print(now  )
										
									except:
											try :
												if  ticker != "BTCUSDT":
													#order = client.order_market_buy(symbol=ticker,quantity=qty)
													print(" ================ loding...... =====================")
													print("buy order BUY MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													now = datetime.datetime.now()
													print(now)
													
											except:
												
												print("Error buy Balance is not enough to buy",ticker)
												print("==============loding......")
												dbuy["B1 {0}".format(ticker)] = 1
												i += 1
												continue


									
											
										
											

									
									
																						
	
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
									
									
									################## $$$$$$$  order sell  $$$$$$$ #################
									

														

									if dstop_traling["stop_traling{0}".format(ticker)] > 0 :		
										
										
										################## $$$$$$$  order sell  $$$$$$$ #################
										
										
										if pricess["price_{0}".format(ticker)]<= dstop_traling["stop_traling{0}".format(ticker)] : 
											segnal_list = [{"ticker":ticker,"FROM":"ZC","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

											SIGNALS = pd.DataFrame(segnal_list)
											SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")												
											
											qty = qtyD["qty_{0}".format(ticker)]
											minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
											qty = format_value(qty,minQty)

											

											try:
												

													#order = client.order_market_sell(symbol=ticker,quantity=qty)
													
													
													print("order sell MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])									
													#now = datetime.datetime.now()
													# print(now, "for api number =",se)
													print(" ================ loding...... =====================")

											except:
													try :
														#order = client.order_market_sell(symbol=ticker,quantity=qty)
														
														print("order sell MARKIT  : ",ticker,"=",pricess["price_{0}".format(ticker)])								
														#now = datetime.datetime.now()
														# print(now, "for api number =",se)
														print(" ================ loding...... =====================")	
													except:
														
														print("Error sell",ticker)


													
													
													
											


											if dsell1["sell1{0}".format(ticker)] == dtreal["T1 {0}".format(ticker)] :
												print("sell 1  = ",dstop_traling["stop_traling{0}".format(ticker)])
											
											if pricess["price_{0}".format(ticker)]> dtreal["T2{0}".format(ticker)] and pricess["price_{0}".format(ticker)]<dtraling_list["traling_list{0}".format(ticker)][0]:
												print("sell 2  = ",dstop_traling["stop_traling{0}".format(ticker)])
								
											if pricess["price_{0}".format(ticker)]> dtreal["T3{0}".format(ticker)] and pricess["price_{0}".format(ticker)]<dtraling_list["traling_list{0}".format(ticker)][0]:
												print("sell 3  = ",dstop_traling["stop_traling{0}".format(ticker)])
											
											if pricess["price_{0}".format(ticker)]> dtreal["T4{0}".format(ticker)] and pricess["price_{0}".format(ticker)]<dtraling_list["traling_list{0}".format(ticker)][0]:
												print("sell 4  = ",dstop_traling["stop_traling{0}".format(ticker)])
										
											if pricess["price_{0}".format(ticker)]> dtreal["T5{0}".format(ticker)] and pricess["price_{0}".format(ticker)]<dtraling_list["traling_list{0}".format(ticker)][0]:
												print("sell 5  = ",dstop_traling["stop_traling{0}".format(ticker)])
											
											
											
											
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
												
												DF.to_csv("ZSCORE_sefty.csv",index=False)
												DF.to_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\ZSCORE_sefty.csv")
												
										
												
												

											except:
												sssss= 0000
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





