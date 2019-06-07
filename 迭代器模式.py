import abc

class Iterator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hasNext(self):
        pass
    @abc.abstractmethod
    def next(self):
        pass

class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getIterator(self):
        pass

class NameRepository(Container):
    def __init__(self):
        self.names = ["Robert","John","Julie","Lora"]
    class NameIterator(Iterator):
        def __init__(self,name):
            self.index = -1
            self.name = name
        def hasNext(self):
            if self.index<len(self.name)-1:
                return True
            return False

        def next(self):
            if self.hasNext():
                self.index+=1
                return self.name[self.index]
            return None
    def getIterator(self):
        return self.NameIterator(self.names)

if __name__ == '__main__':
    '''
    状态模式的优点：
    1. 提供一种方法顺序访问一个聚合对象中的各个元素
    2. 无需暴露聚合对象的内部表示
    3. 支持以不同的方式遍历一个聚合对象
    4. 迭代器简化了聚合类
    5. 在同一个聚合上可以有多个遍历
    6. 在迭代器模式中，增加新的聚合类和迭代器类都很方便，无需修改原有代码
    '''
    nameRepository = NameRepository()
    iter = nameRepository.getIterator()
    i = 0
    while iter.hasNext() :
        name = iter.next()
        print("Name:{}".format(name))
        i+=1