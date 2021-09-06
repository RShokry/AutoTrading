import binance.client 
from binance.client import Client

from telebot import sendmsg

import pandas as pd 
import numpy as np 
import csv
import time
from pandas.core.frame import DataFrame
import requests
import os
import datetime
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




def buy_bnb_fees(api,sek):					




			try:
				client =Client(api_key=api,api_secret=sek)
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
				if bnbusdt<=10:
						priceBNB =df.loc["BNBUSDT"]
						qtybnb = 20/priceBNB
						minQty =  pairQtyinfo("BNBUSDT",len(info["ticker"])-1)
						qtybnb = format_value(qtybnb,minQty)
						try:
							order = client.order_market_buy(symbol="BNBUSDT",quantity=qtybnb)
							print('BNB Order is done')
						except:
							print("Balance_BNB is not enough to buy BNB for fees",se)
			except:
				print("error bnb")
			



def timeselver(se,api,sek):
	try:
		df = pd.read_csv("APIS_1000.CSV")
		client =Client(api_key=api,api_secret=sek)
	
		time_res = client.get_server_time()
		time_res = [time_res]
		time_res = pd.DataFrame(time_res)

		time_res["serverTime"][0] =  pd.to_datetime(time_res["serverTime"][0],unit='ms') 
		time_1 = time_res["serverTime"][0] 
		time_1 = time_1.date()
		

		startdate = datetime.datetime.strptime(df["starttime"][se], "%Y-%m-%d").date()
		print(startdate)
		if (time_1 - startdate).days < df["endtime"][se]:
			
			
			return True
		else:
			print('sub end')
			return False
		
	except:
		time.sleep(1)
		try:
			client =Client(api_key=api,api_secret=sek)
		
			time_res = client.get_server_time()
			time_res = [time_res]
			time_res = pd.DataFrame(time_res)

			time_res["serverTime"][0] =  pd.to_datetime(time_res["serverTime"][0],unit='ms') 
			time_1 = time_res["serverTime"][0] 
			time_1 = time_1.date()
			print(time_1)

			#time_1 = datetime.datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S.%f").date()
			#print(time_1)
			startdate = datetime.datetime.strptime(df["starttime"][se], "%Y-%m-%d").date()
			print(startdate)
			if (time_1 - startdate).days <= df["endtime"][se]:
				
				print('buy')
				return True
			else:
				print('sub end')
				return False
			
		except:
			print("error time f")
			return False




qtysumall ={}
qtyD={}

pricess={}


DATABAIS = []

side = 0
while True:
		try:
			df_signal=pd.read_csv("SIGNALS.csv")
			ticker =df_signal["ticker"][0]
			side =df_signal["side"][0] 
			price =df_signal["price"][0]
			pricess["price_{0}".format(ticker)] = price
			FROM = df_signal["FROM"][0]
			

			try:
			
				os.remove('SIGNALS.csv')
			except:
				aaaa= 4442544
		
		except:
			aa= 1111
		#("   api  1000  ") 
		if side == "BUY":
			print("$$$$$$$$$$$$$$$$ $    api 1000  $$$$$$$$$$$$")
			
			DF_API = pd.read_csv("APIS_1000.CSV")
			
			Pkey =DF_API["Pkey"]
			Skey =DF_API["Skey"]

			
		
	



			se = 0
			for api in Pkey :
					sek= Skey[se]

					USDT = DF_API["CAPITAL_MANGAGEMENT"][se]
					qty = USDT/price
					minQty =  pairQtyinfo(ticker,len(info["ticker"])-1)
					qty = format_value(qty,minQty)
					
					

					try:
						client =Client(api_key=api,api_secret=sek)
					except:
						print("no api" )
						se += 1
						continue

					supscrip =timeselver(se,api,sek)
					if supscrip :
						try:
							print(" ================BUY" , ticker ," loding...... =====================")

							order = client.order_market_buy(symbol=ticker,quantity=qty)
							try :
								if qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] !=0 :
									qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] + qty
								if qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] == 0 :
									qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qty

							except:

								qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qty
								print("qty ok")


							DATA = [qtyD]


							try :
								if qtysumall["qty_{0}{1}".format(se,ticker)] !=0 :
									qtysumall["qty_{0}{1}".format(se,ticker)] = qtysumall["qty_{0}{1}".format(se,ticker)] + qty
								if qtysumall["qty_{0}{1}".format(se,ticker)] == 0 :
									qtysumall["qty_{0}{1}".format(se,ticker)] = qty

							except:

								qtysumall["qty_{0}{1}".format(se,ticker)] = qty


							DATAsum = [qtysumall]



							
							print("buy order BUY MARKIT  : ",ticker,"=",price,"qty = " , qty  , "for api number =",se)									
							
						except:
							print(" traying agane to buy ")
										#buy bnb all apis

							
							buy_bnb_fees(api,sek)
														
							try:
								
								order = client.order_market_buy(symbol=ticker,quantity=qty)
								try :
									if qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] !=0 :
										qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] + qty
									if qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] == 0 :
										qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qty

								except:

									qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] = qty
								DATA = [qtyD]
								try :
									if qtysumall["qty_{0}{1}".format(se,ticker)] !=0 :
										qtysumall["qty_{0}{1}".format(se,ticker)] = qtysumall["qty_{0}{1}".format(se,ticker)] + qty
									if qtysumall["qty_{0}{1}".format(se,ticker)] == 0 :
										qtysumall["qty_{0}{1}".format(se,ticker)] = qty

								except:

									qtysumall["qty_{0}{1}".format(se,ticker)] = qty


								DATAsum = [qtysumall]								
								print("buy order BUY MARKIT  : ",ticker,"=",price,"qty = " , qty  , "for api number =",se)									
								
							except:
								print(" error buy ")		
							

					se += 1
			try:		
				DFDATA= pd.DataFrame(DATA)
				DFDATA.to_csv("zdata.csv")
				DFDATAsum= pd.DataFrame(DATAsum)
				DFDATAsum.to_csv("shadawindata.csv")			

				sendmsg(" {} تم شراء \n متوسط سعر  = {} \n ".format(ticker,price))
			except:
				print(os.error)

			
		if side == "SELL":
			print("============ sell" , ticker ," loding...... =====================")
			try:
				DF_API = pd.read_csv("APIS_1000.CSV")
				USDT = DF_API["CAPITAL_MANGAGEMENT"][0]
				Pkey =DF_API["Pkey"]
				Skey =DF_API["Skey"]			
				
				DF_DATABAIS = pd.read_csv("zdata.CSV")
				DF_DATABAISshdawin = pd.read_csv("shadawindata.csv")

			except:
				print("erorr red fills 314")


			se = 0
			for api in Pkey :
					
					
					sek= Skey[se]

					try:
						client =Client(api_key=api,api_secret=sek)
					except:
						print("no api" )
						se += 1
						continue

					
					try :
						print(" ================   sell loding...... =====================")
						
						try:

							qty =DF_DATABAIS["qty_{0}{1}{2}".format(se,ticker,FROM)][0]
						except:
							print ("error qty vp or zc")
						try:	
							order = client.order_market_sell(symbol=ticker,quantity=qty)
							print("order SELL MARKIT  : ",ticker,"=",price,"qty = " , qty  , "for api number =",se)	
						except:
							print ("error order sell")						
						try:								
							qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] =0
							DATA = [qtyD]
							pd.set_option('chained',None)
							DF_DATABAISshdawin["qty_{0}{1}".format(se,ticker)][0]=DF_DATABAISshdawin["qty_{0}{1}".format(se,ticker)][0]-qty
						except:
							print ("error ad update qty")					
					except:
					
						print(" traying agane to sell ")
						#buy bnb all apis

						buy_bnb_fees(api,sek)

						try :
							
							qty =DF_DATABAIS[qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)]]
							order = client.order_market_sell(symbol=ticker,quantity=qty)
							
							print("order SELL MARKIT  : ",ticker,"=",price,"qty = " , qty  , "for api number =",se)									
							qtyD["qty_{0}{1}{2}".format(se,ticker,FROM)] =0
							DATA = [qtyD]
							pd.set_option('chained',None)
							DF_DATABAISshdawin["qty_{0}{1}".format(se,ticker)][0]=DF_DATABAISshdawin["qty_{0}{1}".format(se,ticker)][0]-qty								
						except:
							print("error sell for api 1000 number =",se)




					se += 1		
			try:
				DFDATA= pd.DataFrame(DATA)
				DFDATA.to_csv("zdata.csv")
				DF_DATABAISshdawin.to_csv("shadawindata.csv")



				sendmsg(" {} تم البيع  \n متوسط سعر  = {} \n ".format(ticker,price))

			except:
				print("eror data base")
		
		side = 0

