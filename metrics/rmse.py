import numpy as np

def rmse(h, x, y):
    m = len(x)
    return np.sqrt(np.power(1/m*np.sum(h(x) - y), 2))

# 예제
# x = np.arange(0, 10)
# def h(x, a=1, b=1):
#     return a*x + b
# y = array([ 1,  5,  7,  9, 11, 13, 15, 17, 19, 21])
# rmse(h, x, y)