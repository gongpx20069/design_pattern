import abc

class Game(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize(self):
        pass
    @abc.abstractmethod
    def startPlay(self):
        pass
    @abc.abstractmethod
    def endPlay(self):
        pass
    # 模板
    def _play(self):
        self.initialize()
        self.startPlay()
        self.endPlay()

class Cricket(Game):
    def endPlay(self):
        print("Cricket Game Finished!")
    def initialize(self):
        print("Cricket Game Initialized! Start playing")
    def startPlay(self):
        print("Criket Game Started. Enjoy the game!")

class Football(Game):
    def endPlay(self):
        print("Football Game Finished!")
    def initialize(self):
        print("Football Game Initialized! Start playing")
    def startPlay(self):
        print("Footbal Game Started. Enjoy the game!")

if __name__ == '__main__':
    '''
    模板模式的优点：
    1. 封装不变部分，扩展可变部分
    2. 提取公共代码，便于维护
    3. 行为由父类控制，字类实现
    4. 模板方法可以使子类不改变你一个算法的结构即可重定义该算法的某些特定步骤
    '''
    game = Cricket()
    game._play()

    game = Football()
    game._play()