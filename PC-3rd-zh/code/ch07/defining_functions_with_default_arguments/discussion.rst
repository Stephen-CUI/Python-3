# 讨论

定义带有默认参数的函数看似很容易，但其实并不像看到的那么简单。

首先，对默认参数的赋值只会在函数定义的时候绑定一次

>>> x = 42
>>> def spam(a, b=x):
...     print(a, b)
...
>>> spam(1)
1 42
>>> x = 23
>>> spam(1)
1 42
>>>

注意到修改变量 x 的值（x 被作为函数参数的默认值）并没有对函数产生任何效果。这是因为默认值已经在函数定义的时候就确定好了。

其次，给默认参数赋值的应该总是不可变的对象，比如 None、True、False、数字或者字符串。

特别要注意的是，绝对不要编写这样的代码：
>>> def spam(a, b=[]):
...     print(b)
...     return b

如果这么做了就会陷入到各种麻烦之中。如果默认值在函数体之外被修改了，那么这种修改将在之后的函数调用中对参数的默认值产生持续的影响。示例如下：

>>> def spam(a, b=[]):
...     print(b)
...     return b
...
>>> x = spam(1)
[]
>>> x
[]
>>> x.append(99)
>>> x.append("Yow!")
>>> x
[99, 'Yow!']
>>> spam(1) # Modified list gets returned!
[99, 'Yow!']
[99, 'Yow!']
>>>

这很可能不是所期望的结果。要避免出现这种问题，最好按照解决方案中的做法，使用 None 作为默认值并在函数体中增加一个对默认值的检查。