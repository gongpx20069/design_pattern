import abc
class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doAction(self,content):
        pass

class StartState(State):
    def doAction(self,content):
        print("Player is in start state")
        content.setState(self)
    def __str__(self):
        return "Start State"

class StopState(State):
    def doAction(self,content):
        print("Player is in stop state")
        content.setState(self)

    def __str__(self):
        return "Stop State"

class Content(object):
    def __init__(self):
        self.__state = None
    def setState(self,state):
        self.__state=state
    def getState(self):
        return self.__state

if __name__ == '__main__':
    '''
    状态模式的优点：
    1. 封装了转换原则
    2. 枚举可能的状态，在枚举状态之前需要确定状态种类
    3. 将所有与某个状态有关的行为放到一个类中，并且可以方便地增加新的状态，只需要改变对象状态即可改变对象的行为
    4. 允许状态转换逻辑与状态对象合成一体，而不是某一个巨大的条件语句块
    5. 可以让多个环境对象共享一个状态对象，从而减少系统中对象的个数
    '''
    content = Content()
    startState = StartState()
    startState.doAction(content)
    print(content.getState())
    stopState = StopState()
    stopState.doAction(content)

    print(content.getState())