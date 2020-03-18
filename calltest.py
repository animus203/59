# Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，
# 这个类型就成为可调用的。换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。



class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)


p = Person('Bob', 'male')
p('Tim')
p.__call__('animus')                            #两句话相同