#! python3.6


import time


if __name__ == '__main__':
    j = '#'
    for i in range(1,61):
        j += '#'
        print('{:.2f}% |{}>'.format((i / 60) * 100, j), end='\r')
        time.sleep(0.05)
    print('100.00% |{}|'.format(j))
    print('\n')
    input('Press <Enter>')
