import poplib

email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Messages: %s. Size %s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(idnex)

msg_content = b'\r\n'.join(lines).decode('utf-8')

msg = Parser().parsestr(msg_content)

server.quit()
