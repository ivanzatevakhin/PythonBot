import telebot
from proverb import proverb
from proverb import wether

bot = telebot.TeleBot('', parse_mode=None)


# Функция, обрабатывающая команды
@bot.message_handler(commands=['start', 'help', 'proverb', 'wether'])
def start(message):
    print(message.text)
    if message.text == '/help':
        bot.reply_to(message, ' /proverb - посылание \n /help - помоги себе сам \n /wether - Прогноз погоды')
    elif message.text == '/proverb':
        bot.send_message(message.chat.id, proverb())
    elif message.text == '/wether' + ' ':
        bot.send_message(message.chat.id, wether('Борисоглебск'))
    else:
        bot.send_message(message.chat.id, 'Неправильная команда - нахуй иди \n /help - помощь')


# Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#    if message.text == '/proverb':
#        bot.send_message(message.chat.id, proverb())
#

# Запускаем бота
bot.infinity_polling()
