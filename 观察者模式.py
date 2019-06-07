import abc
class Subject(object):
    def __init__(self):
        self.__observers = []
    def setState(self,state):
        self.__state = state
    def attach(self,observer):
        self.__observers.append(observer)
    def notifyAllObservers(self):
        for item in self.__observers:
            item.update()

class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._subject = None
    @abc.abstractmethod
    def update(self):
        pass

class BinaryObserver(Observer):
    def __init__(self,subject):
        super().__init__()
        self._subject = subject
        self._subject.attach(self)
    def update(self):
        print("Binary String:{}".format(self._subject.getState()))

class OctalObserver(Observer):
    def __init__(self,subject):
        super().__init__()
        self._subject = subject
        self._subject.attach(self)
    def update(self):
        print("Octal String:{}".format(self._subject.getState()))

if __name__ == '__main__':
    '''
    观察者模式的优点：
    1. 定义对象之间的一对多关系
    2. 当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新
    3. 观察者和被观察者是抽象耦合的
    4. 建立一套触发机制
    '''
    subject = Subject()
    OctalObserver(subject)
    BinaryObserver(subject)

    print("First state change:15")
    subject.setState(15)
    print("Second state change:10")
    subject.setState(10)