#!/usr/bin/env python3
import requests

class BrainStock:

    def __init__(self):
        self.api_key   = ''
        self.ticker    = ''
        self.daysUp    = 0
        self.daysDn    = 0

    def stockData(self):
        self.url       = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&apikey={self.api_key}'
        self.req       = requests.get(self.url)
        self.data      = self.req.json()["Time Series (Daily)"]
        self.open      = list(self.data.items())[0][1]["1. open"]
        self.high      = list(self.data.items())[0][1]["2. high"]
        self.low       = list(self.data.items())[0][1]["3. low"]
        self.close     = list(self.data.items())[0][1]["4. close"]
        self.prevclose = list(self.data.items())[1][1]["4. close"]
        self.change    = float(self.close) - float(self.prevclose)
        self.pctchange = self.change / float(self.prevclose) * 100

    def getSentiment(self):
        for day in range(0, 2):
            self.bias = float(list(self.data.items())[day][1]["4. close"]) - float(list(self.data.items())[day+1][1]["4. close"])
            if self.bias > 0:
                self.daysUp += 1
            elif self.bias < 0:
                self.daysDn += 1
        
        if self.daysUp > self.daysDn:
            self.sentiment = 'bullish'
        elif self.daysUp < self.daysDn:
            self.sentiment = 'bearish'
        else:
            self.sentiment = 'neutral'

    def getStrikePrices(self):
        self.callStrike = float(self.close) + (float(self.close) * 0.01618)
        self.putStrike  = float(self.close) - (float(self.close) * 0.01618)
