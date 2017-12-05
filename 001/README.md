## 001 Calculate crc32, md5 and sha

[TOC levels=3,4]: # "### Table of Contents"

### Table of Contents
- [File list](#file-list)
- [Skill used](#skill-used)
- [Function Used](#function-used)
    - [cls()](#cls)
    - [get_file_url()](#get-file-url)
    - [get_sha1()](#get-sha1)
    - [get_md5()](#get-md5)
    - [get_crc32()](#get-crc32)

---

### File list

- [x] [drop.py](drop.py)
- [x] [md5.py](md5.py)
- [x] [crc32.py](crc32.py)
- [x] [sha1.py](sha1.py)
- [x] [sha256.py](sha256.py)
- [x] [drop_handle_for_python_file.reg](drop_handle_for_python_file.reg "为Python文件注册DropHandle")
- [x] [drop_handle_not_for_python_file.reg](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

---

### Skill used

***重难点：拖动文件到 python 脚本中作为输入参数***

[请参考这篇文章](http://blog.csdn.net/eijnew/article/details/6695271/)

默认情况下，我们无法拖放一个文件给 python 脚本让其去处理这个文件，这是因为 Windows 认为 python 脚本不是一个合法的可拖放的目的对象（drop target）

为了实现拖放目的，请执行 [drop_handle_for_python_file.reg](drop_handle_for_python_file.reg "为Python文件注册DropHandle")  
撤销注册表更改，请执行 [drop_handle_not_for_python_file.reg](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

:warning: 注册表的生效可能需要重启资源管理器

写入注册表后，可以将 [sha1.py](sha1.py) 拖放到 [drop.py](drop.py) 进行测试
```text
        type:  <class 'list'>
         len:  2
         str:  ['D:\\库\\GitHub\\Python-projects\\001\\drop.py', 'D:\\库\\GitHub\\Python-projects\\001\\sha1.py']
 Current_URL:  D:\库\GitHub\Python-projects\001\drop.py
Distinct_URL:  D:\库\GitHub\Python-projects\001\sha1.py
Press <enter>
```

:warning: 当前逻辑还不能处理引号和斜杠的问题

---

### Function Used

[请参考这篇文章](http://blog.csdn.net/marshall001/article/details/50097705)


计算 md5 和 sha 需要 `import hashlib`  
计算 crc32 需要 `import zlib`

下面逐个介绍常用 function

#### cls()

在与 python 脚本交互的时候，常常需要清除 console，这时候你需要一个 cls() 函数

```python
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
```

#### get_file_url()

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

#### get_sha1()

接受文件的路径名，返回字符串类型的 sha1 值

```python
from hashlib import sha1


def get_sha1(file_url):
    sha1_object = sha1()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        sha1_object.update(buffer)
    file_object.close()
    return sha1_object.hexdigest()
```

&nbsp;<details open><summary>**写法二**</summary>
```python
from hashlib import sha1


def get_sha1(file_url):
    sha1_object = sha1()
    with open(file_url, 'rb') as f:
        sha1_object.update(f.read())
    return sha1_object.hexdigest()
```
&nbsp;</details>

> 篇幅有限，`get_sha256()` 和 `get_sha512` 不再列出

> 路径名的输入不能带有引号

#### get_md5()

```python
import hashlib

def get_md5(file_url):
    md5_object = hashlib.md5()
    file_object = open(file_url, 'rb')
    while True:
        buffer = file_object.read(8096)
        if not buffer:
            break
        md5_object.update(buffer)
    file_object.close()
    return md5_object.hexdigest()
```

#### get_crc32()

```python
import zlib


def get_crc32(file_url):
    crc32_object = zlib.crc32()
    file = open(file_url, 'rb')
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        crc32_object.update(buffer)
    file.close()
    return crc32_object
```
&nbsp;<details open><summary>写法二</summary>
```python
from zlib import crc32


def get_crc32(file_url):
    with open(file_url, 'rb') as f:
        return crc32(f.read())
```
&nbsp;</details>


