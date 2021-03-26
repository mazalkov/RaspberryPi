# https://www.learnpython.org/en/Partial_functions


#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
partial_func = partial(func, 5, 4, 3)
print(partial_func(22))
