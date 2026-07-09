class order:
    """Represents an individual order sent to the matching engine."""
    def __init__(self, orderIdIn, traderIdIN, sideIn, typeIn, priceIn, quantityIn, timeIn):
        self.orderId = orderIdIn
        self.tradrId = traderIdIN
        self.side = sideIn
        self.type = typeIn
        self.price = priceIn
        self.quantity = quantityIn
        self.quantityRemaining = quantityIn
        #time stamp used to maintain time priority in matching engine
        self.timeStamp = timeIn

