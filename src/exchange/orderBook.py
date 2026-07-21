from collections import defaultdict, deque
from order import order

class orderBook:
    """Represents all orders currently awaiting a match, used by the matching engine."""
    def __init__(self):
        """Intialise the book, by creating two seperate dictionaries to store bids and asks."""
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)

    def addOrder(self, order):
        """Add orders to the correct dictionary dependant on their type. Stored in the dictionary at their price point."""
        if order.side == 'buy':
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)
        
    def removeOrder(self, order):
        """Remove the specific order, as passed in, from the matching dictionary."""
        if order.side == 'buy':
            self.bids[order.price].remove(order)
            #if the last order at a given price level is removed ensure the entire price level is deleted
            if not self.bids[order.price]:
                del self.bids[order.price]
        else:
            self.asks[order.price].remove(order)
            if not self.asks[order.price]:
                del self.asks[order.price]

    def bestBid(self):
        """Return the price of the highest bid within the order book."""
        #ensure a bid exists in the order book
        if not self.bids:
            return None
        return max(self.bids)
    
    def bestAsk(self):
        """Return the price of the lowest ask within the order book."""
        if not self.asks:
            return None
        return min(self.asks)

    def midPrice(self):
        """Return mean of the highest bid and lowest ask."""
        b = self.bestBid()
        a = self.bestAsk()
        if not a or not b:
            return None
        return (b + a)/2
    
    def spread(self):
        """Return difference between the price of the highest bid and lowest ask."""
        b = self.bestBid()
        a = self.bestAsk()
        if not a or not b:
            return None
        return (a - b)
    
    def bookDepth(self):
        """Print out the entirety of the book for debugging purposes."""
        #bids first
        for key in self.bids:
            sum = 0
            for i in range(len(self.bids[key])):
                sum += self.bids[key][i].quantity
            #ordered by price 
            print("Bid price " + str(key) + ": " + str(sum))
            
        #asks
        for key in self.asks:
            sum = 0
            for i in range(len(self.asks[key]) ):
                sum+=self.asks[key][i].quantity
            print("Ask price " + str(key) + ": " + str(sum))