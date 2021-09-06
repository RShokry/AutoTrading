

import imaplib
import email
from os import error
import os 
import sys
import  pandas as pd
import time
from A__APISS import*
host = 'imap.gmail.com'
username = username 
password =  password
mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
ee = 0
print("ATR inbox WORKING")
my_inbox = []

def get_inbox():
    try :

        mail.select("inbox")
        _, search_data = mail.search(None, 'UNSEEN')
        my_message = []
        for num in search_data[0].split():
            email_data = {}
            _, data = mail.fetch(num, '(RFC822)')
            # print(data[0])
            _, b = data[0]
            email_message = email.message_from_bytes(b)
            for header in ['subject', 'to', 'from', 'date']:

                #print("{}: {}".format(header, email_message[header]))
                email_data[header] = email_message[header]
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    try:
                        body = part.get_payload(decode=True)
                        email_data['body'] = body.decode()
                    except:
                        print("error red")
                elif part.get_content_type() == "text/html":
                    try:
                        html_body = part.get_payload(decode=True)
                        email_data['html_body'] = html_body.decode()

                    except:
                        print("error red")
            my_message.append(email_data)
        return my_message
    except:
        print("error")
        os.system("B__Email_inbox_alerts.py")


while True:


    try:
        if __name__ == "__main__":
            
            
            my_inbox = get_inbox()
            #print(my_inbox)
            
            if my_inbox != [] :
                
                inpox = pd.DataFrame(my_inbox)
                inpox.to_csv("inpox.csv")

                if "TradingView" in inpox["from"][0] :
                    
                    myString = str(inpox["subject"][0])
                    print(myString)
                    if "Alert" in myString:

                        A = myString.replace('Alert: ','')
                        A = A.replace('ALERT :','') 
                        side =A[-1:]
                        ticr = A.replace(side,'') 
                        print("=======LODING.......")
                        coind = [{"ticker":ticr,"side":side}]
                        
                        dfcoin = pd.DataFrame(coind)
                        dfcoin.to_csv("C__alertes.csv",index=False)
                        #,index=False
                        

        
    except:
        print(error)
        os.system("B__Email_inbox_alerts.py")