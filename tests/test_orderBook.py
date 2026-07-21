from src.exchange.order import order
from src.exchange.orderBook import orderBook

#currently testing by fully printing out
#will switch to pytest later in development

def test_orderBook():
    book = orderBook()
    order1 = order(0, 0, "buy", 0, 100, 50, 1)
    order2 = order(0, 0, "buy", 0, 100, 100, 2)
    order3 = order(0, 0, "sell",0, 110, 50, 1)
    order4 = order(0, 0, "sell", 0, 115, 50, 1)

    book.addOrder(order1)
    book.addOrder(order2)
    book.addOrder(order3)
    book.addOrder(order4)

    print(book.bestBid())
    print(book.bestAsk())
    print(book.midPrice())
    print(book.spread())
    print(book.bookDepth())

    #assert book.bestBid() == 100

test_orderBook()