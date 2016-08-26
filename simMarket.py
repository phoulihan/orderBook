#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:08:20 2016

@author: Patrick Houlihan
"""

import random
import datetime
from datetime import datetime
from googlefinance import getQuotes
from yahoo_finance import Share

#get times in ms for now, mktopen and mktclose
def getTimes():
    timestamp = datetime.now()
    now = (timestamp - timestamp.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    mktOpen = datetime.strptime('09:30:00.000000', '%H:%M:%S.%f')
    mktOpen = (mktOpen - mktOpen.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    mktClose = datetime.strptime('16:00:00.000000', '%H:%M:%S.%f')
    mktClose = (mktClose - mktClose.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return {'now': now, 'mktOpen': mktOpen, 'mktClose': mktClose}
    
#simulate random order type
def orderPacket(ticker,percRange):
    theOrder = {}   
    orderId = int(random.uniform(1,100))
    
    theData = fetchPrice(ticker)
    price = theData['price']
    timestamp= theData['timestamp']
    
    orderType = random.choice(["R" ,"A"])
    side = random.choice(["B", "S"])
    size = int(random.uniform(1,1000))

    if (orderType == "A"): #sell order
        theOrder = {'timestamp': timestamp, 'type': orderType, 'orderId' : orderId, 'side': side, 'price': price, 'size': size}
    else: 
        theOrder = {'timestamp': timestamp, 'type': orderType, 'orderId' : orderId, 'size': size}
    
    return theOrder

def fetchPrice(ticker):
    quoteData = getQuotes(ticker)
        
    theTimes = getTimes() 
    timestamp = theTimes['now']
    mktOpen = theTimes['mktOpen']
    mktClose = theTimes['mktClose']
    
    if (timestamp < mktOpen):
        price = float(after_hours.pre_latest(ticker)[1])
    elif (timestamp >= mktOpen and timestamp <= mktClose):
        price = float(quoteData[0]["LastTradePrice"])
    else:
        price = float(after_hours.ah_latest(ticker)[1])
    
    outData = {'price': price,'timestamp': timestamp}   
    
    return outData

def orderBookGenerator(ticker):
    a = 1
    

#def action(orderType()):
#    if orderType() == "Buy":
#        a = 1
    

        