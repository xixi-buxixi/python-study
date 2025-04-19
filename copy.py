import copy
y={"a":[1,2],"b":5}
x=y["b"]
print("x修改前,y=",y)
x=6
print("x修改后,y=",y)
print("a的地址",id("a"))
print("x地址",id(x))
#python中一般对静态变量的传递为拷贝，对动态变量的传递为引用。
#字符串、数值、元组均为静态变量；
#列表、字典、集合为动态变量
#浅拷贝修改第二层值，原来的也会变
#深拷贝则不会
import copy
y=[1,2,,['a','b']]
x=copy.copy(y)
print("浅拷贝，x修改前，y=",y)
x[2][1]='浅拷贝'
print("浅拷贝，x修改后，y=",y)
