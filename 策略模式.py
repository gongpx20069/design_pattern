import abc

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doOperation(self,num1,num2):
        pass

class OperationAdd(Strategy):
    def doOperation(self,num1,num2):
        return num1+num2

class OperationSubstract(Strategy):
    def doOperation(self,num1,num2):
        return num1-num2

class OperationMultiply(Strategy):
    def doOperation(self,num1,num2):
        return num1*num2

class Context(object):
    def __init__(self,strategy):
        self.__strategy = strategy
    def excuteStartegy(self,num1,num2):
        return self.__strategy.doOperation(num1,num2)

if __name__ == '__main__':
    '''
    策略模式的优点：
    1. 定义了一系列的算法，将其封装，并可以相互替换
    2. 算法可以自由切换
    3. 避免使用多重条件判断
    4. 扩展性良好
    '''
    context = Context(OperationAdd())
    print("10+5={}".format(context.excuteStartegy(10,5)))

    context = Context(OperationSubstract())
    print("10-5={}".format(context.excuteStartegy(10, 5)))

    context = Context(OperationMultiply())
    print("10*5={}".format(context.excuteStartegy(10, 5)))