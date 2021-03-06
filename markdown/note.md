#Note for Markdown Language  
##换行  
1. 两个空格然后回车
2. 两个回车  

想通过换行退出列表需要两个回车  
连续的两个标题只需要一个回车不需要空格  
正常文字的换行可以通过两个空格一个回车或者两个回车
##标题  
###类Setext形式  
1. 	标题一级
	========
2.	标题二级
	--------  

###类atx形式
1.	#这是一级标题#可以不闭合
2.	##这是二级标题
3.	###这是三级标题  

##区块引用  
在每行的最前面用`>`来引用，在引用内部换行用两个空格加回车，通过回车摆脱引用用两个回车  
##列表  
1.	无序列表采用**星号**、**加号**、**减号**作为列表标记
2.	有序列表采用**数字**加上一个英文句点  
3.	换行对列表来说无所谓，只需要一个回车  

##代码区块  
缩进4个空格和一个制表符
还可以用三个\`来包裹代码块，并且在开头标注代码的语言类别并回车
##分隔线  
在一行中用三个以上的`星号`、`减号`和`底线`来建立一个分隔线中间可以插入空格  
##链接  
###*行内式的链接*  
1. 在方块括号后紧接着圆括号并插入网址链接即可  
    [This Link](http://www.baidu.com/) has no title attribute.
2. 加入title文字，直接在括号后里最后用双引号标出  
    This is [an example](http://www.baidu.com/ "百度") inline link.
3. 如果链接到同主机资源可以使用相对路径  

###*参考式的链接*
1. 添加一个方括号
2. 接着在文件的任意处，把标记的链接内容定义出来  
```c
	This is [an example][id] reference-style link.
	[id]: http://www.baidu.com/ "title"
	or:
	[id]: http://www.baidu.com/ (title)
	or:
	[id]: http://www.baidu.com/ 'title'   
```
This is [an example][1] reference-style link.
[1]: http://www.baidu.com (百度)  
##强调  
1. 用一个星号或者下划线包围  
	*single asterisks*  
	_single underscores_
2. 用两个星号或者下划线包围  
	**double asterisks**  
	__double underscores__  

##行内代码  
用反引号将行内的代码包裹起来，例如:`printf()`  
##图片  
和链接类似  
1. 一个感叹号
2. 一个方括号，放入替代文字 alt
3. 接着一个普通括号，将网址放进去，后面还可以跟title

##markdown支持的符号  
1. \
2. `
3. _
4. {}
5. []
6. ()
7. .
8. !

---  
需要转义的符号

9. \*
10. \#
11. \+
12. \-    

##自动链接  
用尖括号扩起来的邮箱或者网址，可以自动导航过去  
##快捷键  
1. CTRL + B bold 加粗 `**加粗**`
2. CTRL + H head 提升标题 `##标题`
3. CTRL + I italic 斜体  `*斜体*`
4. CTRL + S 删除线   `~~删除线~~`
5. CTRL + Q quote 引用   `>引用`
6. CTRL + R 水平尺 `---换行`
