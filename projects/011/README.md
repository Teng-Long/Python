## CentOS7 RPM 安装 python3.6

先来介绍一下 [IUS](https://link.jianshu.com/?t=https://ius.io/) 这个社区，名字的全写是【Inline with Upstream Stable】取首字母，它主要是一个提供新版本RPM包的社区。具体使用可以查看[官方文档](https://link.jianshu.com/?t=https://ius.io/GettingStarted/#install-via-automation) 简单说来就只要按下面的命令操作即可。

    yum -y install https://centos7.iuscommunity.org/ius-release.rpm

添加 IUS 之后，先创建缓存元数据，再进行安装即可

    yum makecache
    yum install python36u
    yum -y install python36u-pip
    yum -y install python36u-devel

完成后直接终端输入 `python3` 即可。

