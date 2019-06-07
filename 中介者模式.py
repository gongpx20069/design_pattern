import time

class ChatRoom(object):
    @classmethod
    def showMessage(cls,user,message):
        print(time.strftime("%b %d %H:%M:%S"),"[{}]".format(user.getName()),message)

class User(object):
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def sendMessage(self,message):
        ChatRoom.showMessage(self,message)

if __name__ == '__main__':
    '''
    中介者模式的优点：
    1. 中介者使各对象不需要显式地相互引用，使其耦合松散，可以独立地改变它们之间的交互
    2. 降低了类的复杂度，将一对多转化成了一对一
    3. 各个类之间的解耦
    4. 符合迪米特原则
    '''
    robert = User("Robert")
    john = User("John")

    robert.sendMessage("Hi! John!")
    john.sendMessage("Hello! Robert!")