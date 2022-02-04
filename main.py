import telebot #pip install pyTelegramBotAPI
import configure #Token in another python file

client = telebot.TeleBot(configure.config['token'])

@client.message_handler(content_types =  ['text'])
def get_text(message):
    if message.text.lower() == 'hello':
        client.send_message(message.chat.id,'hello unknown user')
    elif message.text.lower() == 'how are you':
        client.send_message(message.chat.id,'I am okay,and you 😁')


client.polling(none_stop=True,interval=0)