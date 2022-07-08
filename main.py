from datetime import datetime
import telebot
from parse import get_last_news
from servise import custom_crono
import time
from decouple import config


token = config("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def commands(message):
    
    if message.text == "/start":
        
        while True:
            post = get_last_news()
            
            if post != None:
                
                for i in post:
                    bot.send_message(message.from_user.id, i)
                    
            time.sleep(86400)
            

bot.polling()