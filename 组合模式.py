class Employee(object):
    def __init__(self,name,dept,sal):
        self.__name = name
        self.__dept = dept
        self.__salary = sal
        self.__subordinates = []
    def add(self,e):
        self.__subordinates.append(e)

    def remove(self,e):
        self.__subordinates.remove(e)

    def getSubordinates(self):
        return self.__subordinates

    def __str__(self):
        return "Employee :[ Name :{}, dept :{}, salary :{} ]".format(self.__name,self.__dept,self.__salary)

if __name__ == '__main__':
    '''
    组合模式的优点：
    1. 将对象组合成树形结构以表示“部分-整体”的层次结构，使用户对单个对象和组合对象的使用具有一致性
    2. 高层模块调用简单
    3. 节点自由增加
    '''
    CEO = Employee("John","CEO",3000)
    headSales = Employee("Robert","Head Sales",2000)
    headMarketing = Employee("Michel","Head Marketing",2000)

    clerk1 = Employee("Laura","Marketing",10000)
    clerk2 = Employee("Bob","Marketing",10000)

    salesExecutive1 = Employee("Richard","Sales",10000)
    salesExecutive2 = Employee("Rob","Sales",10000)

    CEO.add(headSales)
    CEO.add(headMarketing)

    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)

    print(CEO)
    for headEmployee in CEO.getSubordinates():
        print(headEmployee)
        for employee in headEmployee.getSubordinates():
            print(employee)