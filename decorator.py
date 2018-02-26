import datetime
def now():
    print(datetime.datetime.now())

f = now
f()
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now2():
    print(datetime.datetime.now())

now2()
