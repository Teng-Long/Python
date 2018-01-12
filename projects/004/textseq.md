### 文本序列类型 `str`

Python 中的文本数据是用 str 对象或字符串处理的。字符串是一个 Unicode 的不可变序列

    [...]

字符串文本有多种表达方式

    单引号: `'allows embedded "double" quotes'`
    双引号: `"allows embedded 'single' quotes"`
    三引号: `'''Three single quotes''', """Three double quotes"""`

三引号支持多行。其中的空白字符也包含在字符串文本中

    [...]

作为单个表达式的一部分的两个字符串将隐式转换为单个字符串文本：

    >>> 'Py''thon'
    Python

字符串文本有多种形式：

    stringliteral   ::=  [stringprefix](shortstring | longstring)
    stringprefix    ::=  "r" | "u" | "R" | "U" | "f" | "F"
                         | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
    shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
    longstring      ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
    shortstringitem ::=  shortstringchar | stringescapeseq
    longstringitem  ::=  longstringchar | stringescapeseq
    shortstringchar ::=  <any source character except "\" or newline or the quote>
    longstringchar  ::=  <any source character except "\">
    stringescapeseq ::=  "\" <any source character>

字符串可以使用 `str` 构造器由其他类型的对象构造得到

    class str(object=b'', encoding='utf-8', errors='strict')



















