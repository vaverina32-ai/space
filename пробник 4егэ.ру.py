#2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((y<=x) and not(w) and z) == 1:
#                     print(x, y, w, z)

5.txt
# ans = []
# for n in range(1,1000000):
#     n2 = f'{n:b}'
#     if sum(map(int,n2))%2==0:
#         n2+='11'
#     else:
#         n2+='01'
#     r = int(n2,2)
#     if r>61:
#         ans+=[r]
# print(min(ans))

#6
# from turtle import *
# tracer(0)
# k = 40
# screensize(2000,2000)
# lt(90)
# for i in range(5):
#     fd(8*k)
#     rt(90)
#     fd(11*k)
#     rt(90)
# up()
# for x in range(-30,30):
#     for y in range(-30,30):
#         goto(x*k, y*k)
#         dot(4, 'green')
# done()

#9
# f = open('1')
# k = 0
# for s in f:
#     a = [int(x)  for x in s.split()]
#     a2 = [x  for x in a  if x%10==5]
#     a.sort()
#     if (a[-1] + a[-2])*2 > (a[0]+a[1]+a[2])*3:
#         if len(a2)>=2:
#             k+=1
# print(k)

#11
# from math import *
# l = 256
# n = 10+4080
# i= ceil(log2(n))
# v = ceil(l*i/8)
# print((v*2**16)/1024/1024)

#14
# def perevod(x, osn):
#     s = ''
#     while x>0:
#         s = str(x%osn) + s
#         x//=osn
#     return s
# a = 4**644 + 4**322 + 16**35 - 64**3
# a4 = perevod(a,4)
# print(a4.count('3'))

#15
# x>0
# y>0
# for a in range(100000):
#     # for x in range(100000):
#     #     for y in range(100000):
#     if ((x<=19) or (y<2*x +a -50) or (y>17))==1:
#
#             print(a)

#16
# def f(n):
#     if n>400: return n**n
#     return n+6+ f(n+12)
# print(f(72)-f(108))

#23
def f(s,e):
    if s==e: return 1
    if s>e or s==22: return 0
    return f(s+3, e) + f(s+4, e)
print(f(16,38))