# def getHello(x):
#     if x==6:
#         return "good"
#     elif x<6:
#         return "bad"
#     else:
#         return "perfect"
#
# result=getHello(9)
# print(result)
import math
# def quadratic(a, b, c):
#     x=a*a+b+c
#     print(x)
#
# quadratic(3,7,9)

# def hehe(name,age,height=190):
#     return name,age,height
#
# print(hehe("xiaom",8,00))
# def add_end(L=[]):
#     L.append('END')
#     return L
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())
# print(add_end())

def calc(*nums):
    for num in nums:
        print(num)

# a=[1,2,3]
calc(1,3,4)
