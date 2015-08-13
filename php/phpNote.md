#The Note of PHP langage

Tags： 笔记 PHP

---

##PHP的8种原始数据类型  
PHP是弱类型语言，声明时通常不需要程序员指定类型
使用伪变量`$`+`变量名称`作为变量的声明
1. Boolean 布尔型
2. Integer 整型
3. Float   浮点型
4. String  字符串
5. Array   数组
6. Object  对象
7. Resource资源
8. NULL    无类型  

---

##PHP的array类型
php的array实际上是一个有序的映射，是把values关联到keys的类型
可以当做数组，列表，散列表，字典，集合，栈等
用作散列表:
```PHP
<?php
$myMap = array(key => value，...);
//key 可以是integer 和string
//value 可以是任意类型的值
?>

//以上方式可以简写为
<?php
$myMap = [key=>value,...];
?>
```

---

##PHP的Resource类型
保存了到外部资源的一个引用，如一个文件，数据库连接，图形画布区域等的句柄

---

##PHP的Calback回调类型
PHP可以将string类型的函数名执行
```PHP
function func1(){
    echo "i'm func1";
}
class class1{
    static function func2(){
        echo "i'm func2";
    }
}
//回调普通函数
call_user_func('func1');
//回调静态对象的函数
call_user_func(array('class1','func2'));
```

---

##PHP变量
默认是传值赋值，也可以引用赋值
```PHP
$arg1 =150;
$arg2 = &$arg1;
$arg1 = 120;
echo $arg2;
```

---

##PHP变量范围
函数内如果想引用函数外的变量，必须在前面将改变量声明为`global` 类似于C语言的`extern`

---

##可变变量
```PHP
$var1 = 'var_name';
$$var1 = 25;
//此时，$var1将与'var_name'代换
//$$var1 相当于$var_name
echo $var_name;
```

---

##PHP的常量
1. 常量前没有$
2. 常量只能用`define()`函数来定义
   类定义之外可以用`const`关键字定义常量
3. 常量不像变量作用域，可以在任何地方定义和访问
4. 常量一旦定义就不能被重新定义或取消定义
5. 常量的值只能是标量
6. 如果常量名是动态的，可以用`constant()`来获取常量的值
7. 可以用`get_defined_constants()`来获得所有已定义的常量列表
##运算符优先级
| 结合方向 | 运算符 | 类别 |
|:---------:|:-------:|:-----:|
| 无 | clone new | clone和new |
|左|[|array()|
|右|!|逻辑运算符|
|无|instanceof|类型|
|左|\* / % |算术运算符|
|左|\+ \- .|算术运算符和字符串运算符|
|左|<< >>|位运算符|
|左|&|位运算符和引用|
|左|^|位运算符|
|左|&&|逻辑运算符|
|左|?:|三元运算符|
|无|== != === !== <>|比较运算符|
|右|++ -- ~ (int) (float)|类型和递增/递减|
|左|and|逻辑运算符|
|左|xor|逻辑运算符|
|左|or|逻辑运算符|
|左|,|多处用到|


---
