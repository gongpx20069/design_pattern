import copy
import abc

class Prototype(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clone(self):
        pass
    def deep_clone(self):
        pass

class Shape(Prototype,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")
    def clone(self):
        return copy.copy(self)
    def deep_clone(self):
        return copy.deepcopy(self)

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")
    def clone(self):
        return copy.copy(self)
    def deep_clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    '''
    原型模式的优点：
    1. 用原型实例指定创建对象的种类，并通过拷贝这些原型创建新的对象
    2. 性能提高
    3. 逃避构造函数的约束
    '''
    # 初始化实例
    shape1 = Circle()
    shape2 = shape1.clone()
    shape3 = shape1.deep_clone()
    #分别调用draw()方法
    shape1.draw()
    shape2.draw()
    shape3.draw()
    #查看三个对象的地址，可以验证shape1与shape2地址相同（浅拷贝），shape3为深拷贝
    print(id(shape1))
    print(id(shape2))
    print(id(shape3))
