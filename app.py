import telebot

from extensions import CurrencyConvert, ConvBotExp, TOKEN, curr

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help_com(message: telebot.types.Message):
    privet = 'Бот пересчитывает валюты по курсу. \n \
Введите <Изначальную валюту>\
<Валюту для пересчёта>\
<Сумму изначальной валюты> \n \
Список доступных валют по команде \n \
values'
    bot.reply_to(message, privet)


@bot.message_handler(commands=['values'])
def start_help_com(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for cur in curr.keys():
        text = '\n'.join((text, cur,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvBotExp('Параметров должно быть 3.')

        base, quote, amount = values

        result = CurrencyConvert.get_price(base, quote, amount)

    except ConvBotExp as fail:
        bot.reply_to(message, f'Ошибка пользователя. \n{fail}')

    except Exception as fail_:
        bot.reply_to(message, f'Не удалось обработать команду. \n{fail_}')

    else:
        total_ = float(amount)*float(result)
        text = f'{amount} {quote} равно {total_} {base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
