from spyre import server
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd
from IPython.display import HTML
#import matplotlib.pyplot as plt


class Cryptoheaven(server.App):
    title = "Cryptoheaven "
    inputs = [{ "type":"dropdown",
                "key":"ticker",
                "label": "companies",
                "options": [
                     {"label": "Bitcoin USD(BTC/USD)", "value": "BTC"},
                     {"label": "Ethereum USD(ETH/USD)", "value": "ETH"},
                     {"label": "Ripple USD(XRP/USD)", "value": "XRP"}
             ],
                "action_id":"table_id"}]


    outputs = [{"type":"table",
                "id":"table_id",}]

    def getData(self, params):
        ticker = params['ticker']
        key = '' #insertkeyhere-for.ex-6CGJ8IWIR2UQ361H
        cc = CryptoCurrencies(key,output_format='pandas')
        df, meta = cc.get_digital_currency_daily(symbol=ticker,market='USD')

        #df= pd.read_csv('physical_currency_list.csv')
        return df



app = Cryptoheaven()
app.launch()
exit
