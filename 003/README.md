## 进度条

### File List

- [x] [循环的进度条](cycle_process_bar.py)
- [x] [百分比显示+进度条](example2.py)

---

### 思路

#### 使用转义符 `\r`

`\r` 使光标到行首，后面的输出就可以覆盖已有的输出

#### 使用转义符 `\r`

`\b` 相当于退格符

#### 使用类库

类“progressbar”(http://code.google.com/p/python-progressbar/)

---

### 用到的函数

#### cycle_process_bar(width, rate, hash_number)

```python
import time


def cycle_process_bar(width, rate, hash_number):
    width += hash_number
    while True:
        for i in range(width):
            str_obj = '[' + (' ' * (i % width) + '#' * hash_number + ' ' * (width - i % width))[hash_number:width] + ']'
            print(str_obj, end="\r")
            time.sleep(rate)
```