import re

s = r'ABC\-001'

ans = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

print(ans)

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')
else:
    print('failed')


print(re.split(r'\s+', 'a b  c'))

m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

g = re.match(r'^(\d+)(0*)$','102300').groups()

print(g)

g = re.match(r'^(\d+?)(0*)$','102300').groups()

print(g)

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
rt = re_telephone.match('010-123456').groups()

print(rt)

re_email = re.compile(r'^([0-9a-zA-Z\_\.]+)@(gmail|qq|microsoft).com')
re = re_email.match('someone@gmail.com').groups()
print(re)
