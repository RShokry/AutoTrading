

Pkey = ""
Skey = ""
import binance.client 
from binance.client import Client
from numpy.lib.function_base import average 
import pandas as pd 
import numpy as np
from scipy import stats, signal
import plotly.express as px
import plotly.graph_objects as go
import time
import requests
import datetime
import os
import requests
import pyttsx3
engine = pyttsx3.init() 
rate = engine.getProperty('rate')   
print() 
print(" Welcome to my program")    
print() 
print(" my name is RAMY SHOKRY ")                      
engine.setProperty('rate', 130)
engine.say("hi sur")
D = "Welcome to my program "
b = "my name is RAAMY SHOKREY "
a = " you can Follow me oon telygram  SMART TREAD "
aa = [D,b,a]
engine.say(aa )
engine.runAndWait()
engine.stop()

client = Client(api_key=Pkey, api_secret=Skey) 
def get_dist_plot(c, v, kx, ky):
			fig = go.Figure()
            
			fig.add_trace(go.Histogram(name='Volum Profile', x=c, y=v, nbinsx=150, 
									histfunc='sum', histnorm='probability density',
									marker_color='#B0C4DE'))
			fig.add_trace(go.Scatter(name='KDE', x=kx, y=ky, mode='lines', marker_color='#D2691E'))
            
            
                        
                        
                       
                        
                        
              

			return fig

print()
print("you can follow me on telegram  SMART TRADE ") 
print()
print("https://t.me/joinchat/o1g4s1Oq4oA0MjJk")
print() 
while True :


        def oto_volim():
                try:
                    print("Enter the coin name in capital letter :")
                    engine.say("enter your coin in capital letters" )
                    engine.runAndWait()
                    engine.stop()
                    ticker = input()
                    print("How many days of data you want to see in Volume profile ?")
                    engine.say("enter how many day VOOLUM PROFIL you want")
                    engine.runAndWait()
                    engine.stop()
                    day1 = input()
                    print("Please Wait ..")
                    engine.say("Please Wait")
                    engine.say("LODING")
                    engine.runAndWait()
                    engine.stop()                    
                    print("=======  LODING......")
                    day = ("{} day ago UTC").format(day1)               
                    rawa2 = client.get_historical_klines(ticker , Client.KLINE_INTERVAL_1MINUTE,day)
                    rawa2 = pd.DataFrame(rawa2)
                
                    if not rawa2.empty:
                        rawa2[0] =  pd.to_datetime(rawa2[0],unit='ms')    
                        rawa2.columns = ['timestamp','Open','High','Low','Close','Volume','IGNORE','quoteVolume','SELLVolume','BUY_VOL','BUY_VOL_VAL','x']
                        rawa2 ["Open"] = pd.to_numeric(rawa2["Open"])
                        rawa2 ["High"] = pd.to_numeric(rawa2["High"])
                        rawa2 ["Low"] = pd.to_numeric(rawa2["Low"])
                        rawa2 ["Close"] = pd.to_numeric(rawa2["Close"])
                        rawa2 ["Volume"] = round(pd.to_numeric(rawa2["Volume"]))
                        rawa2 ["quoteVolume"] = round(pd.to_numeric(rawa2["quoteVolume"]))
                        rawa2 ['IGNORE'] = pd.to_numeric(rawa2['IGNORE'])
                        rawa2 ['BUY_VOL'] = pd.to_numeric(rawa2['BUY_VOL'])
                        rawa2 ['BUY_VOL_VAL'] = pd.to_numeric(rawa2['BUY_VOL_VAL'])
                        rawa2.loc[rawa2.quoteVolume < 100, 'quoteVolume'] =100
                                
                    rawa2 = rawa2[['Open', 'High', 'Low', 'Close', 'Volume',"quoteVolume"]]
                    kde_factor = 0.05
                    num_samples = 500
                    kde = stats.gaussian_kde(rawa2["Close"],weights=rawa2["Volume"],bw_method=kde_factor)
                    xr = np.linspace(rawa2["Close"].min(),rawa2["Close"].max(),num_samples)
                    kdy = kde(xr)
                    ticks_per_sample = (xr.max() - xr.min()) / num_samples
                    peaks,_ = signal.find_peaks(kdy)
                    pkx = xr[peaks]
                    pky = kdy[peaks]
                    pk_marker_args=dict(size=10)
                    fig = get_dist_plot(rawa2["Close"], rawa2["Volume"], xr, kdy)
                    fig.update_layout( title_text="SMART TRADE   RAMY SOKRY")
                    fig.add_trace(go.Scatter(name="HVN", x=pkx, y=pky, mode='markers', marker=pk_marker_args)).show()
                    rawa2M = {"VOLIM" : pky ,"price": pkx}
                    rawa2M = pd.DataFrame(rawa2M)       
                    x2 = pd.DataFrame(rawa2M)
                    lins2 = len(rawa2M)-1   
                    maxall7 = max(rawa2M["VOLIM"])
                except:
                    print("error")
                    print("enter your coine in capital letters")
                    print("Example :  BTCUSDT")                    
                    engine.say("enter your coine in capital letters")
                    engine.say("Example :  B T C U S D T")
                    engine.say("try again")
                    engine.runAndWait()
                    engine.stop()



                try:
                    i = 0
                    while i <= lins2 : 
                        if len(rawa2M["VOLIM"]) > i:
                    
                            if maxall7 == rawa2M["VOLIM"][i] : 
                                maxallhvn7 = rawa2M["price"][i]

                                print("point of control = ",maxallhvn7)
                                
                        i += 1
                except :
                    print("error")

        
        oto_volim()           
