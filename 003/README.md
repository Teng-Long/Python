## 进度条

### File List

- [ ] [cycle_process bar.py](cycle_process_bar.py)


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