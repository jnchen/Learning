# Python improve

标签（空格分隔）： Python 笔记

---

##高阶函数  

可以将函数作为函数的参数

 **map()函数**

接收一个函数f和一个list，把函数f依次作用在list的每个元素上，得到一个新的list并返回  
函数原型 `map(function,list)`

```python
def f(x):
    return x * x
print map(f,range(1,10))
Result:[1,4,9,16,25,36,49,64,81]
```

**reduce()函数**

接收一个函数f和一个list，但传入的函数f必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值  
reduce()函数还可以传入第三个参数，代表了计算的初始值，即第一次执行f传入初始值和list第一个元素  
函数原型 `reduce(function,list)`

 **filter()函数**

接收一个函数f和一个list，函数f的作用是对每个元素进行判断，返回True或False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list  
函数原型 `filter(function,list)`

 **sorted()函数**

接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素x，y，如果x应该排在y前面，返回-1，如果x应该排在y后面，返回1。x和y相等返回0  
函数原型 `sorted(list,function)`

---

## 闭包

内层函数引用了外层函数的变量(参数也算变量),然后返回内层函数的情况，称为闭包(Closure)  
特点:返回的函数还引用外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
  
通俗讲，将内部函数返回在外部能够正常使用

```python
//反例
#希望一次返回3个函数，分别计算1**2 2**2 3**2
def count():
    fs =[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
    
f1,f2,f3 = count()
f1(),f2(),f3()
Result: 9,9,9
//fs返回后，i的值最后为3

//正例
def count():
    fs = []
    for i in range(1,4):
        def f(i):
            def f2():
                return i*i
            return f2
        r = f(i)
        fs.append(r)
    return fs    
f1,f2,f3 = count()
Result:1,4,9
```

---

#匿名函数  

关键字lambda表示匿名函数

```python
def f(x):
    reutrn x*x
//等价于
lambda x:x*x
```

---

## decorator  

本质上就是一个高阶函数，传入的参数和传出的参数均为函数，对传入的函数进行包装以后return  

```python
def log(f):
    def fn(x): #这个函数是当做return的量定义的
        print 'log call %s'%f.__name__
        return f(x)
    return fn
    
def func(x):
    print x
//////////////////////////
f = new log(func)
f()
//以上两句可通过在函数前@log来简化
@log
def func():
    print x
    
func()


//带多个参数的函数修饰器
def log(f):
    def fn(*args,**kw):
        print 'call %s()'%f.__name__
        return f(*args,**kw)
    return fn
    
```

## 带参数decorator  

```python
def log(arg):
    def log_decorator(f):
        def fn(*args,**kw):
            print 'call %s() arg:%s'%(f.__name__,arg)
            return f(*args,**kw)
        return fn
    return log_decorator
   
@log('DEBUG')
def test(x):
    print x

test()
/////////////////////////////////////
#此时的test函数已经变成了对内部fn的引用
//
//
#为了保留最初test的引用利用了functools模块中的wraps来复制原函数的__name__,__doc__
//将
def log(f):
    def wrapper(*args,**kw):
        print 'call...'
        return f(*args,**kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
//变成
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print 'call...'
        return f(*args,**kw)
    return wrapper

```

---

## 偏函数  
functools.partial函数

```python
//python 2.x
import functools
sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.supper()))

sorted_ignore_case(list)

///不用偏函数实现 python2.x
sorted(list,cmp=lambda x,y:cmp(x.upper(),y.upper()))

```

---

## 导入模块  

```python
import moduleName  
#不存在冲突，需要通过模块名引用函数/属性

from moduleName import attribute/method
#有可能存在冲突

from moduleName import attr/method as alias
#moduleName中的attr/method变成了alias
```

如果导入模块不存在，Python会报ImportError错误  
```python
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
//Another Example
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})
```

---

## \_\_future\_\_

python新版本的功能会在老版本的`__future__`库中存在，可以导入`__future__`模块来“试用”

---

## 安装第三方模块  
###pip  
下载pip包
python setup.py install
pip install web.py

---

# 面向对象编程

## 定义类、创建类实例
class 关键字定义类，通常以大写字母开头，然后是`(object)`代表类是从哪个类继承下来  
创建类实例: 使用`类名+()`

## 创建实例属性  
创建实例后直接对属性赋值创建

```python
xiaoming = Person()
xiaoming.name = 'XiaoMing'
xiaoming.age = 22
xiaoming.gender = 'Male'
```

## 初始化实例属性  
类在创建时应该有一些所有类实例通用的属性  
在定义类时，增加一个特殊的`__init__()`方法,该方法会在创建实例时自动被调用  
`__init__()`方法的第一个参数必须是*self*(也可以用别的名字，习惯用法是self)  
在创建实例时，必须提供除了*self*之外的参数  

## 访问控制  
如果一个属性由双下划线开头，该属性就无法被外界访问 

## 类属性  
实例属性不会影响其他实例，每个实例各自拥有，互相独立  
类属性，在一个的无数个实例中有且只有一份   
类属性通过**`类名.属性名`**直接访问

当实例属性和类属性重名时，实例属性优先级高  
*可见，不要在实例上修改类属性，实际上并没有修改类属性， 而是给实例绑定了一个实例属性*

## 实例方法  
在类中定义的函数，它的第一个参数永远都是`self`，指向调用该方法的实例本身，其他参数和一个普通参数是完全一样的  

方法也是一个属性，可以动态的添加到实例上，但需要用types.MethodType()把一个函数变为一个方法:
```python
import types
def fn_get_grade(self):
    if self.score >=80:
        return 'A'
    elif self.score >=60:
        return 'B'
    else:
        return 'C'
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

p1 = Person('Bob',90)
p1.get_grade = types.MethodType(fn_get_grade,p1,Person)
print p1.get_grade()
# => A
p2 = Person('Alice',65)
print p2.get_grade()
# ERROR : AttributeError : 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade
```

将函数调用赋给属性，也可以为实例增加方法，不过和绑定方法不同，不用传入self

## 类方法  

类方法不属于实例，直接属于类  
通过标记`@classmethod`，将一个方法绑定到类上，类方法的第一个参数将传入`这个类自己`，通常读取类属性，无法获得实例变量。  

---

## 继承  

继承实现了is关系
has关系用组合来实现 (类中的属性)  

### python继承的特点

总是从某个类继承
不要忘记调用`super().__init__`  
```python
#子类的__init__
def __init__(self,args):
    super(SubClass,self).__init__(args)
```

### 判断实例的类型

`isinstance(obj,Type)`返回obj是否是Type的实例

### 多重继承  

**多重继承的目的**是从两种继承树中分别选择并继承出子类，以便组合功能使用  

### 获取对象信息

`type()`     获取变量的类型`type(arg)`
`dir()`      获取变量的所有属性`dir(arg)`
`getattr()`  获取属性`getattr(arg,name)`
`setattr()`  设置属性`setattr(arg,name,value)`  

---

## 特殊方法  

类似java `toString()`的方法`__str__()`，在print的时候会自动调用该实例的`__str__()`  

用于`print()`的`__str__()`
用于`len()`的`__len__()`
用于`cmp()`的`__cmp__()` 2.x

特点：  
特殊方法定义在class中
不需要直接调用Python的某些函数或操作符会调用相对应的特殊方法  

怎么实现：  
只需要编写用到的特殊方法  
有关联性的特殊方法都必须实现 `__getattr__` `__setattr`

### \_\_str\_\_

即java的toString 
`__repr__`可以在命令行中直接打印toString，不用print

### \_\_len\_\_  

实现了`__len__`就可以用`len()`函数返回实例‘长度’

### \_\_add\_\_

实现了`__add__`就可以用`+`来进行运算

### \_\_sub\_\_

实现了`__sub__`就可以用`-`来进行减运算

实现了`__mul__`就可以用`*`来进行乘运算

实现了`__div__`就可以用`/`来进行除运算 2.x

实现了`__truediv__`可以用`/`来进行除运算 3.x
实现了`__divmod__`可以用`//`来进行整除运算 3.x

实现了`__mod__`可以用`%`来进行取余运算

### 类型转换特殊函数

`__int__`用于`int()`
`__float__`用于`float()`

### @property

```python
def get_score(self):
    return self.__score
def set_score(self,score):
    if score < 0 or score >100:
        raise ValueError('invalid score')
    self.__score = score
    
s = Student('Bob',59)
s.set_score(60)
```

为了简化属性的get/set 引入了`@property`和`@attribute.setter`

```python
@property
def score(self):
    return self.__score
@score.setter
def score(self,score):
    if score < 0 or score > 100:
        raise ValueError('invalid score')
    self.__score = score

s = Student('Bob',59)
s.score = 60
```

如果没有定义`set`方法，可以创建一个只读属性

### \_\_slots\_\_  

由于python是动态语言，任何实例运行时都可以动态添加属性，如果要限制属性，就要用到`__slots__`  

### \_\_call\_\_  

为类实现一个`__call__()`则，类的实例可以被调用

