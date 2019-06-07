import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Shape:Rectangle")

class Circle(Shape):
    def draw(self):
        print("Shape:Circle")

class ShapeDecorator(Shape,metaclass=abc.ABCMeta):
    def __init__(self,decorateShape):
        self._decoratedShape = decorateShape
    def draw(self):
        self._decoratedShape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self,decoratedShape):
        super().__init__(decoratedShape)
    def draw(self):
        self._decoratedShape.draw()
        self.setRedBorder(self._decoratedShape)

    def setRedBorder(self,decoratedShape):
        print("Border Color:Red")

if __name__ == '__main__':
    '''
    装饰器模式的优点：
    1. 动态地给对象添加额外的职责，比生成子类更加灵活
    2. 装饰类和被装饰类可以独立发展，不会相互耦合
    3. 装饰模式是继承的一个替代模式，可以动态扩展一个实现类的功能
    '''
    circle = Circle()
    redCircle = RedShapeDecorator(Circle())
    redRectangle = RedShapeDecorator(Rectangle())

    print("Circle with normal border")
    circle.draw()

    print("Circle of red border")
    redCircle.draw()

    print("Rectangle of red border")
    redRectangle.draw()


