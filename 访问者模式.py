import abc

class ComputerPart(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self,computerPartVisitor):
        pass

class Keyboard(ComputerPart):
    def accept(self,computerPartVisitor):
        computerPartVisitor.visit(self)

class Monitor(ComputerPart):
    def accept(self,computerPartVisitor):
        computerPartVisitor.visit(self)

class Mouse(ComputerPart):
    def accept(self,computerPartVisitor):
        computerPartVisitor.visit(self)

class Computer(ComputerPart):
    def __init__(self):
        self._parts = [Mouse(),Keyboard(),Monitor()]

    def accept(self,computerPartVisitor):
        for part in self._parts:
            part.accept(computerPartVisitor)
        computerPartVisitor.visit(self)

# 定义一个表示访问者的虚类（接口）

class ComputerPartVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self,item):
        pass

class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit(self,item):
        if isinstance(item,Computer):
            print("Displaying Computer")
        elif isinstance(item,Mouse):
            print("Displaying Mouse")
        elif isinstance(item,Keyboard):
            print("Displaying keyboard")
        elif isinstance(item,Monitor):
            print("Displaying Monitor")

if __name__ == '__main__':
    '''
    访问者模式的优点：
    1. 符合单一责任原则
    2. 稳定的数据结构和易变的操作耦合问题
    3. 将数据结构与数据操作分离
    4. 优秀的扩展性
    5. 灵活性
    '''
    # 使用ComputerPartDisplayVisitor来显示Computer的组成部分
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())