import base64

b = base64.b64encode(b'binary\x00string')
print(b)
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
