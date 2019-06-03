# общие библиотеки
# import datetime
# import sys

# библиотеки сообщества
from binance_api import Binance

# мои библиотеки
# import bFunc


# исходные данные ----------------

# подключаемся к бирже
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

lExchangeInfo = bot.exchangeInfo()
print(lExchangeInfo)