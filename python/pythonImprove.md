# Python improve

��ǩ���ո�ָ����� Python �ʼ�

---

##�߽׺���  

���Խ�������Ϊ�����Ĳ���

 **map()����**

����һ������f��һ��list���Ѻ���f����������list��ÿ��Ԫ���ϣ��õ�һ���µ�list������  
����ԭ�� `map(function,list)`

```python
def f(x):
    return x * x
print map(f,range(1,10))
Result:[1,4,9,16,25,36,49,64,81]
```

**reduce()����**

����һ������f��һ��list��������ĺ���f�����������������reduce()��list��ÿ��Ԫ�ط������ú���f�����������ս��ֵ  
reduce()���������Դ�������������������˼���ĳ�ʼֵ������һ��ִ��f�����ʼֵ��list��һ��Ԫ��  
����ԭ�� `reduce(function,list)`

 **filter()����**

����һ������f��һ��list������f�������Ƕ�ÿ��Ԫ�ؽ����жϣ�����True��False��filter()�����жϽ���Զ����˵�������������Ԫ�أ������ɷ�������Ԫ����ɵ���list  
����ԭ�� `filter(function,list)`

 **sorted()����**

����һ���ȽϺ�����ʵ���Զ������򣬱ȽϺ����Ķ����ǣ������������Ƚϵ�Ԫ��x��y�����xӦ������yǰ�棬����-1�����xӦ������y���棬����1��x��y��ȷ���0  
����ԭ�� `sorted(list,function)`

---

## �հ�

�ڲ㺯����������㺯���ı���(����Ҳ�����),Ȼ�󷵻��ڲ㺯�����������Ϊ�հ�(Closure)  
�ص�:���صĺ�����������㺯���ľֲ����������ԣ�Ҫ��ȷʹ�ñհ�����Ҫȷ�����õľֲ������ں������غ��ܱ䡣
  
ͨ�׽������ڲ������������ⲿ�ܹ�����ʹ��

```python
//����
#ϣ��һ�η���3���������ֱ����1**2 2**2 3**2
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
//fs���غ�i��ֵ���Ϊ3

//����
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

#��������  

�ؼ���lambda��ʾ��������

```python
def f(x):
    reutrn x*x
//�ȼ���
lambda x:x*x
```

---

## decorator  

�����Ͼ���һ���߽׺���������Ĳ����ʹ����Ĳ�����Ϊ�������Դ���ĺ������а�װ�Ժ�return  

```python
def log(f):
    def fn(x): #��������ǵ���return���������
        print 'log call %s'%f.__name__
        return f(x)
    return fn
    
def func(x):
    print x
//////////////////////////
f = new log(func)
f()
//���������ͨ���ں���ǰ@log����
@log
def func():
    print x
    
func()


//����������ĺ���������
def log(f):
    def fn(*args,**kw):
        print 'call %s()'%f.__name__
        return f(*args,**kw)
    return fn
    
```

## ������decorator  

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
#��ʱ��test�����Ѿ�����˶��ڲ�fn������
//
//
#Ϊ�˱������test������������functoolsģ���е�wraps������ԭ������__name__,__doc__
//��
def log(f):
    def wrapper(*args,**kw):
        print 'call...'
        return f(*args,**kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
//���
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print 'call...'
        return f(*args,**kw)
    return wrapper

```

---

## ƫ����  
functools.partial����

```python
//python 2.x
import functools
sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.supper()))

sorted_ignore_case(list)

///����ƫ����ʵ�� python2.x
sorted(list,cmp=lambda x,y:cmp(x.upper(),y.upper()))

```

---

## ����ģ��  

```python
import moduleName  
#�����ڳ�ͻ����Ҫͨ��ģ�������ú���/����

from moduleName import attribute/method
#�п��ܴ��ڳ�ͻ

from moduleName import attr/method as alias
#moduleName�е�attr/method�����alias
```

�������ģ�鲻���ڣ�Python�ᱨImportError����  
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

python�°汾�Ĺ��ܻ����ϰ汾��`__future__`���д��ڣ����Ե���`__future__`ģ���������á�

---

## ��װ������ģ��  
###pip  
����pip��
python setup.py install
pip install web.py

---

# ���������

## �����ࡢ������ʵ��
class �ؼ��ֶ����࣬ͨ���Դ�д��ĸ��ͷ��Ȼ����`(object)`�������Ǵ��ĸ���̳�����  
������ʵ��: ʹ��`����+()`

## ����ʵ������  
����ʵ����ֱ�Ӷ����Ը�ֵ����

```python
xiaoming = Person()
xiaoming.name = 'XiaoMing'
xiaoming.age = 22
xiaoming.gender = 'Male'
```

## ��ʼ��ʵ������  
���ڴ���ʱӦ����һЩ������ʵ��ͨ�õ�����  
�ڶ�����ʱ������һ�������`__init__()`����,�÷������ڴ���ʵ��ʱ�Զ�������  
`__init__()`�����ĵ�һ������������*self*(Ҳ�����ñ�����֣�ϰ���÷���self)  
�ڴ���ʵ��ʱ�������ṩ����*self*֮��Ĳ���  

## ���ʿ���  
���һ��������˫�»��߿�ͷ�������Ծ��޷��������� 

## ������  
ʵ�����Բ���Ӱ������ʵ����ÿ��ʵ������ӵ�У��������  
�����ԣ���һ����������ʵ��������ֻ��һ��   
������ͨ��**`����.������`**ֱ�ӷ���

��ʵ�����Ժ�����������ʱ��ʵ���������ȼ���  
*�ɼ�����Ҫ��ʵ�����޸������ԣ�ʵ���ϲ�û���޸������ԣ� ���Ǹ�ʵ������һ��ʵ������*

## ʵ������  
�����ж���ĺ��������ĵ�һ��������Զ����`self`��ָ����ø÷�����ʵ����������������һ����ͨ��������ȫһ����  

����Ҳ��һ�����ԣ����Զ�̬����ӵ�ʵ���ϣ�����Ҫ��types.MethodType()��һ��������Ϊһ������:
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
# ��Ϊp2ʵ����û�а�get_grade
```

���������ø������ԣ�Ҳ����Ϊʵ�����ӷ����������Ͱ󶨷�����ͬ�����ô���self

## �෽��  

�෽��������ʵ����ֱ��������  
ͨ�����`@classmethod`����һ�������󶨵����ϣ��෽���ĵ�һ������������`������Լ�`��ͨ����ȡ�����ԣ��޷����ʵ��������  

---

## �̳�  

�̳�ʵ����is��ϵ
has��ϵ�������ʵ�� (���е�����)  

### python�̳е��ص�

���Ǵ�ĳ����̳�
��Ҫ���ǵ���`super().__init__`  
```python
#�����__init__
def __init__(self,args):
    super(SubClass,self).__init__(args)
```

### �ж�ʵ��������

`isinstance(obj,Type)`����obj�Ƿ���Type��ʵ��

### ���ؼ̳�  

**���ؼ̳е�Ŀ��**�Ǵ����ּ̳����зֱ�ѡ�񲢼̳г����࣬�Ա���Ϲ���ʹ��  

### ��ȡ������Ϣ

`type()`     ��ȡ����������`type(arg)`
`dir()`      ��ȡ��������������`dir(arg)`
`getattr()`  ��ȡ����`getattr(arg,name)`
`setattr()`  ��������`setattr(arg,name,value)`  

---

## ���ⷽ��  

����java `toString()`�ķ���`__str__()`����print��ʱ����Զ����ø�ʵ����`__str__()`  

����`print()`��`__str__()`
����`len()`��`__len__()`
����`cmp()`��`__cmp__()` 2.x

�ص㣺  
���ⷽ��������class��
����Ҫֱ�ӵ���Python��ĳЩ�������������������Ӧ�����ⷽ��  

��ôʵ�֣�  
ֻ��Ҫ��д�õ������ⷽ��  
�й����Ե����ⷽ��������ʵ�� `__getattr__` `__setattr`

### \_\_str\_\_

��java��toString 
`__repr__`��������������ֱ�Ӵ�ӡtoString������print

### \_\_len\_\_  

ʵ����`__len__`�Ϳ�����`len()`��������ʵ�������ȡ�

### \_\_add\_\_

ʵ����`__add__`�Ϳ�����`+`����������

### \_\_sub\_\_

ʵ����`__sub__`�Ϳ�����`-`�����м�����

ʵ����`__mul__`�Ϳ�����`*`�����г�����

ʵ����`__div__`�Ϳ�����`/`�����г����� 2.x

ʵ����`__truediv__`������`/`�����г����� 3.x
ʵ����`__divmod__`������`//`�������������� 3.x

ʵ����`__mod__`������`%`������ȡ������

### ����ת�����⺯��

`__int__`����`int()`
`__float__`����`float()`

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

Ϊ�˼����Ե�get/set ������`@property`��`@attribute.setter`

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

���û�ж���`set`���������Դ���һ��ֻ������

### \_\_slots\_\_  

����python�Ƕ�̬���ԣ��κ�ʵ������ʱ�����Զ�̬������ԣ����Ҫ�������ԣ���Ҫ�õ�`__slots__`  

### \_\_call\_\_  

Ϊ��ʵ��һ��`__call__()`�����ʵ�����Ա�����

