def foo():
    r = some_function()
    if f == (-1):
        return -1
    return r

def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass



try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

print('END')
