#-*-coding:utf-8-*-#
"""
@Author: ypp
@Filetype:python source code
@Tool: Vim & Gcc
"""

import numpy as np
s = np.random.rand(1,3)#均匀分布中取出3个随机数
s = np.random.random((1,3))#和上面的方法只是参数传递不同而已
s = np.random.uniform(1,6,10)#在１－６之间生成１０个浮点随机数
s = np.random.randint(1,6,10)#......................整形随机数
s = np.random.normal(size=(5,2))#符合标准正太分布,5*2
s = np.arange(10)#输出（0,1,2,3,4,5,6,7,8,9)
s = np.random.choice(s,7)#在ａ中有放回的取出７次
s = np.random.choice(s,7,replace = False)#在ａ中无放回的取出７次
