# -*-coding:UTF-8 -*-

1、新建一个utils然后吧logger文件放进去
2、新建一个logs文件夹
3、打开testcase中你要加入日志的文件，在类定义的前面加
   logger = Logger('TestGoods').getlog()
   其中只改TestGoods（你自己的类名）
4、在代码中的任何位置都可以实施打印，格式如下：
   logger.info('我打开的url地址是' + url)
