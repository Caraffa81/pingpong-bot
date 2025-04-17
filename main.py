import requests
import datetime
import telegram

BOT_TOKEN = '8132622545:AAFrcm7_iG7PCCmkXOX3shisUIAotABnnHw'
CHAT_ID = '835674736'

now = datetime.datetime.now()
current_hour = now.hour

message = f"Ciao! Sono attivo! Ora attuale: {current_hour}:00"

bot = telegram.Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message)
