import abc
class Image(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self,filename):
        self.__filename = filename
        self.__loadFromDisk(self.__filename)

    def display(self):
        print("Displaying {}".format(self.__filename))

    def __loadFromDisk(self,filename):
        print("Loading {}".format(filename))

class ProxyImage(Image):
    def __init__(self,filename):
        self.__filename = filename
        self.__realimage = None

    def display(self):
        if self.__realimage == None:
            self.__realimage = RealImage(self.__filename)
        self.__realimage.display()

if __name__ == '__main__':
    '''
    代理模式的优点：
    1. 为其他对象提供一种代理以控制对这个对象的访问
    2. 职责清晰
    3. 高扩展性
    4. 智能化
    '''
    image = ProxyImage("test.jpg")

    #图像从磁盘加载
    image.display()

    #图片不需要从磁盘加载
    image.display()