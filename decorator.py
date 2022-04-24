def start_stop(f):
    def wrapper():
        print('start')
        f()
        print('end')
    return wrapper

def func():
    print('i am func')

x = start_stop(func)
x()

## @ syntax
@start_stop
def func2():
    print('i am func2')

func2()

#Dans l'état ca ne marche pas avec si func a un argument alors que func2 n'en a pas.
def start_stop_up(f):
    def wrapper(*args, **kwargs):
        print('start')
        f(*args, **kwargs)
        print('end')
    return wrapper

@start_stop_up
def func3(x):
    print(x)
    return x

@start_stop_up
def func4():
    print('i am func4')

func3('i am func3')
func4()
#Dans l'état ca ne marche pas avec des pures functions.
y = func3('alex')
print(y)

def start_stop_final(f):
    def wrapper(*args, **kwargs):
        print('start')
        rv = f(*args, **kwargs)
        print('end')
        return rv
    return wrapper

@start_stop_final
def func5(x):
    print(x)
    return x

y = func5('i am func5')
print(y)

#### decorator for timing exeution
from cgi import test
import time
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        rv = func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return rv
    return wrapper

@timer
def timed_func(n):
    s = 0
    for i in range(n):
        s+=i
    return s

z = timed_func(1_000)
print(z)

@timer
def test_time(n):
    time.sleep(n)

test_time(3)
