# -*- coding: utf-8 -*-

print ('hello world')

# def add(x,y,f):
# 	return f(x)+f(y)
# # 把函数作为参数传入，这样的函数称为高阶函数，
# # 函数式编程就是指这种高度抽象的编程范式。
# print add(-5, 6, abs)


# L = list(range(10))
# def f1(x):
# 	return x*x
# def f2(x,y):
# 	return x*y
# def char2num(s):
# 	digits = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]

# # 高阶函数map：
# # map()函数接收两个参数，一个是函数，一个是Iterable(可迭代的），
# # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator（迭代器）返回。
# print list(map(f1,L))
# print list(map(char2num, 'bce57'))

# # 高阶函数：reduce
# # reduce把一个函数作用在一个序列上，
# # 这个函数必须接收两个参数，
# # reduce把结果继续和序列的下一个元素做累积计算
# print reduce(f2, map(char2num, 'bce57'))

# L1 = ['adam', 'LISA', 'barT']
# L2 = [9,3,5,7]
# st = 'helLO, wORlD!'
# print st.title()

# def Dx(x):
# 	y = x.title()
# 	return y
# print list(map(Dx,L1))

# def Qj(x,y):
# 	z = x*y
# 	return z

# def prod(L3):
# 	return reduce(Qj, L3)
# if prod([3, 5, 7, 9]) == 945:
#     print(u'测试成功!')
# else:
#     print(u'测试失败!')

# filter()也接收一个函数和一个序列，
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# def is_odd(n):
# 	return n%2==0
# print list(filter(is_odd, list(range(10))))

# # 求素数：
# def sss(x):
# 	n = 2
# 	if isinstance(x,int) == False or x<2:
# 		return False
# 	elif x==2:
# 		return 2
# 	else:
# 		while n<x:
# 			if x%n!=0:
# 				n=n+1
# 			else:
# 				return False
# 		return x
# print list(filter(sss, range(2,55)))

# 回数：从左向右读和从右向左读都是一样的数
# def hhh(x):
# 	b = str(x)
# 	c = list(b)
# 	n=0
# 	m=len(c)-1
# 	while n<=m:
# 		if c[n]==c[m]:
# 			n+=1
# 			m=m-1
# 			return x
# 		else:
# 			return False
	
# print list(filter(hhh,range(100)))
# # 利用切片筛选回数------这个厉害
# def is_palindrome(n):
# 	s = str(n)
# 	return s[::-1]==s
# print list(filter(is_palindrome,range(200)))

# # sorted()也是一个高阶函数，
# # 它还可以接收一个key函数来实现自定义的排序
# L01 = [3,7,1,9,2,-3,-9]
# L02 = ['bob', 'about', 'Zoo', 'Credit','AAd']
# print sorted(L01, key = abs)
# print sorted(L02)
# # 默认对字符串按照ASCII的大小，由于'Z' < 'a'
# print sorted(L02, key=str.lower)
# # 要进行反向排序，不必改动key函数，
# # 可以传入第三个参数reverse=True
# print sorted(L02, key=str.lower, reverse=True)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print sorted(L)
# # 算是明白了，key的作用是对每一个排序的对象进行对应的函数的操作，
# # 然后将操作后的结果排序，再映射回原来的值。
# # 这样的话，要按照名字排序，就只需要返回tuple里面的姓名信息就好。
# # 要按照成绩排序，就返回tuple里面的成绩信息。
# def by_name(t):
# 	return t[0]
# def by_score(t):
# 	return t[1]
# print sorted(L, key=by_score)


# 返回函数
# 返回闭包时牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f1 = lazy_sum(1,2,3,4,5)
print(f1())
f2 = lazy_sum(1,2,3,4,5)
print(f1()==f2())
print(f1==f2)


