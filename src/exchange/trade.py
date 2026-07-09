class trade:
    """Represents executed transactions, as a combination of two orders."""
    def __init__(self, tradeIdIn, buyIdIn, sellIdIN, priceIn, quantityIn, timeIn, causeSideIn):
        self.tradeId = tradeIdIn
        self.buyId = buyIdIn
        self.sellId = sellIdIN
        self.price = priceIn
        self.quantity = quantityIn
        self.quantityTraded = quantityIn
        self.timeStamp = timeIn
        #the side of the order sent to the matching engine latest (hence the cause of the trade)
        self.side = causeSideIn
