from collections import defaultdict, deque
from order import order

class orderBook:
    """Represents all orders currently awaiting a match, used by the matching engine."""
    def __init__(self):
        """Intialise the book, by creating two seperate dictionaries to store bids and asks."""
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)


