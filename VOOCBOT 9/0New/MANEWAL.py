



import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import numpy as np 
import csv
import time
from pandas.core.frame import DataFrame
def returnNotMatches(a, b):
	a = set(a)
	b = set(b)
	return list(a - b)

N_tickers=[]


while True:
    print ("enter the ticker")
    ticker =str(input())
    print ("pric of ticer naw")
    prices =float(input())
    print("side   BUY  OR SELL")
    side = str(input())
    
    if side == "BUY":
        segnal_list = [{"ticker":ticker,"FROM":"VP","side":side,"price":prices}]

        SIGNALS = pd.DataFrame(segnal_list)
        SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")

        SIGNALS.to_csv("manual.csv")
        print("BUY ORDER FILD ",ticker)
        N_tickers.append(ticker)
       # try:
                

        
        dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")
        BAS =returnNotMatches(N_tickers,dfdata["tickers"])
        print(BAS)
        for tcoine in BAS :
            
                
                    DATABE = {"tickers":tcoine , "qty" :100 , "price_of_buy":prices }
                    dfdata =dfdata.append(DATABE,ignore_index=True)
                    pd.set_option('chained',None)
                    
                    dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv",index=False)									

                    print("data bais")


                                    
       # except:
           # print("error data bais")	
    if side == "SELL":

        segnal_list = [{"ticker":ticker,"FROM":"VP","side":side,"price":prices}]

        SIGNALS = pd.DataFrame(segnal_list)
        SIGNALS.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\SIGNALS.csv")

        SIGNALS.to_csv("manual.csv")
        print("BUY ORDER FILD ",ticker)


        dfdata = pd.read_csv (r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv" ,index_col=0)
        dfdata =dfdata.drop(index=ticker)
        dfdata.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\databas_vooc.csv")									

        print("data bais")


