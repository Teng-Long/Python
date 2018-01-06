## Python3 规范

### 编码

:o: 字符编码声明

源代码文件中，如果有用到非ASCII字符，则需要在文件头部进行字符编码的声明，有多种写法：

    # -*- coding: utf-8 -*-
    # coding: utf-8

:o: 根据用途采用不同类型的字符串

    Python3 有两种不同的字符串：
    一个用于存储文本，使用 Unicode 存储
    一个用于存储原始字节，显示为 ASCII
    
    python3中，文本型字符串类型被命名为str，字节字符串类型被命名为bytes
    
    正常情况下，实例化一个字符串会得到一个str实例
    如果希望得到一个bytes实例，需要在文本之前添加 b 字符
    
    str类包含一个encode方法，用于使用特定编码将其转换为一个bytes
    bytes类包含一个decode方法，接受一个编码作为单个必要参数，并返回一个str
    
    python3中永远不会尝试隐式地在一个str与一个bytes之间进行转换，需要显式使用str.encode 或者 bytes.decode方法

:warning: Python2 中 str 类是一个字节字符串  
:warning: Python2 会在文本字符串和字节字符串之间尝试进行隐式转换

:o: 根据情况使用 codecs.open() 替代内置的 open()

    内置的open()方法打开文件时，read()读取的是str，读取后需要使用正确的编码格式进行decode()
    
    write()写入时，如果参数是unicode，则需要使用你希望写入的编码进行encode()
    如果是其他编码格式的str，则需要先用该str的编码进行decode()，转成unicode后再使用写入的编码进行encode()
    如果直接将unicode作为参数传入write()方法，Python将先使用源代码文件声明的字符编码进行编码然后写入。

---

    模块codecs提供了一个open()方法，可以指定一个编码打开文件，使用这个方法打开的文件读取返回的将是unicode
    写入时，如果参数是unicode，则使用open()时指定的编码进行编码后写入
    
    如果是str，则先根据源代码文件声明的字符编码，解码成unicode后再进行前述操作
    
    相对内置的open()来说，这个方法比较不容易在编码上出现问题

:o: 绝对需要避免使用的字符编码：MBCS/DBCS和UTF-16

    这里说的MBCS不是指GBK什么的都不能用，而是不要使用Python里名为'MBCS'的编码，除非程序完全不移植。
    
    Python中编码'MBCS'与'DBCS'是同义词，指当前Windows环境中MBCS指代的编码
    Linux的Python实现中没有这种编码，所以一旦移植到Linux一定会出现异常！
    
    另外，只要设定的Windows系统区域不同，MBCS指代的编码也是不一样的




