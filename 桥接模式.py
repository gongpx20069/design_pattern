import abc
class DrawAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drawCircle(self,radius,x,y):
        pass

class RedCircle(DrawAPI):
    def drawCircle(self,radius,x,y):
        print("Drawing Circle[ color: red, radius: {}, x: {}, y:{}]".format(radius,x,y))

class GreenCircle(DrawAPI):
    def drawCircle(self,radius,x,y):
        print("Drawing Circle[ color: green, radius: {}, x: {}, y:{}]".format(radius,x,y))

class Shape(metaclass=abc.ABCMeta):
    def __init__(self,drawAPI):
        self._drawAPI = drawAPI
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,x,y,radius,drawAPI):
        super().__init__(drawAPI)
        self.__x = x
        self.__y = y
        self.__radius = radius

    def draw(self):
        self._drawAPI.drawCircle(self.__radius,self.__x,self.__y)

if __name__ == '__main__':
    '''
    桥接模式的优点：
    1. 将抽象部分与实现部分分离，使他们都可以独立变化
    2. 抽象和实现的分离
    3. 优秀的扩展能力
    4. 实现细节对客户透明
    '''
    redCircle = Circle(100,100,10,RedCircle())
    greenCircle = Circle(100,100,10,GreenCircle())

    redCircle.draw()
    greenCircle.draw()