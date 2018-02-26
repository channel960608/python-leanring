from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

s = StringIO('Hello!\nHi\nGoodbye!')
while True:
    ss = s.readline()
    if ss == '':
        break
    print(ss.strip())
