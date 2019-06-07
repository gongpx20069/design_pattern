import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class Rectangle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class ShapeMaker(object):
    def __init__(self):
        self.__circle = Circle()
        self.__rectangle = Rectangle()
        self.__square = Square()

    def drawCircle(self):
        self.__circle.draw()

    def drawRectangle(self):
        self.__rectangle.draw()

    def drawSquare(self):
        self.__square.draw()

if __name__ == '__main__':
    '''
    外观模式的优点：
    1. 降低访问复杂系统内部子系统的复杂度，简化了客户端与之的接口
    2. 减少系统相互依赖
    3. 提高灵活性
    4. 提高了安全性
    '''
    shapeMaker = ShapeMaker()

    shapeMaker.drawCircle()
    shapeMaker.drawRectangle()
    shapeMaker.drawSquare()