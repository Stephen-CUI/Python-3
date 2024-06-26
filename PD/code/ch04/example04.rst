在程序进行赋值时，就会创建一个新引用

>>> a = [1, 2, 3, 4]
>>> b = a
>>> b is a
True
>>> b[2] = 999
>>> a
[1, 2, 999, 4]
>>>

对于容器对象（如列表和元组），存在两种类型的复制操作：浅复制和深复制，浅复制创建一个对象，但使用原始对象所包含项目的引用来填充容器

>>> a = [1, 2, [3, 4]]
>>> b = list(a)      # 创建一个 a 的浅复制
>>> b is a
False
>>> b.append(999)    # 将元素追加到 b
>>> a                # 注意，a 没有改变
[1, 2, [3, 4]]
>>> b
[1, 2, [3, 4], 999]
>>> b[2][0] = -99
>>> a                # 注意，a 发生改变
[1, 2, [-99, 4]]
>>> b
[1, 2, [-99, 4], 999]
>>> 
>>> a[2] is b[2]     # 这两个引用的是同一个标识
True
>>> 

深复制创建一个新对象，并递归地复制对象包含的所有对象。没有内置运算符可供创建对象的深度复制，但是可以使用标准库中的 ``copy.deepcopy()``函数

>>> import copy
>>> a = [1, 2, [3, 4]]
>>> b = copy.deepcopy(a) 
>>> b[2][0] = -100
>>> b
[1, 2, [-100, 4]]
>>> a   # 注意，a 并未改变
[1, 2, [3, 4]]
>>> 