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
