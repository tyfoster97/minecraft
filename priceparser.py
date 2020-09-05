#imports

price_file = "data/prices.yml"
#item_file = "data/sellable.txt"
sell_file = "worth.yml"
buy_file = "server-prices.yml"

# Tracks a Minecraft item and prices for the item
class Item:
    #Constructor
    def __init__(self, name, sell=0, qty=1):
        self.f = False #edited boolean flag
        self.n = name
        self.sp = sell / qty #user sell price per 1
        self.q = qty
    # gets name for worth.yml
    # None -> str
    def name(self):
        return self.n.replace('_','') #plugin compatibility
    def getbp(self):
        return round(self.sp * 0.4, 2)
    def getf(self):
        return self.f
    # gets name for prices.yml
    # None -> str
    def getn(self):
        return self.n
    def getsp(self):
        return round(self.sp, 2)
    def print(self):
        print(self.n)
        print('  sp: ' + str(self.sp))
        print('  bp: ' + str(self.getbp()))
    def setsp(self, price, qty=1):
        self.sp = price / qty
        self.bp = price * 0.4 / qty
        self.qty = qty
        self.f = True #flag as edited


#class
class PriceParser:

    #constructor
    def __init__(self, file):
        self.f = file
        self.e = False # flag for if db is edited
        self.idb = dict() # hash table of items

    def interact(self):
        cmd = '/'
        while cmd != 'exit':
            cmd = input('/')
            c = cmd.split(' ')
            if c[0] == 'sp':
                n = c[1]
                sp = float(c[2])
                if c[1] in self.idb:
                    self.idb[n].setsp(sp)
                    self.e = True
                else:
                    print('Invalid key')
            elif c[0] == 'get':
                if c[1] in self.idb:
                    i = self.idb[c[1]]
                    i.print()
                else:
                    print(c[1] + ' not found')
            elif c[0] == 'add':
                i = Item(c[1])
                i.setsp(float(c[2]))
                self.e = True
                self.idb[c[1]] = i
            elif c[0] == 'del':
                if input('del ' + c[1] + ' y/n?') == 'y':
                    del self.idb[c[1]]
            elif c[0] == 'cal':
                p = 0
                i = 1
                while i < len(c):
                    if c[i] in self.idb:
                        p += self.idb[c[i]].getsp() * float(c[i+1])
                        i += 2
                    else:
                        print('  no info for: ' + c[i])
                        break
                print('price: '+ str(p))
            elif c[0] == 'save':
                self.write_prices()
                self.write_worth()

    #read input from txt file
    def read(self):
        # open file
        items = open(self.f, 'r')
        # loop through lines
        while True:
            item = items.readline()
            # if at end of file stop the loop
            if not item:
                break
            # if line starts with # or is blank -> move on
            # else
            if item[0] != '#' and item[0] != '\n':
                #get name
                n, junk = item.split(':')
                item = items.readline().strip()
                #get buy price
                junk, buy = item.split(': ')
                item = items.readline().strip()
                #get quantity
                junk, qty = item.split(': ')
                #calculate individual prices
                sp = float(buy.replace(',',''))
                #write to dictionary
                self.idb[n] = Item(n, sp, float(qty))
        items.close()

    def write_prices(self):
        if self.e:
            with open(self.f, 'w') as items:
                for name in self.idb:
                    items.write(name + ':\n')
                    i = self.idb[name]
                    items.write('    buyPrice: ' + str(i.getsp()) + '\n')
                    items.write('    quantity: 1.0\n')
            items.close()
    
    #write sale prices
    def write_worth(self):
        if self.e:
            with open(sell_file, 'w') as out:
                out.write('worth: \n')
                for name in self.idb:
                    i = self.idb[name]
                    s = '    ' + i.name() + ': ' + str(i.getbp()) + '\n'
                    out.write(s)
            out.close()

if __name__=='__main__':
    pp = PriceParser(price_file)
    pp.read()
    pp.interact() # use database
    pp.write_prices() # save on exit
    pp.write_worth()