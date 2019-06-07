import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")

class Green(Color):
    def fill(self):
        print("Inside Green::fill() method.")

class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")

class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getShape(self,shapeType):
        pass
    def getColor(self, color):
        pass

class ShapeFactory(AbstractFactory):
    def getShape(self,shapeType):
        if shapeType=="CIRCLE":
            return Circle()
        elif shapeType=="RECTANGLE":
            return Rectangle()
        elif shapeType=="SQUARE":
            return Square()
        else:
            return None
    def getColor(self, color):
        return None

class ColorFactory(AbstractFactory):
    def getShape(self,shapeType):
        return None
    def getColor(self, color):
        if color == "RED":
            return Red()
        elif color=="GREEN":
            return Green()
        elif color =="BLUE":
            return Blue()
        else:
            return None

class FactoryProducer(object):
    @classmethod
    def getFactory(cls,choice):
        if choice=="SHAPE":
            return ShapeFactory()
        elif choice=="COLOR":
            return ColorFactory()
        else:
            return None

if __name__ == '__main__':
    '''
    抽象工厂模式的优点：
    1. 提供一个创建一系列相关或相互依赖对象的接口，而无需指定他们的类
    2. 当一个产品族中的多个对象设计成一起工作时，他能保证客户端始终只使用同一个产品族中的对象
    '''
    #获取形状工厂
    shapeFactory = FactoryProducer.getFactory("SHAPE")
    # 获取工厂Cicle、Rectangle、Square对象
    shape1 = shapeFactory.getShape("CIRCLE")
    shape2 = shapeFactory.getShape("RECTANGLE")
    shape3 = shapeFactory.getShape("SQUARE")
    # 调用三个对象的draw方法
    shape1.draw()
    shape2.draw()
    shape3.draw()
    #获取颜色工厂
    colorFactory = FactoryProducer.getFactory("COLOR")
    #获取Red、Green、Blue的对象
    color1 = colorFactory.getColor("RED")
    color2 = colorFactory.getColor("GREEN")
    color3 = colorFactory.getColor("BLUE")
    #调用三个对象的fill方法
    color1.fill()
    color2.fill()
    color3.fill()