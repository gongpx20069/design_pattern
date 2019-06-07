class SingleObject(object):
    #cls是一个类
    def __init__(self,cls):
        self._cls = cls
        self._instance = {}
    #将类的对象变为可调用对象（函数）
    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@SingleObject
class cls(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    '''
    单例模式的优点：
    1. 保证一个类只有一个实例，并提供一个访问它的全局访问点
    2. 在内存里只有一个实例，减少了内存开销和频繁的创建和销毁实例
    3. 避免对资源的多重占用
    '''
    #获取单例
    cls1 = cls()
    cls2 = cls()
    # Python的id关键字可以查看对象在内存中存放位置
    print(id(cls1),id(cls2),id(cls1)==id(cls2))