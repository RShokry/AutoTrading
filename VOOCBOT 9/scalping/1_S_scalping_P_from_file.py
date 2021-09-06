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
from prises import*
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

df = pd.read_csv("VOLUM_PROFIL_90_DAYS.csv")


list_data = []
d ={}
ORDERS_ENded =0
SUM_PROFITS = 0
DF_ =[]
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print()
print("SCALPING")
def A():
	while True:
			df = pd.read_csv("VOLUM_PROFIL_90_DAYS.csv")
				
			A = 0

			for ticker in df["coins"][:50]:               
								if pricess["price_{0}".format(ticker)]!= 0 and ticker != "EURUSDT" :
									TECARS = pd.read_csv("manuall.csv")
									
									for i in TECARS["tickers"] :
										if ticker == i:
											print("===== def A     loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])

											UP = 1/100
											DOWN = -3/100
											OR_1_up = df["HVN__1"][A]+(df["HVN__1"][A]*UP)
											OR_1_dow =df["HVN__1"][A]+(df["HVN__1"][A]*DOWN)

											OR_2_up = df["HVN__2"][A]+(df["HVN__2"][A]*UP)
											OR_2_dow =df["HVN__2"][A]+(df["HVN__2"][A]*DOWN)

											OR_3_up = df["HVN__3"][A]+(df["HVN__3"][A]*UP)
											OR_3_dow =df["HVN__3"][A]+(df["HVN__3"][A]*DOWN)

											
											if pricess["price_{0}".format(ticker)] >= OR_1_dow and pricess["price_{0}".format(ticker)] <= OR_1_up :


												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")										
												SIGNALS.to_csv("SIGNALS.csv")
												d["BUY1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
												
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														print("YOU CAN SELL ", ticker)
														ORDERS_ENded +=1
														DF_.append({"tiker" :ticker ,"SELL_FROM":"SCALPING"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":2 ,"resulting":"profit" ,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + 2 })
														DF= pd.DataFrame(DF_)
														SUM_PROFITS=sum(DF["percentage_%"])
														DF.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\Scalping.csv")
														break	
										
											if pricess["price_{0}".format(ticker)] >= OR_2_dow and pricess["price_{0}".format(ticker)] <= OR_2_up :

												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
												SIGNALS.to_csv("SIGNALS.csv")
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														print("YOU CAN SELL ", ticker)
														ORDERS_ENded +=1
														DF_.append({"tiker" :ticker ,"SELL_FROM":"SCALPING"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":2 ,"resulting":"profit" ,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + 2 })
														DF= pd.DataFrame(DF_)
														SUM_PROFITS=sum(DF["percentage_%"])
														DF.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\Scalping.csv")
														break	




											if pricess["price_{0}".format(ticker)] >= OR_3_dow and pricess["price_{0}".format(ticker)] <= OR_3_up :


												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
												SIGNALS.to_csv("SIGNALS.csv")
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														print("you can sell",ticker)
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														break	

											
						

								A += 1
def B():
	while True:
			df = pd.read_csv("VOLUM_PROFIL_90_DAYS.csv")
				
			A = 0

			for ticker in df["coins"][50:]:               
								if pricess["price_{0}".format(ticker)]!= 0 and ticker != "EURUSDT" :
									TECARS = pd.read_csv("manuall.csv")
									
									for i in TECARS["tickers"] :
										if ticker == i:
											print("=====  def B  loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])

											UP = 1/100
											DOWN = -3/100
											OR_1_up = df["HVN__1"][A]+(df["HVN__1"][A]*UP)
											OR_1_dow =df["HVN__1"][A]+(df["HVN__1"][A]*DOWN)

											OR_2_up = df["HVN__2"][A]+(df["HVN__2"][A]*UP)
											OR_2_dow =df["HVN__2"][A]+(df["HVN__2"][A]*DOWN)

											OR_3_up = df["HVN__3"][A]+(df["HVN__3"][A]*UP)
											OR_3_dow =df["HVN__3"][A]+(df["HVN__3"][A]*DOWN)

											
											if pricess["price_{0}".format(ticker)] >= OR_1_dow and pricess["price_{0}".format(ticker)] <= OR_1_up :


												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")										
												SIGNALS.to_csv("SIGNALS.csv")
												d["BUY1{0}".format(ticker)] = pricess["price_{0}".format(ticker)]
												
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														print("YOU CAN SELL ", ticker)
														ORDERS_ENded +=1
														DF_.append({"tiker" :ticker ,"SELL_FROM":"SCALPING"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":2 ,"resulting":"profit" ,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + 2 })
														DF= pd.DataFrame(DF_)
														SUM_PROFITS=sum(DF["percentage_%"])
														DF.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\Scalping.csv")
														break	
										
											if pricess["price_{0}".format(ticker)] >= OR_2_dow and pricess["price_{0}".format(ticker)] <= OR_2_up :

												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
												SIGNALS.to_csv("SIGNALS.csv")
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														print("YOU CAN SELL ", ticker)
														ORDERS_ENded +=1
														DF_.append({"tiker" :ticker ,"SELL_FROM":"SCALPING"  ,"buy_price":d["BUY1{0}".format(ticker)],"seLL_pric":pricess["price_{0}".format(ticker)],"percentage_%":2 ,"resulting":"profit" ,"ORDERS_ENded":ORDERS_ENded,"ALL_PROFITS" : SUM_PROFITS + 2 })
														DF= pd.DataFrame(DF_)
														SUM_PROFITS=sum(DF["percentage_%"])
														DF.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\Scalping.csv")
														break	




											if pricess["price_{0}".format(ticker)] >= OR_3_dow and pricess["price_{0}".format(ticker)] <= OR_3_up :


												segnal_list = [{"ticker":ticker,"FROM":"SK","side":"BUY","price":pricess["price_{0}".format(ticker)]}]

												SIGNALS = pd.DataFrame(segnal_list)
												SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
												SIGNALS.to_csv("SIGNALS.csv")
												print("YOU CAN BUY ", ticker)
												UPT = 2/100
												UPTO = pricess["price_{0}".format(ticker)] +(pricess["price_{0}".format(ticker)]*UPT)
												while True :
													##print("=====loding.......",ticker ," = " ,pricess["price_{0}".format(ticker)])
													if pricess["price_{0}".format(ticker)] > UPTO :
														print("you can sell",ticker)
														segnal_list = [{"ticker":ticker,"FROM":"SK","side":"SELL","price":pricess["price_{0}".format(ticker)]}]

														SIGNALS = pd.DataFrame(segnal_list)
														SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")	
														break	

											
						

								A += 1

threading.Thread(target=A ).start()
threading.Thread(target=B ).start()