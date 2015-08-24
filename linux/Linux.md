#Linux 小命令笔记

##Shell 常用快捷键

|按键|作用|
|:---|:------|
|`Ctrl+D`|键盘输入结束或者退出终端|
|`Ctrl+S`|暂停当前程序，暂停后按下任意键恢复运行|
|`Ctrl+Z`|将当前程序放到后台运行，恢复到前台命令为fg,查看前后台程序jobs|
|`Ctrl+A`|将光标移动至输入行头，相当于`HOME`键|
|`Ctrl+E`|将光标移动至输入行末，相当于`END`键|
|`Ctrl+K`|删除从光标所在位置到行末|
|`Alt+BACKSPACE`|向前删除一个单词|
|`Shift+PgUp`|将终端显示向上滚动|
|`Shift+PgDn`|将终端显示向下滚动|

##Shell 常用通配符  

|字符|含义|
|:----|:-----|
|`*`|匹配0或多个字符|
|`?`|匹配任意一个字符|
|`[list]`|匹配list中任意单一字符|
|`[!list]`|匹配除list中的任意单一字符以外的字符|
|`c1-c2`]|匹配c1-c2中的任意单一字符 如:[0-9][a-z]|
|`{string1,string2,...}`|匹配string1或string2(或更多)其一字符串|
|`{c1..c2}`|匹配c1-c2中全部字符 如{1,10}|

## `who`命令  

|参数|说明|
|----|----|
|`-a`|打印能打印的全部|
|`-d`|打印死掉的进程|
|`-m`|和`am i` , `mom likes`相同|
|`-q`|打印当前登录用户数及用户名|
|`-u`|打印当前用户登录信息|
|`-r`|打印运行等级|

## Linux文件类型  

`d` 目录
`l` 软链接
`b` 块设备
`c` 字符设备
`s` socket
`p` 管道
`-` 普通文件

## Linux文件权限   
 
一个目录要同时具有读权限和执行权限才可以打开，而一个目录要有写权限才允许在其中创建其它文件 

## Linux目录

<table>
    <tr>
        <th></th>
        <th>可分享的(shareable)</th>
        <th>不可分享的(unshareable)</th>
    </tr>
    <tr>
        <td rowspan="2">不可变的(static)</th>
        <td>/usr(软件放置处)</td>
        <td>/etc(配置文件)</td>
    </tr>
    <tr>
        <td>/opt(第三方软件)</td>
        <td>/boot(开机及内核文件)</td>
    </tr>
    <tr>
        <td rowspan="2">可变动的(variable)</td>
        <td>/var/mail(用户邮件信箱)</td>
        <td>/var/run(程序相关)</td>
    </tr>
    <tr>
        <td>/var/news(新闻组)</td>
        <td>/var/lock(文件锁相关)</td>
    </tr>
</table>

