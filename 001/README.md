## 001 Calculate crc32, md5 and sha

### File list

- [x] [drop.py](drop.py)
- [x] [md5.py](md5.py)
- [x] [crc32.py](crc32.py)
- [x] [sha1.py](sha1.py)
- [x] [sha256.py](sha256.py)

---

### 难点

:o: ***拖动文件到 python 脚本中作为输入参数***

将多个文件拖放到 [drop.py](drop.py) 进行测试

```text
       file0:  D:\库\GitHub\Python-projects\001\README.md
       file1:  D:\库\GitHub\Python-projects\001\sha1.py
       file2:  D:\库\GitHub\Python-projects\001\sha256.py
       file3:  D:\库\GitHub\Python-projects\001\crc32.py
       file4:  D:\库\GitHub\Python-projects\001\drop_handle_for_python_file.reg
       file5:  D:\库\GitHub\Python-projects\001\drop_handle_not_for_python_file.reg
       file6:  D:\库\GitHub\Python-projects\001\md5.py


Press <enter>
```

:warning: 当前逻辑还不能处理斜杠的问题

---

### 用到的 function

- [清屏：cls()](#cls)
- [获取文件的路径：get_file_url()](#get_file_url)
- [计算 sha：get_sha1()](#get_sha1)
- [计算 md5：get_md5()](#get_md5)
- [计算 crc32：get_crc32()](#get_crc32)
- [去除路径两端的引号：remove_quotes()](#remove_quotes)



#### cls()

在与 python 脚本交互的时候，常常需要清除 console，这时候你需要一个 cls() 函数

```python
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
```

#### get_file_url()

通过检查传参 `sys.argv`，返回多个文件的 url 路径，返回值为列表类型，列表值为字符串类型

```python
import sys


def get_file_url():
    if len(sys.argv) == 1:
        file_name = input("Please input the file URL:")
        return [file_name]
    elif len(sys.argv) == 2:
        return [sys.argv[1]]
    else:
        return sys.argv[1:]
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

&nbsp;<details><summary>:notebook_with_decorative_cover: 写法二</summary>
```python
from hashlib import sha1


def get_sha1(file_url):
    sha1_object = sha1()
    with open(file_url, 'rb') as f:
        sha1_object.update(f.read())
    return sha1_object.hexdigest()
```
&nbsp;</details>
&nbsp;

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
from zlib import crc32


def get_crc32(file_url):
    with open(file_url, 'rb') as file_object:
        return crc32(file_object.read())
```

#### remove_quotes()

```python
def remove_quotes(string_object):
    return string_object.strip('"')
```

