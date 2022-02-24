import requests

import json


t = open('Param.txt', 'r', encoding='utf8')

TOKEN = t.readline()

t.close()


curr = {
    'рубль': 'RUB',
    'евро': 'EUR',
    'доллар': 'USD',
}


class ConvBotExp(Exception):
    pass


class CurrencyConvert:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base.lower() == quote.lower():
            raise ConvBotExp('Введены одинаковые валюты для пересчёта.')

        try:
            f_c = curr[base.lower()]
        except KeyError:
            raise ConvBotExp(f'Валюта {base} не найдена.')

        try:
            s_c = curr[quote.lower()]
        except KeyError:
            raise ConvBotExp(f'Валюта {quote} не найдена.')

        try:
            c_c = float(amount)
        except ValueError:
            raise ConvBotExp('Количество должно быть числом.')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={s_c}&tsyms={f_c}').content
        result = json.loads(r)[f_c]

        return result

#     Код ниже шёл для сайта, на котором по бесплатной подписке была доступен расчёт только с одной базовой валютой = EUR
#  и ответ включает не только валюту и её значение
# r_ = requests.get(
#         f'http://data.fixer.io/api/latest?access_key=b4742dec44bf912a21ed2b2484d3f9ef&symbols=USD&format=1').content
# result = json.loads(r_)['rates']['USD']