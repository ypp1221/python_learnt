#-*-coding:utf-8-*-#
"""
@Author: ypp
@Filetype:python source code
@Tool: Vim & Gcc
"""

"""
取两位小数
a = '0.1233444'
s = round(a,2)
"""
def two_round(a):
    return round(a,2)


a = 0.22222
print(two_round(a))
