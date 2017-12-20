## centos7 编译安装 python3.6

:o: 查看 CentOS 版本

    [jason@test ~]$ cat /etc/redhat-release
    CentOS Linux release 7.4.1708 (Core)

:o: 下载源码包

    [jason@test ~]$ curl -JkLO https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 16.2M  100 16.2M    0     0  2449k      0  0:00:06  0:00:06 --:--:-- 2329k

:o: 安装必要的包

    [jason@test ~]$ sudo yum install gcc make zlib-devel readline-devel openssl-devel

:o: 安装可选的包

    [jason@test ~]$ sudo yum install bzip2-devel ncurses-devel sqlite-devel gdbm-devel xz-devel tk-devel

:o: 编译安装（安装到 /home/jason）

    [jason@test ~]$ tar -Jxf Python-3.6.4.tar.xz
    [jason@test ~]$ cd Python-3.6.4
    [jason@test Python-3.6.4]$ ./configure --prefix=/home/jason/
    [jason@test Python-3.6.4]$ make
    [jason@test Python-3.6.4]$ make install

:o: 编译安装（安装到 /usr/local/python3.6）

    [jason@test ~]$ tar -Jxf Python-3.6.4.tar.xz
    [jason@test ~]$ cd Python-3.6.4
    [jason@test Python-3.6.4]$ ./configure --prefix=/usr/local/python3.6
    [jason@test Python-3.6.4]$ make
    [jason@test Python-3.6.4]$ sudo make install

:o: 查看安装情况

    [jason@test Python-3.6.4]$ cd
    [jason@test ~]$ which python3
    [jason@test ~]$ whereis python3

:o: 运行 python3（安装到 /home/jason）

    [jason@test ~]$ python --version
    Python 3.6.4

:o: 运行 python3（安装到 /usr/local/python3.6）

    [jason@test ~]$ /usr/local/python3.6/bin/python3 --version
    Python 3.6.4

:o: 重新编译命令

使用 python3 遇到问题，请删除安装目录，然后在源码目录执行 `sudo make clean`

然后安装缺少的开发包，重新编译安装

如果 python3 使用没有任何问题，并且长期使用下来很稳定，在 `./configure` 时可以加上选项：
``

### 报错分析

:o: 未安装 gcc 编译器

解决方法：`sudo yum install gcc`

    [jason@test Python-3.6.4]$ ./configure
    checking build system type... x86_64-pc-linux-gnu
    checking host system type... x86_64-pc-linux-gnu
    checking for python3.6... no
    checking for python3... no
    checking for python... python
    checking for --enable-universalsdk... no
    checking for --with-universal-archs... no
    checking MACHDEP... linux
    checking for --without-gcc... no
    checking for --with-icc... no
    checking for gcc... no
    checking for cc... no
    checking for cl.exe... no
    configure: error: in `/home/jason/Python-3.6.4':
    configure: error: no acceptable C compiler found in $PATH
    See `config.log' for more details

:o: 未安装 zlib-devel 开发包

    [jason@test Python-3.6.4]$ sudo make install
    [...]
    Traceback (most recent call last):
      File "/home/jason/Python-3.6.4/Lib/runpy.py", line 193, in _run_module_as_main
        "__main__", mod_spec)
      File "/home/jason/Python-3.6.4/Lib/runpy.py", line 85, in _run_code
        exec(code, run_globals)
      File "/home/jason/Python-3.6.4/Lib/ensurepip/__main__.py", line 5, in <module>
        sys.exit(ensurepip._main())
      File "/home/jason/Python-3.6.4/Lib/ensurepip/__init__.py", line 204, in _main
        default_pip=args.default_pip,
      File "/home/jason/Python-3.6.4/Lib/ensurepip/__init__.py", line 117, in _bootstrap
        return _run_pip(args + [p[0] for p in _PROJECTS], additional_paths)
      File "/home/jason/Python-3.6.4/Lib/ensurepip/__init__.py", line 27, in _run_pip
        import pip
    zipimport.ZipImportError: can't decompress data; zlib not available
    make: *** [install] Error 1 

:o: 缺少相应的开发包

    [jason@test Python-3.6.4]$ ./configure
    [...]
    Python build finished successfully!
    The necessary bits to build these optional modules were not found:
    _bz2                  _curses               _curses_panel
    _dbm                  _gdbm                 _lzma
    _sqlite3              _ssl                  _tkinter
    readline
    To find the necessary bits, look in setup.py in detect_modules() for the module's name.
    
    The following modules found by detect_modules() in setup.py, have been
    built by the Makefile instead, as configured by the Setup files:
    atexit                pwd                   time
    [...]

:o: 缺少相应的开发包

    Python build finished successfully!
    The necessary bits to build these optional modules were not found:
    _bz2                  _curses               _curses_panel
    _dbm                  _gdbm                 _lzma
    _sqlite3              _ssl                  _tkinter
    readline              zlib
    To find the necessary bits, look in setup.py in detect_modules() for the module's name.
    
    The following modules found by detect_modules() in setup.py, have been
    built by the Makefile instead, as configured by the Setup files:
    atexit                pwd                   time

:o: 安装后 python3 使用异常

安装相应开发包，并且重新编译安装

    # 解决 import bz2 报错
    yum install  bzip2-devel
    
    # 解决 import curses 报错
    yum install  ncurses-devel
    
    # 解决 import sqlite3 报错
    yum install sqlite-devel
    
    # 解决 _dbm _gdbm 缺失提醒
    yum install gdbm-devel
    
    # 解决 _lzma 缺失提醒
    yum install xz-devel
    
    # 解决 _tkinter 缺失提醒
    yum install tk-devel
    
    # 解决 readline 缺失提醒及方向键行为非预期的问题
    yum install readline-devel
    
    # 解决 pip 提示缺少 SSL 模块
    yum install openssl-devel

:o: pip 安装 readline 时报错

readline 是 python 内置函数，无需使用 pip 来安装

:o: 使用 Python 自带的 readline 模块

可以尝试使用 Python 自带的 readline 模块。切换至 Modules 目录，修改 Setup 文件：

    # cd Modules/
    # vi Setup

取消文件中 readline 部分对应的注释符：

    #readline readline.c -lreadline -ltermcap

然后，再重新编译安装 Python。

:o: raw_input 和 input 无法退格

在 `.py` 中 `import readline`

:o: 将 /usr/local/python3.6/bin 加入环境变量（当前用户，临时）

    export PATH="/usr/local/python3.6/bin:$PATH"

:o: 删除环境变量（当前用户，临时）

    /usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/jason/.local/bin:/home/jason/bin

:o: 将 /usr/local/python3.6/bin 加入环境变量（全局，永久）

    sudo vi /etc/profile
        +export PATH="/usr/local/python3.6/bin:$PATH"
    source /etc/profile

:o: 将 /usr/local/python3.6/bin 加入环境变量（当前用户，永久）

    vi ~/.bash_profile
        +export PATH="/usr/local/python3.6/bin:$PATH"
    source ~/.bash_profile

:o: 执行 sudo pip3 命令时 command not found （永久）

    vi /etc/sudoers
        -Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin
        +Defaults    secure_path = /usr/local/python3.6/bin:/sbin:/bin:/usr/sbin:/usr/bin

:o: 执行 sudo pip3 命令时 command not found （临时）

方法一：使用命令的绝对路径  
方法二：用 `sudo env PATH=$PATH` 替换 `sudo`  
方法三：把脚本拷贝或链接到系统$PATH中

:o: 执行 sudo pip3 命令时 command not found （终极）

重新编译sudo,不带–with-secure-path选项

:o: 自动补全和修复input的退格键

如果想启动python编辑器就自动加载，则需要做以下操作

切换到python目录，我的系统是/usr/lib/python2.7

编辑startup.py脚本

    #!/usr/bin/python
    import readline, rlcompleter
    readline.parse_and_bind("tab: complete")


授权

    #chmod 755 /usr/lib/python2.7/startup.py

修改根目录的.bashrc文件

添加如下一行

    export PYTHONSTARTUP=/usr/lib/python2.7/startup.py

重新加载环境变量

    #source .bashrc

这样再进入python编辑器就可以自动补全啦

:o: 在CentOS 6.4上设置Python 2.7.6和3.3.3环境

http://blog.everlose.com/set-up-python-on-centos.html

:o: 文件结束符是 EOL 而不是 EOF，导致 Linux 无法执行 py 文件

    /usr/bin/python^M: bad interpreter: No such file or directory

用 vi/vim 打开该文件，命令模式下执行 `:set fileformat=unix`

回车执行后，没有任何变化，不要担心，实际上已经完成了

`:wq` 保存后，重新运行文件即可


