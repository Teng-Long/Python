## Python 编码知识点

### 从基础讲起

#### BCD 码

    二进码十进数（Binary-Coded Decimal，BCD）
    
    常见的有以4位表示1个十进制数字，称为压缩的BCD码（compressed or packed）  
    或者以8位表示1个十进制数字，称为未压缩的BCD码（uncompressed or zoned）

#### ASCII 码

    ASCII（/ˈæski/，American Standard Code for Information Interchange）是基于拉丁字母的一套电脑编码系统
    
    ASCII 码一共规定了128个字符的编码  
    这128个符号（包括32个不能打印出来的控制符号），只占用了一个字节的后面7位，最前面的一位统一规定为0。

#### Unicode

    一个byte并不能将世界上不同国家的文字和符都囊括在内。  
    这时就出现了各种个样的编码标准。  
    最为普遍的编码标准是unicode，它把一个文字，符号按照最多4个byte来编码

#### UTF-8

    UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，也是一种前缀码。
    
    UTF-8 是 Unicode 的实现方式之一
    
    它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容

#### Little endian 和 Big endian

    第一个字节在前，就是"大头方式"（Big endian），第二个字节在前就是"小头方式"（Little endian）
    
    Unicode 规范定义，每一个文件的最前面分别加入一个表示编码顺序的字符，这个字符的名字叫做"零宽度非换行空格"（zero width no-break space），用FEFF表示。这正好是两个字节，而且FF比FE大1。
    
    如果一个文本文件的头两个字节是FE FF，就表示该文件采用大头方式；如果头两个字节是FF FE，就表示该文件采用小头方式。

---

### 查看编码

Linux 上有个查看本地话的工具：locale

    LANG="en_US.UTF-8"                  # 它的值用于指定下面环境变量没有设置的所有变量值。如果指定了上面任何一个变量的值，则会废除对应的LANG值的缺省设置。
    LC_CTYPE="zh_CN.UTF-8"              # 用于字符分类和字符串处理，控制所有字符的处理方式，包括字符编码，字符是单字节还是多字节，如何打印等。
    LC_NUMERIC="en_US.UTF-8"            # 指定使用某区域的非货币的数字格式
    LC_TIME="en_US.UTF-8"               # 指定使用某区域的日期和时间格式
    LC_COLLATE="en_US.UTF-8"            # 指定使用某区域的排序规则
    LC_MONETARY="en_US.UTF-8"           # 指定使用某区域的货币格式
    LC_MESSAGES="en_US.UTF-8"           # 用于控制程序输出时所使用的语言，主要是提示信息，错误信息，状态信息， 标题，标签， 按钮和菜单等。
    LC_PAPER="en_US.UTF-8"              # 指定使用某区域的纸张大小
    LC_NAME="en_US.UTF-8"               # 指定使用某区域的姓名书写方式
    LC_ADDRESS="en_US.UTF-8"            # 指定使用某区域的地址格式和位置信息
    LC_TELEPHONE="en_US.UTF-8"          # 指定使用某区域的电话号码格式
    LC_MEASUREMENT="en_US.UTF-8"        # 指定使用某区域的度量衡规则
    LC_IDENTIFICATION="en_US.UTF-8"     # 对 locale 自身信息的概述
    LC_ALL=                             # 它不是环境变量，只是一个宏，可使用setlocale设置所有的LC_*环境变量。这个变量设置之后，可以废除LC_*和LANG的设置值，使得这些变量的设置值与LC_ALL的值一致。

通过 Python 也可以查看

    [root@jason ~]# python -c "import sys;print sys.stdout.encoding"
    UTF-8

查看 Windows 使用的编码

    C:\Users\Jason>chcp
    活动代码页: 936

---

### 拓展阅读

字符编码笔记：ASCII，Unicode 和 UTF-8 http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html

Python字符编码详解 http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html

哇，原来python字符串是这样的！https://www.jianshu.com/p/4f0e65bee38b

Python2与Python3的字符编码与解码 https://www.jianshu.com/p/19c74e76ee0a?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

python与编码 http://www.cnblogs.com/jessonluo/p/4801580.html




