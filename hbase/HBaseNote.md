# HBaseNote

Tags: 笔记 HBase

---

##Zookeeper的安装
`yum install zookeeper`

增加目录
`/usr/lib/zookeeper/`  -软件安装目录 
`/etc/zookeeper/conf`  -配置文件目录

设置`/etc/zookeeper/conf/zoo.cfg`

其他的可以适当修改，增加
`server.X = A:B:C`
X是一个数字, 表示这是第几号server.
A是该server所在的IP地址.
B配置该server和集群中的leader交换消息所使用的端口.
C配置选举leader时所使用的端口

然后在每个机器的dataDir中创建文件myid,将本机的X写入到该文件中


最后依次启动`/usr/lib/zookeeper/bin/zkServer.sh start`

##Hbase的安装
`yum install hbase`
如果需要服务的话
master机另外安装`yum install hbase-master`
slave机另外安装`yum install hbase-regionserver`

###配置文件如下 /etc/hbase/conf/hbase-site.xml
```xml
        <property>
                <name>hbase.rootdir</name>
                <value>hdfs://computer1:8020/hbase</value>
                <description>hbase在hdfs上的数据存放目录</description>
        </property>
        <property>
                <name>hbase.cluster.distributed</name>
                <value>true</value>
                <description>是否开启分布式集群模式</description>
        </property>
        <property>
                <name>hbase.zookeeper.quorum</name>
                <value>computer2,computer3,computer4</value>
                <description>Zookeeper集群的hostname</description>
        </property>
        <property>
                <name>hbase.tmp.dir</name>
                <value>/var/lib/hbase/tmp/</value>
                <description>hbase临时文件的目录</description>
        </property>
```

###启动遇到问题

 `Permission denied:user=hbase,access=WRITE,inode="/":root:supergroup:drwxr-xr-x`
 hbase用户没权限在hadoop上创建目录
 
 在hdfs上建立hbase用户
 1. hdfs启动用户执行 `hadoop dfs -mkdir /user/hbase` 
 2. 更改`/user/hbase`的权限 `hadoop dfs -chown -R hbase:hbase /user/hbase` 这样`/user/hbase`的权限为用户`hbase`组`hbase`
 `hadoop dfs -chown -R hbase /user/hbase` 这样`/user/hbase`的权限为用户`hbase`组`supergroup`

在hdfs`/`上创建`/hbase`
`hadoop dfs -mkdir /hbase`

将`/hbase`的权限改为`hbase:hbase`
`hadoop dfs -chown -R hbase:hbase /hbase`


---
`Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/hadoop/hbase/protobuf/generated/MasterProtos$MasterService$BlockingInterface`用`hadoop jar`执行hbase java api 程序时出现的一系列的`NoClassDefFoundError`

原因是没有引入hbase的classpath，

方法
1. 将hbase的依赖jar包全部复制到hadoop/lib/下

    cp /home/hbase/lib/hbase-*.jar /home/hadoop/share/hadoop/common
    cp /home/hbase/lib/htrace-*.jar /home/hadoop/share/hadoop/common
    cp /home/hbase/lib/high-scale-lib-1.1.1.jar /home/hadoop/share/hadoop/common
    cp /home/hbase/lib/metrics-core-2.2.0.jar /home/hadoop/share/hadoop/common
    cp /home/hbase/conf/hbase-site.xml /home/hadoop/etc/hadoop

注：以上包均为必须jar包。如果没有`high-scale-lib-1.1.1.jar`和`metrics-core-2.2.0.jar`Hadoop只可以将mapreduce导入hbase，但是无法使用`TableMapReduceUtil`将hbase导入mapreduce.
2. 修改`hadoop-env.sh`添加hbase的classpath
在`hadoop-env.sh`中添加``export HADOOP_CLASSPATH = ${HADOOP_CLASSPATH}:`hbase classpath` ``  
**此方法消耗内存大**
   
 

#HBase Java Coding

创建或修改表DDL

```java
Configuration conf = HBaseConfiguration.create();
conf.set(HConstants.ZOOKEEPER_QUORUM,"hostname");
conf.setInt(HConstants.ZOOKEEPER_CLIENT_PORT,2181);
HBaseAdmin ha = new HBaseAdmin(conf);
TableName name = TableName.valueOf("jnchen");
HTableDescriptor desc = new HTableDescriptor(name);
HColumnDescriptor family = new HColumnDescriptor(Bytes.toBytes("fm1"));
family.setXXXXXXXX;//对列族进行设置
desc.addFamily(family);
desc.setXXXXXXXX;//对表进行设置

ha.createTable();
ha.modifyTable();

ha.close();
```

DML  `delete/exist/get/put/`
```java
HTable table = new HTable(conf,"test_table");
Put put = new Put(ROWKEY);
put.add(FAMILY,COLUMN,TIMESTAME,VALUE);

table.put(PutList|PUT);

Get get = new Get(ROWKEY);
get.addFamily(FAMILY);
get.addColumn(FAMILY,COLUMN);

Result result = table.get(GETLIST|GET);
result.getRow() : Bytes[]
result.getValue(FAMILY,COLUMN) : Bytes[]

//扫描表
Scan scan = new Scan();
scan.addColumn(FAMILY,COLUMN);
scan.setCaching(100);//每次扫描100个
scan.setTimeRange(START,END);
scan.setStartRow(STARTROW);
scan.setStopRow(STOPROW);//HBase rowkey有序
ResultScanner scaner = table.getScanner(scan);
Result result = null;
while((result = scanner.next())!=null){
    result = scanner.next();
    
}

//Delete 操作
Delete delete = new Delete(ROWKEY);
delete.deleteColumn(FAMILY,COLUMN,TIMESTAMP);
table.delete(delete);

//Table.exists
table.exists(GET) :boolean


table.close();

```

