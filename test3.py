# -*- coding: utf-8 -*-

print ('hello world')

# # 面向对象最重要的概念就是类（Class）和实例（Instance）
# # 类是抽象的模板
# # 实例是根据类创建出来的一个个具体的“对象”，
# # 每个对象都拥有相同的方法，但各自的数据可能不同。

# # 通过class关键字定义类
class Kids(object):    
	pass

# # class后面紧接着是类名(如Students)，类名通常是大写开头的单词，
# # 紧接着是(object)，表示该类是从哪个类继承下来的，
# # 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类

# # 定义好了类，就可以根据类创建出实例，
# # 创建实例是通过类名+()

# # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# # 通过定义一个特殊的__init__方法，在创建实例的时候，就把某些属性绑上去：

class Students(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_p1(self, gender):
        print('%s is %s and the score is %s' % (self.name, gender, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 注意：__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
# 必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去：

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。


a1 = Students('bob', 59)
a2 = Students('alan', 87)
# a3 = Students()

print('a1.name =', a1.name)
print('a2.score =', a2.score)
a2.print_p1('M')      # 封装结果
# a3.print_p1("F")

print('bob grade:', a1.get_grade())
print('alan grade:', a2.get_grade())























