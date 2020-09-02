#imports

in_file = "prices.txt"
sell_file = "worth.txt"
buy_file = "server-price.txt"

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
        ins = open(self.file, 'r')
        # loop through lines
        while True:
            line = ins.readline()
            # if at end of file stop the loop
            if not line:
                break
            # if line starts with # or is blank -> move on
            # else
            if line[0] != '#' and line[0] != '\n':
                #get name
                name, junk = line.split(':')
                line = ins.readline().strip()
                #get buy price
                junk, buy = line.split(': ')
                line = ins.readline().strip()
                #get sell price
                junk, sell = line.split(': ') 
                line = ins.readline().strip()
                #get quantity
                junk, qty = line.split(': ')
                #calculate individual prices
                buy_price = round(float(buy.replace(',','')) / float(qty), 2)
                sell_price = round(float(sell.replace(',','')) / float(qty), 2)
                #write to dictionary
                self.sell_prices[name] = sell_price
                self.buy_prices[name] = buy_price
        ins.close()

    #write sale prices
    def write_sell_prices(self):
        with open(sell_file, 'w') as out:
            for key in self.sell_prices:
                s = key + ': ' + str(self.sell_prices[key]) + '\n'
                out.write(s)
        out.close()

    #write buy prices
    def write_buy_prices(self):
        pass

if __name__=='__main__':
    pp = PriceParser(in_file)
    pp.read()
    pp.write_sell_prices()