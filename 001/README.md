## 001 计算文件的 SHA 和 MD5


### 文件

- [x] [drop.py](drop.py)
- [ ] [md5.py](md5.py)
- [x] [sha1.py](sha1.py)
- [ ] [sha256.py](sha256.py)
- [x] [drop_handle_for_python_file](drop_handle_for_python_file.reg "为Python文件注册DropHandle")
- [x] [drop_handle_not_for_python_file](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

---

### 难点：拖动文件到 python 脚本中作为输入参数

[请参考这篇文章](http://blog.csdn.net/eijnew/article/details/6695271/)

默认情况下，我们无法拖放一个文件给 python 脚本让其去处理这个文件，这是因为 Windows 认为 python 脚本不是一个合法的可拖放的目的对象（drop target）

为了实现拖放目的，请执行 [drop_handle_for_python_file](drop_handle_for_python_file.reg "为Python文件注册DropHandle")  
撤销注册表更改，请执行 [drop_handle_not_for_python_file](drop_handle_not_for_python_file.reg "为Python文件注册DropHandle（恢复）")

> 注册表的生效可能需要重启资源管理器

写入注册表后，可以运行 [drop.py](drop.py) 进行测试

> : 当前逻辑还不能处理引号和斜杠的问题





