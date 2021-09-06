import telegram

bot = telegram.Bot(':')

def sendmsg(msg):
        chat_id = 
        bot.send_message(chat_id, text=msg)
