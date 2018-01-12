## PySQL 简明教程

:o: 为什么用 PySQL

python3不再支持mysqldb 请用pymysql和mysql.connector

:o: PySQL 和 MySQLdb

MySQLdb 与PyMySQL都是Python与MySQL数据库的连接器，不同的是MySQLdb是为Python 2.x设计的，而PyMySQL是为Python 3.x设计的。
如果是使用Python 2.x，则应该安装MySQLdb;如果是使用Python 3.x，则应该安装PyMySQL


安装完毕后，导入如下：
Python 2.x:

    >>> import MySQLdb #（注意大小写）

Python 3.x

    >>> import pymysql #（全部为小写字母）

https://www.techforgeek.info/mysqldb_pymysql.html

:o: Python3 安装 PySQL

    C:\Users\Jason>py -3 -m pip install PyMySQL
    Collecting PyMySQL
      Downloading PyMySQL-0.8.0-py2.py3-none-any.whl (83kB)
        100% |████████████████████████████████| 92kB 121kB/s
    Installing collected packages: PyMySQL
    Successfully installed PyMySQL-0.8.0
    
    C:\Users\Jason>


:o: 查询表格中的列

    import pymysql.cursors
    
    
    database_connection = pymysql.connect(host='39.108.85.208',
                                          user='jason',
                                          password='19990124**1y',
                                          db='jason_library_system',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    
    with database_connection.cursor() as cursor:
        try:
            sql = 'select `user` from users'
            cursor.execute(sql)
            select_result = cursor.fetchall()
            print('select_result: ', select_result)
        finally:
            database_connection.close()

返回结果：`select_result:  {'user': 'jason'}`

遍历字典的值可以使用 `for user in select_result.values()`

:o: 使用字典存储连接参数，更加优雅

SQL: `select `user` from users`

    import pymysql.cursors
    
    config = {
        'host': '39.108.85.208',
        'user': 'jason',
        'password': '19990124**1y',
        'db': 'jason_library_system',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        }
    
    database_connection = pymysql.connect(**config)
    
    with database_connection.cursor() as cursor:
        try:
            sql = 'select `user` from users'
            cursor.execute(sql)
            select_result = cursor.fetchall()
            print('select_result: ', select_result)
        finally:
            database_connection.close()

:o: 可用的参数

    :param host: Host where the database server is located
    :param user: Username to log in as
    :param password: Password to use.
    :param database: Database to use, None to not use a particular one.
    :param port: MySQL port to use, default is usually OK. (default: 3306)
    :param bind_address: When the client has multiple network interfaces, specify
        the interface from which to connect to the host. Argument can be
        a hostname or an IP address.
    :param unix_socket: Optionally, you can use a unix socket rather than TCP/IP.
    :param charset: Charset you want to use.
    :param sql_mode: Default SQL_MODE to use.
    :param read_default_file:
        Specifies  my.cnf file to read these parameters from under the [client] section.
    :param conv:
        Conversion dictionary to use instead of the default one.
        This is used to provide custom marshalling and unmarshaling of types.
        See converters.
    :param use_unicode:
        Whether or not to default to unicode strings.
        This option defaults to true for Py3k.
    :param client_flag: Custom flags to send to MySQL. Find potential values in constants.CLIENT.
    :param cursorclass: Custom cursor class to use.
    :param init_command: Initial SQL statement to run when connection is established.
    :param connect_timeout: Timeout before throwing an exception when connecting.
        (default: 10, min: 1, max: 31536000)
    :param ssl:
        A dict of arguments similar to mysql_ssl_set()'s parameters.
        For now the capath and cipher arguments are not supported.
    :param read_default_group: Group to read from in the configuration file.
    :param compress: Not supported
    :param named_pipe: Not supported
    :param autocommit: Autocommit mode. None means use server default. (default: False)
    :param local_infile: Boolean to enable the use of LOAD DATA LOCAL command. (default: False)
    :param max_allowed_packet: Max size of packet sent to server in bytes. (default: 16MB)
        Only used to limit size of "LOAD LOCAL INFILE" data packet smaller than default (16KB).
    :param defer_connect: Don't explicitly connect on contruction - wait for connect call.
        (default: False)
    :param auth_plugin_map: A dict of plugin names to a class that processes that plugin.
        The class will take the Connection object as the argument to the constructor.
        The class needs an authenticate method taking an authentication packet as
        an argument.  For the dialog plugin, a prompt(echo, prompt) method can be used
        (if no authenticate method) for returning a string from the user. (experimental)
    :param db: Alias for database. (for compatibility to MySQLdb)
    :param passwd: Alias for password. (for compatibility to MySQLdb)
    :param binary_prefix: Add _binary prefix on bytes and bytearray. (default: False)

:o: PyCharm warning

Setting 搜索 `SQL Dialects` ，将 `<Generic> dialect` 更改为你使用的数据库类型，比如 `MySQL`

    Detects the best matching SQL dialect for files in <Generic> dialect.









