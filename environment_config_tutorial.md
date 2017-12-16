## Python 多版本开发环境配置

### 下载安装包

:o: 你需要的安装包有：

    Anaconda3-5.0.1-Windows-x86_64.exe
    Git-2.15.1.2-64-bit.exe
    pycharm-professional-2017.3.1.exe
    python-2.7.14.amd64.msi
    python-3.6.3-amd64.exe
    setupssh-7.6p1-1.exe

:o: 官方下载地址：

    https://repo.continuum.io/archive/
    https://www.python.org/ftp/python/
    https://www.jetbrains.com/pycharm/download/#section=windows
    https://git-scm.com/downloads
    http://www.mls-software.com/opensshd.html

### 安装

:o: 安装 Git

安装选项不作要求，我们要的是安装目录下的 `bin\git.exe`

我修改了安装路径：`C:\MyProgram\Git`

:o: 安装 OpenSSH

安装选项不作要求

:o: 安装 Anaconda

安装时 ***不要*** 勾选 `Add to Path`

我修改了安装路径：`C:\Users\Jason\Anaconda3`

:o: 安装 Python 2.7

安装时 ***不要*** 勾选 `Add to Path`

我修改了安装路径：`C:\Users\Jason\Python\Python27`

:o: 安装 Python 3.6

安装时 ***不要*** 勾选 `Add to Path`

***请*** 勾选 `Python Launcher` 和 `Associate .py`

我修改了安装路径：`C:\Users\Jason\Python\Python36`

:o: 安装 Pycharm

正常安装，使用高校的学生邮箱激活

### 配置

:o: 修改注册表（不完整）

1. 将 `.py` 注册为 `Python.File`
2. 定位到 `HKEY_CLASSES_ROOT\Python.File`
3. 修改 `DefaultIcon\@` 为 `"C:\WINDOWS\py.exe",0`
4. 修改 `Shell\editwithidle\shell\edit27\MUIVerb` 为 `Edit with IDLE 2.7 (64-bit)`
5. 修改 `Shell\editwithidle\shell\edit27\command\@` 为 `"C:\Users\Jason\Python\Python27\pythonw.exe" "C:\Users\Jason\Python\Python27\Lib\idlelib\idle.pyw" -e "%1"`
6. 删除 `idle2.7`
7. 修改 `Shell\open\command\@` 为 `"C:\Windows\py.exe" "%1" %*`

:o: 刷新/重启资源管理器，并运行测试脚本

双击运行即可

[python 2.py](python_2.py)

    2.7.14
    
    Press <Enter>

[python3.py](python_3.py)

    3.6.3
    
    Press <Enter>

### 使用

:o: 通过 shebang 选择 python 解释器

有四种语法，默认选择 python2 最新版本，python2 代表 python2 最新版本，python3 代表 python3 最新版本，python3.6 代表 python3.6.x

    #! /usr/bin/env python*
    #! /usr/bin/python*
    #! /usr/local/bin/python*
    #! python*

:o: 通过 command-line 指定 python 解释器

语法如下

    py -2 hello.py
    py -3 hello.py
    py -3.6 hello.py

