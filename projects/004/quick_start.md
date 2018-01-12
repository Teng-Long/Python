### Quick Start

:o: 创建字符串

Python 可以用多种方式来操纵字符串。字符串可以被单引号 `'...'` 包裹，也可以被双引号 `"..."` 包裹，`\` 可以用来转义字符串中的引号

    >>> 'spam eggs'
    'spam eggs'
    >>> 'doesn\'t'
    "doesn't"
    >>> '"yes," he said.'
    '"yes," he said.'
    >>> "\"Yes,\" he said."
    '"Yes," he said.'
    >>> '"Isn\'t," she said.'
    '"Isn\'t," she said.'

:notebook_with_decorative_cover: 在交互型解释器中，输出的字符串被引号包裹，而且其中的特殊字符被反斜杠转义了，所以它看起来和你的输入有所不同，甚至包裹字符串的引号都有可能发生变化。如果字符串只包含单引号，那么应该用双引号来包裹这个字符串，否则，统一使用单引号来包裹字符串

:o: 使用 `print()` 打印字符串

`print()` 函数能输出更加可读的结果。通过忽略包裹字符串，并且将转义字符和特殊字符打印出来

    >>> '"Isn\'t," she said.'
    '"Isn\'t," she said.'
    >>> print('"Isn\'t," she said.')
    "Isn't," she said.
    >>> 'First line.\nSecond line.'
    'First line.\nSecond line.'
    >>> print('First line.\nSecond line.')
    First line.
    Second line.

:o: 使用 `r` 来关闭转义

如果你不希望字符被 `\` 转义，你应该在原始的字符串前面加上 `r`

    >>> print('C:\some\name')
    C:\some
    ame
    >>> print(r'C:\some\name')
    C:\some\name

:o: 使用三引号来进行多行排版

字符串的排版可以跨行。有一种实现方法是，使用三引号 `"""..."""` or `'''...'''`。行结束符会自动包含在字符串中，你可以使用 `\` 来避免这样做

    >>> print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    
    >>> 


:o: 使用 `+` 连接字符串，使用 `*` 重复字符串

    >>> 3 * 'un' + 'ium'
    'unununium'

:o: 连续的原始字符串自动被连接

    >>> text = ('Put several strings within parentheses '
    ...         'to have them joined together.')
    >>> text
    'Put several strings within parentheses to have them joined together.'

:o: 原始字符串指的是用引号包裹的字符串对象，而不是一个常量或者变量的形式

    >>> prefix = 'Py'
    >>> prefix 'thon'
      ...
    SyntaxError: invalid syntax
    >>> ('un' * 3) 'ium'
      ...
    SyntaxError: invalid syntax

:o: 连接原始字符串和变量，请使用 `+`

    >>> prefix = 'Py'
    >>> prefix + 'thon'
    'Python'

:o: 字符串可以被索引

字符串的第一个字符的索引为 `0` 。字符没有类型，它只是一个长度为 `1` 的字符串

    >>> word = 'Python'
    >>> word[0]
    'P'
    >>> word[5]
    'n'

:o: 索引值可以为负数

索引可以为负数，这表示从右向左进行索引。注意，`-0` 相当于 `0` ，负索引总是从 `-1` 开始

    >>> word[-1]
    'n'
    >>> word[-2]
    'o'
    >>> word[-6]
    'P'

:o: 对字符串进行切片

可以使用索引来对字符串进行切片，如果索引值包含了字符，那么切片被赋值为子字符串，否则为空字符串

    >>> word[0:2]
    'Py'
    >>> word[2:5]
    'tho'

:o: `s[:i] + s[i:] = s`

对于切片 `s[i:j]`， `s[i]` 包含在切片中， `s[j]` 不包含在切片中。所以有这个公式 `s[:i] + s[i:] = s`

    >>> word[:2] + word[2:]
    'Python'
    >>> word[:4] + word[4:]
    'Python'

:o: 切片的省略语法

切片有一个有用的默认用法：`s[:j]` 相当于 `s[0:j]` ，`s[i:]` 相当于 `s[i:len(s)]`

    >>> word[:2]
    'Py'
    >>> word[4:]
    'on'
    >>> word[-2:]
    'on'

:o: 切片的图形化表达

切片 `[i:j]` 等于下标 `i` 到下标 `j` 的子字符串

     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1

:o: 切片的长度

对于非负数的索引，切片长度等于索引的差：`len(word[1:3])` 等于 `2`

:o: 索引的范围

字符串索引的最大值不能超过字符串的长度，否则会抛错；但是切片中的索引没有这个限制

    >>> word[42]  # the word only has 6 characters
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range
    >>> word[4:42]
    'on'
    >>> word[42:]
    ''

:o: 字符串不能被赋值

字符串是一个列表对象，因此它不能被赋值

    >>> word[0] = 'J'
      ...
    TypeError: 'str' object does not support item assignment
    >>> word[2:] = 'py'
      ...
    TypeError: 'str' object does not support item assignment

:o: 若需要不同字符串，你应该新创建一个

    >>> 'J' + word[1:]
    'Jython'
    >>> word[:2] + 'py'
    'Pypy'

:o: 使用 `len()` 函数获得字符串的长度

内置函数 `len()` 可以获得字符串对象的长度

    >>> s = 'supercalifragilisticexpialidocious'
    >>> len(s)
    34

















