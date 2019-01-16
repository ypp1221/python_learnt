#-*-coding:utf-8-*-#
"""
@Author: ypp
@Filetype:python source code
@Tool: Vim & Gcc
"""
"""
is 比较的是对象（地址）
== and != 比较的是内存中的值
"""
a = 1
b = 1.0
c = 1
print(a == b)#True
print(a is b )#False
print(a is c)#True
