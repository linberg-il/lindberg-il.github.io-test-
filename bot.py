#-*-coding:utf-8-*-
import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler( commands=['start', 'help'] )
def welcome_mess(message):
    bot.send_message(message.chat.id, 'Welcome')
@bot.message_handler( regexp="test")
def test_message(message):
    bot.send_message(message.chat.id, 'Я блядь наглая блядь сука ленивая надо чтоб какая-нибудь сволочь пришла дала мне пинка блядь под жопу и сказала  «Жопу свою оторви блядь и поищи блядь работу потому что работа бывает у тех кому не лень блядь оторвать жопу и ее поискать». Вот что мне надо.	')
    pass
if __name__ == '__main__':
    bot.polling(none_stop = True)