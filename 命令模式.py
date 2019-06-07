import abc

class Order(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

class Stock(object):
    def __init__(self):
        self.__name = "ABC"
        self.__quantity = 10

    def buy(self):
        print("Stock [ Name:{}, Quantity:{} ] bought".format(self.__name,self.__quantity))

    def sell(self):
        print("Stock [ Name:{}Quantity: {} ] sold".format(self.__name,self.__quantity))

class BuyStock(Order):
    def __init__(self,abcStock):
        self.__abcStock = abcStock
    def execute(self):
        self.__abcStock.buy()

class SellStock(Order):
    def __init__(self,abcStock):
        self.__abcStock = abcStock
    def execute(self):
        self.__abcStock.sell()

class Broker(object):
    def __init__(self):
        self.__orderList = []

    def takeOrder(self,Order):
        self.__orderList.append(Order)

    def placeOrders(self):
        for order in self.__orderList:
            order.execute()
        self.__orderList = self.__orderList.clear()

if __name__ == '__main__':
    '''
    命令模式的优点：
    1. 将一个请求封装成对象，从而可以用不同的请求对客户参数化
    2. 降低了系统耦合度
    3. 新的命令可以很容易添加到系统中
    '''
    abcStock = Stock()
    buyStockOrder = BuyStock(abcStock)
    sellStockOrder = SellStock(abcStock)

    broker = Broker()
    broker.takeOrder(buyStockOrder)
    broker.takeOrder(sellStockOrder)

    broker.placeOrders()