import os
import telebot


bot = telebot.TeleBot("5734044165:AAFb9JIBuO4aFPadvZMm4ArucY9bgZD3o1g")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I am ChargSPOT007. Wellcome To the ChargSPOT SriLanla")


@bot.message_handler(commands=["How Register ChargSpot Flatform"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.chargespotsa.com/#/reg?inviteCode=848806")



bot.polling()
