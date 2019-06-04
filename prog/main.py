# общие библиотеки
# import datetime
# import sys

# библиотеки сообщества
from binance_api import Binance
from init import aaa as keyB

# мои библиотеки
# import bFunc


# исходные данные ----------------

# подключаемся к бирже
bn = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

lExchangeInfo = bn.exchangeInfo()
print(lExchangeInfo)
print(keyB)
