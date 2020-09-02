#imports
import os

#class
class PriceParser:

    #constructor
    def __init__(self, file):
        self.file = file
        self.sell_prices = dict()
        self.buy_prices = dict()

    #read input from txt file
    def read(self):
        # open file
            # if line starts with # or is blank -> move on
            # else
                #get name
                #get buy price
                #get sell price
                #get quantity
                #calculate individual prices
        pass

    #write sale prices
    def write_sell_prices(self):
        # make dictionary of item names and sell prices
        # write dictionary
        pass

    #write buy prices
    def write_buy_prices(self):
        pass