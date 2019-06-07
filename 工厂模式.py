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

class ShapeFactory(object):
    def getShape(self, shapeType):
        if shapeType=="CIRCLE":
            return Circle()
        elif shapeType=="RECTANGLE":
            return Rectangle()
        elif shapeType=="SQUARE":
            return Square()
        else:
            return None

if __name__ == '__main__':
    '''
    工厂模式的优点：
    1. 一个调用者想创建一个对象，只要知道其名称
    2. 扩展性高，如果想增加一个产品，只要扩展一个工厂类就可以
    3. 屏蔽产品的具体实现，调用者只关心产品的接口
    '''
    shapeFactory = ShapeFactory()
    # 获取Cicle、Rectangle、Square的对象
    shape1 = shapeFactory.getShape("CIRCLE")
    shape2 = shapeFactory.getShape("RECTANGLE")
    shape3 = shapeFactory.getShape("SQUARE")
    #分别调用draw()方法
    shape1.draw()
    shape2.draw()
    shape3.draw()