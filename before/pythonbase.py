#set 是一个无值的dict。要创建一个set，需要提供一个list作为输入集合
# 显示的顺序也不表示set是有序的
# set是无序的,set可以看成数学意义上的无序和无重复元素的集合
# >>> s = set([1, 1, 2, 2, 3, 3])
# >>> s
# {1, 2, 3}



#函数
#调用python自带函数


# abs(100)# 求绝对值
#max(1,2,3)  #求最大值


# a=abs
# print(a(-1))

#自定义函数 def

# def my_abs(x):
#     if x >=0:
#         return x
#     else:
#         return -x
# print(my_abs(-100))


# def my_abs2(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >=0:
#         return x
#     else:
#         return -x
# print(my_abs2('a'))


# import math

# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny
# r = move(100,100,60,math.pi/6)
# print(r)


# import math
# def quadrativ(a,b,c):
#     s = b**2 -4 * a * c
#     if s < 0 :
#         return '该方程误解'
#     elif s == 0:
#         v = -b /(2*a)
#         return v
#     else: 
#         x1 =round((-b + math.sqrt(b * b - 4*a*c))/(2*a),2)
#         x2 =round((-b - math.sqrt(b * b - 4*a*c))/(2*a),2)
#         return x1,x2
# r = quadrativ(2,3.58,1)
# print(r)



#函数的参数
#此时n设为默认参数，默认值为2
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def power(x,n=2):
#     s=1
#     while n>0 :
#         s = s* x
#         n=n-1
#     return s

# print(power(5))
# print(power(5,3))

#可变参数
def calc(*numbers):
    s=0
    for n in numbers:
        s = s+n
    return s
print(calc(1,2,3))

nums=[1,2,3]
print(calc(*nums))

