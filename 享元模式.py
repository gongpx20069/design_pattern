import abc
import random
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,color):
        self.__color = color

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def setRadius(self,radius):
        self.__radius = radius

    def draw(self):
        print("Circle: Draw() [Color :{}, x :{}, y :{}, radius :{}".format(self.__color,self.__x,self.__y,self.__radius))

class ShapeFactory(object):
    circleMap = {}
    @classmethod
    def getCircle(self,color):
        if color in ShapeFactory.circleMap.keys():
            circle = ShapeFactory.circleMap[color]
        else:
            circle = Circle(color)
            ShapeFactory.circleMap[color] = circle
            print("Creating circle of color:{}".format(color))
        return circle

if __name__ == '__main__':
    '''
    享元模式的优点：
    1. 在有大量对象时，可以避免重复创建已经有的对象
    2. 大大减少了对象的创建，降低系统内存损耗，使效率提高
    '''
    colors = ["Red","Green","Blue","White","Black"]
    for i in range(0,21):
        circle = ShapeFactory.getCircle(random.choice(colors))
        circle.setX(random.randint(0,100))
        circle.setY(random.randint(0,100))
        circle.setRadius(100)
        circle.draw()