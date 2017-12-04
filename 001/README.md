## 001 计算文件的 crc32，md5，sha


### 文件

- [x] [drop.py](drop.py)
- [x] [md5.py](md5.py)
- [ ] [crc32.py](crc32.py)
- [x] [sha1.py](sha1.py)
- [x] [sha256.py](sha256.py)
- [x] [drop_handle_for_python_file.reg](drop_handle_for_python_file.reg "为Python文件注册DropHandle")
- [x] [drop_handle_not_for_python_file.reg](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

---

### 难点：拖动文件到 python 脚本中作为输入参数

[请参考这篇文章](http://blog.csdn.net/eijnew/article/details/6695271/)

默认情况下，我们无法拖放一个文件给 python 脚本让其去处理这个文件，这是因为 Windows 认为 python 脚本不是一个合法的可拖放的目的对象（drop target）

为了实现拖放目的，请执行 [drop_handle_for_python_file.reg](drop_handle_for_python_file.reg "为Python文件注册DropHandle")  
撤销注册表更改，请执行 [drop_handle_not_for_python_file.reg](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

> 注册表的生效可能需要重启资源管理器

写入注册表后，可以将 [sha1.py](sha1.py) 拖放到 [drop.py](drop.py) 进行测试
```text
        type:  <class 'list'>
         len:  2
         str:  ['D:\\库\\GitHub\\Python-projects\\001\\drop.py', 'D:\\库\\GitHub\\Python-projects\\001\\sha1.py']
 Current_URL:  D:\库\GitHub\Python-projects\001\drop.py
Distinct_URL:  D:\库\GitHub\Python-projects\001\sha1.py
Press <enter>
```

> TODO: 当前逻辑还不能处理引号和斜杠的问题

### 重点：计算文件的 crc32，md5，sha

计算 md5 和 sha 需要 `import hashlib`  
计算 crc32 需要 `import zlib`

下面逐个介绍常用 function

#### 函数：cls()

在与 python 脚本交互的时候，常常需要清除 console，这时候你需要一个 cls() 函数

```python
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
```

#### 函数：get_file_url()

通过检查传参 `sys.argv`，返回文件的 url 路径

```python
import sys


def get_file_url():
    if len(sys.argv) != 2:
        file_url = input("Please input the file URL:")
        return file_url
    else:
        return sys.argv[1]
```

> `sys.argv` 是一个列表类型的值

#### 函数：get_sha1()

接受文件的路径名，返回字符串类型的 sha1 值

```python
import hashlib


def get_sha1(file_url):
    sha1 = hashlib.sha1()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        sha1.update(buffer)
    file.close()
    return sha1.hexdigest()
```

> 路径名的输入不能带有引号

#### 函数：get_md5()

```python
import hashlib

def get_md5(file_url):
    md5 = hashlib.md5()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        md5.update(buffer)
    file.close()
    return md5.hexdigest()
```


