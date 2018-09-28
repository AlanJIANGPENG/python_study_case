# -*- coding: utf-8 -*-

print 'hello world'
# print '你好' # 注意编码格式UTF8
# name = raw_input("Please input your name:")    # Python2/3 input语法区别
# print "hello", name
# print "hello " + name

# print u"整数：",      # python2输出中文语法
# print 100, -10

# print u'浮点数：',
# print 1.20, -9.01

# s1 = input()   # python2 input（）输入整数， raw_input()是字符串
# s2 = 12.3e4
# print s1,s2
# if s1 == s2:
# 	print 'Passed'
# else:
# 	print "Failed"

# print u'字符串：'
# a = "I'm OK!"
# print a
# for  i in a:
# 	print i,
# print len("I'm OK!")
# print '\\\t\\'
# print r"\\\t\\"
# print '''line1
# line2
# line3'''

# print u'布尔值：'
# n1 = 123.0
# n2 = 123
# print n1==n2
# print n1>n2

# print u'空值: None'

# print 10.0/3
# print 10/3
# print 10%3

# print u'中文'
# aa = u'Hi %s, your score is %f, 你是第%d名。' %(u'艾伦', 100, 11)
# print aa


# l1 = ['alan', 'bob', 'candy', 'david']
# print l1
# print len(l1)
# print l1[0]
# print l1[3]
# print l1[-2]
# l1.append('cathrilien')
# print l1
# l1.insert(2, 'will')
# print l1
# l1.pop(5)
# print l1
# l1[4] = 'allen'
# print l1


# t1 = ('alan', 'bob', 'candy')
# print t1
# # tuple没有 append/insert/pop
# t2 = ('alan', 'bob', ['A', 'B', 'C'])
# print t2[2][0]
# print t2[2][1]
# print t2[2][2]
# t2[2][0] = 'Allen'
# t2[2][2] = 'Will'
# print t2

# L = [[1,2,3,4], ['a','b','c','d'], ['java', 'phton','ruby', 'php']]
# print L[0][0]
# print L[1][1]
# L[2][1] = 'python'
# print L[2]


# a = input('Please input your age :')
# if a>18:
# 	print 'Hi man'
# 	print 'Your age is '+ str(a) +'!'
# else:
# 	print 'Hello baby'
# 	print "Your age is",a

# a1 = input('input your age:')
# if a1>=24:
# 	print 'Hi man'
# elif a1>18:
# 	print 'Hi young'
# else:
# 	print "Hello kid"

# height = input('height:')
# weight = input('weight:')
# bmi = weight/(height*height)
# print bmi
# if bmi<18.5:
# 	print u'过轻'
# elif 18.5<=bmi<25:
# 	print u'正常'
# elif 25<=bmi<28:
# 	print u'较重'
# elif 28<=bmi<32:
# 	print u'肥胖'
# else:
# 	print u'严重肥胖'


# for tu in t2:
# 	print tu
# for tup in t2[2]:
# 	print tup
# for  l in L:
# 	print l

# sum = 0
# # for i in range(101):
# # 	if i==50:
# # 		continue
# # 	sum = sum + i

# n=0
# while n<100:
# 	n = n + 1
# 	if n == 50:
# 		continue
# 	sum = sum + n
# print sum


# dict = {'alan':11, 'bob':22, 'candy':33, 'doctor':44}
# print dict['alan']
# print ('tom' in dict)
# print dict.get('tom', 'there is no tom')
# dict['tom'] = 55
# print dict
# for key in dict:
# 	print key


# print abs(-21)
# print max(33,12,56,-99,-11,44)
# print int('123')
# f1 = float('12.3')
# s1 = str(12.3)
# print f1
# print s1
# print f1==s1
# print bool(0)
# print bool("")


# def my_qwer():
# 	pass
# def my_asd(x,n=2):
# 	s = 1
# 	if n>0:
# 		while n>0:
# 			n = n-1
# 			s = s*x
# 		return s
# 	elif n<0:
# 		while n<0:
# 			n = n+1
# 			s = s*x
# 		return 1.0/s
# 	else:
# 		return 1

# print my_asd(-2,-3)
# print my_asd(5)

# def stu(name, gender, age=18, city='QingDao'):      # 定义默认参数要牢记一点：默认参数必须指向不变对象！ 
# 	print 'name:',name
# 	print 'gender:',gender
# 	print 'age:', age
# 	print 'city:',city

# stu('alan', 'F', city='Beijing')


# def cal(*num):
# 	sum = 0
# 	for n in num:
# 		sum = sum+n*n
# 	return sum

# print cal(1,2)
# L = [1,2,3]
# T = (1,2,3,4)
# print cal(*L)
# print cal(*T)


# def per(name, age, **kw):
# 	print 'name:', name
# 	print 'age:', age
# 	print 'other:', kw

# per('alan', 18)

# dict1 = {
# 	'job': 'Engineer',
# 	'city': 'QingDao',
# 	'gender': 'M'
# }
# per('bob', 19, **dict1)

# def f1(a,b,c=0,*args,**kw):
# 	print 'a=',a
# 	print 'b=',b
# 	print 'c=',c
# 	print 'args=',args
# 	print 'kw=',kw

# def f2(a,b,c=0,* d,**kw):
# 	print 'a=',a
# 	print 'b=',b
# 	print 'c=',c
# 	print 'd=',d
# 	print 'kw=',kw
# f1(1,2,3,'a','b',kw='x6')
# f2(1,2,d=44,ex=None)
# # f2(1,2,'a','b',ex=None)


# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


# 递归：
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print fact(5)

# 递归思想： 汉诺塔
def move(n, a, b, c):
	if n == 1:
 	   print(a, '-->', c)
	else:
 	   move(n-1,a,c,b)
 	   move(1,a,b,c)
 	   move(n-1,b,a,c)
move(3,'A','B','C')



L1 = (1,2,3,4,5,6,7,8,9,0)
L2 = ['a','b','c','d','e','f','g','h']
L3 = list(range(100))
L4 = tuple(range(100))
D1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}

# r = []
# n = 3
# for i in range(n):
# 	r.append(L1[i])
# n=0
# while n<3:
# 	r.append(L1[n])
# 	n=n+1
# print r

# # 切片（Slice）list/tuple
# print L1[0:3]      # 前三个    
# print L1[3:4]      # 第4个
# print L1[-1]      # 最后一个
# print L1[7:]      # 从第八个开始之后所有
# print L1[-3:]      # 最有三个

# print L3[:10]      # 前十个
# print L3[-10:]      # 后十个
# print L3[:]      # 复制数列
# print L3[::5]      # 该数列所有，每5个取一个
# print L3[10:20:2]      # 该数列11-20个，每2个取一个

# # Python的for循环不仅可以用在list或tuple上
# for m in "ABCDE":
# 	print m

# for k in D1:      # 字典dict无顺序, 默认迭代key
# 	print k

# for v in D1.values():
# 	print v

# for k, v in D1.items():
# 	print k, v

# for x,y in [(0,0),(1,1),(2,4),(3,9)]:
# 	print (x,y)

# for i, v in enumerate(L2):
# 	print i,v

# def findMinandMax(L):
# 	if L ==[]:
# 		print u'数列为空'
# 	else:
# 		min = max = L[0]
# 		for i in L:
# 			if i<min:
# 				min = i
# 			elif i>max:
# 				max = i
# 		print(min,max)

# findMinandMax([22,33,11,23,44,78,54,43,-99])
# L0=[]
# findMinandMax(L0)

# print (min(L3), max(L3))


# # 列表生成式：
# print [x*x for x in range(1,11) if x%2==0]
# print [m+n for m in "ABC" for n in 'XYZ']

# print [d for d in os.listdir('.')]

# LL = ['Hello', 'World', 18, 'Apple', None]
# print [l.lower() for l in LL if isinstance(l,str)]


# 生成器：
# J = [x*x for x in range(10)]
# print J
# G = (x*x for x in range(10))
# # for g in G:
# # 	print g

# 斐波那契序列
def fib(max):
	n,a,b=0,0,1
	while n<max:
		# print b
		yield b
		a,b=b,a+b
		n=n+1
	# return 'OK'
f = fib(6)
print f
# generator是非常强大的工具。
# 注意区分普通函数和generator函数，普通函数调用直接返回结果
# generator函数的“调用”实际返回一个generator对象







