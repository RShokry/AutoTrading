import telegram

bot = telegram.Bot('1761051650:AAFw9h1XUWLd3b9F2jcyMljFZWf_GsoPWGg')

def sendmsg(msg):
        chat_id = -1001508640971
        bot.send_message(chat_id, text=msg)
