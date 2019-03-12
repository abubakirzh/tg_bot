import telebot
import requests

TOKEN = "702434438:AAFr7vWf3TWQvTlSgHmKJtFMkURz27YQ_YE"
API = 'https://api.bitfinex.com/v1/pubticker/ethusd'
bot = telebot.TeleBot(TOKEN)

store_data = {}

@bot.message_handler(commands=['gotext'])
def hello(message):
    read_api_and_send_data(message)
    bot.send_message(message.chat.id, store_data)


@bot.message_handler(commands=['crypto'])
def read_api_and_send_data(message):
    read_data = requests.get(API).json()

    for key, value in read_data.items():
        store_data[key] = value


bot.polling()


    # store_data['Mid'] = read_data['mid']
    # bot.send_message(message.chat.id, "Mid: {}".format(read_data['mid']),
    #                     "Bid: {}".format(read_data['bid']),
    #                     "Ask: {}".format(read_data['ask']),
    #                     "Last Price: {}".format(read_data['last_price']),
    #                     "high: {}".format(read_data['timestamp']))
