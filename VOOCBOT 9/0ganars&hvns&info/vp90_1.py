from market_profile import MarketProfile
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
import threading
import pyttsx3
engine = pyttsx3.init() 
from APISS import*
client = Client(api_key=Pkey, api_secret=Skey) 
def get_dist_plot(c, v, kx, ky):
			fig = go.Figure()
			fig.add_trace(go.Histogram(name='Vol Profile', x=c, y=v, nbinsx=150, 
									histfunc='sum', histnorm='probability density',
									marker_color='#B0C4DE'))
			fig.add_trace(go.Scatter(name='KDE', x=kx, y=ky, mode='lines', marker_color='#D2691E'))
			return fig




tickers = pd.read_csv("TICAR_GANERS.CSV")
tickers_1 = tickers["ticker"]


#tickers_1 = ["ADAUSDT"]		



ALL_DATA_list = []
DATA_BUY_list = []
#######################


qv_buy_list = []
qv_sell_list = []
v_buy_list = []
v_sell_list = []

HVNS = []

###########################

numr_of_ind = 0


for ticker in tickers_1 : 
    numr_of_ind += 1
    print(numr_of_ind ,ticker , "loding.....")
    
    #print(ALL_DATA_list)


    try:
        rawa = client.get_historical_klines(ticker , Client.KLINE_INTERVAL_1MINUTE,"90 day ago UTC")
        rawa = pd.DataFrame(rawa)
        #print(rawa)
        if not rawa.empty:
            rawa[0] =  pd.to_datetime(rawa[0],unit='ms')    
            rawa.columns = ['timestamp','Open','High','Low','Close','Volume','IGNORE','quoteVolume','SELLVolume','BUY_VOL','BUY_VOL_VAL','x']
            # convert to numbers 
            rawa ["Open"] = pd.to_numeric(rawa["Open"])
            rawa ["High"] = pd.to_numeric(rawa["High"])
            rawa ["Low"] = pd.to_numeric(rawa["Low"])
            rawa ["Close"] = pd.to_numeric(rawa["Close"])
            rawa ["Volume"] = round(pd.to_numeric(rawa["Volume"]))
            rawa ["quoteVolume"] = round(pd.to_numeric(rawa["quoteVolume"]))
            rawa ['IGNORE'] = pd.to_numeric(rawa['IGNORE'])
            rawa ['BUY_VOL'] = pd.to_numeric(rawa['BUY_VOL'])
            rawa ['BUY_VOL_VAL'] = pd.to_numeric(rawa['BUY_VOL_VAL'])

            rawa.loc[rawa.quoteVolume < 100, 'quoteVolume'] =100
        
            time_now = rawa ["timestamp"].iloc[-1]
            low = min(rawa ["Low"])
            #print(low)
            

            rawa.to_csv("ETHusdt1.csv",index= False)
            DF= pd.read_csv('ETHusdt1.csv')
            DF = DF[['Open', 'High', 'Low', 'Close', 'Volume',"quoteVolume"]]
            kde_factor = 0.05
            num_samples = 500
            kde = stats.gaussian_kde(DF["Close"],weights=DF["Volume"],bw_method=kde_factor)
            xr = np.linspace(DF["Close"].min(),DF["Close"].max(),num_samples)
            kdy = kde(xr)
            ticks_per_sample = (xr.max() - xr.min()) / num_samples
            peaks,_ = signal.find_peaks(kdy)
            pkx = xr[peaks]
            pky = kdy[peaks]
            pk_marker_args=dict(size=10)
            fig = get_dist_plot(DF["Close"], DF["Volume"], xr, kdy)
            fig.add_trace(go.Scatter(name="Peaks", x=pkx, y=pky, mode='markers', marker=pk_marker_args))#.show()

            ALLHVN = {"VOLIM" : pky ,"price": pkx}
            ALLHVN = pd.DataFrame(ALLHVN)
            x = pd.DataFrame(ALLHVN)
            #print(x)
            x.to_csv("high_vooc_1.csv",index= False)
            DFM= pd.read_csv('high_vooc_1.csv')
            dfvolum = DFM["VOLIM"]
            #print(dfvolum)
            linsall = len(DFM)-1
            line3 = int(linsall/3)
            line3dabell=line3+line3
            dfvolum_1 =dfvolum[:line3]
            dfvolum_2 =dfvolum[line3:line3dabell]
            dfvolum_3 = dfvolum[line3dabell:]
            maxs1=max(dfvolum_1)
            maxs2=max(dfvolum_2)
            maxs3=max(dfvolum_3)
            HVNS =[]
            i = 0
            while i <= linsall :
                    
                if len(DFM["VOLIM"]) > i:
                    
                        if maxs1 == DFM["VOLIM"][i] : 
                            HVNS.append(DFM["price"][i])
                            #print(HVNS)
                        if maxs2 == DFM["VOLIM"][i] : 
                            HVNS.append(DFM["price"][i])
                            #print(HVNS)
                        if maxs3 == DFM["VOLIM"][i] : 
                            HVNS.append(DFM["price"][i])
                            #print(HVNS)
                    
                i += 1


    
            print("HVN =" ,HVNS )
            
            
            ALL_DATA = {"coins": ticker,"HVN__1":HVNS[0],"HVN__2":HVNS[1],"HVN__3" : HVNS[2]}

            ALL_DATA_list.append(ALL_DATA)
            HVNS = []
            
        
    except :
            print("error")

###########################



try:
    ALL_DAT = pd.DataFrame(ALL_DATA_list)
    ALL_DAT.to_csv("VOLUM_PROFIL_90_DAYS.csv",index=False)


    ALL_DAT.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\VOOC BOT\VOLUM_PROFIL_90_DAYS.CSV",index=False)
    ALL_DAT.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\scalping\VOLUM_PROFIL_90_DAYS.CSV",index=False)
    ALL_DAT.to_csv(r"C:\Users\Administrator\Desktop\VOOCBOT 9\1volumprofilstratgy\VOLUM_PROFIL_90_DAYS.CSV",index=False)

except:
    aaaaaaaaaaaa= 0000000000000
    print ("ERROR sinding file")













