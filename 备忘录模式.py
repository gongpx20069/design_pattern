class Memento(object):
    def __init__(self,state):
        self.__state = state
    def getState(self):
        return self.__state

class Originator(object):
    def setState(self,state):
        self.__state =state
    def getState(self):
        return self.__state
    def saveStateToMemento(self):
        return Memento(self.__state)
    def getStateFromMemento(self,Memento):
        self.__state = Memento.getState()

class CareTaker(object):
    def __init__(self):
        self.__mementoList = []
    def add(self,state):
        self.__mementoList.append(state)
    def get(self,index):
        return self.__mementoList[index]

if __name__ == '__main__':
    '''
    备忘录模式的优点：
    1. 在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存了这个状态
    2. 给用户提供了一种可以恢复状态的机制，可以使用户能够比较方便地回到某个历史状态
    3. 实现了信息的封装，使得用户不需要关心状态的保存细节
    '''
    originator = Originator()
    careTaker = CareTaker()
    originator.setState("State #1")
    originator.setState("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #4")

    print("Current State:{}".format(originator.getState()))
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State:{}".format(originator.getState()))
    originator.getStateFromMemento(careTaker.get(1))
    print("Second saved State:{}".format(originator.getState()))