from socket import socket, AF_INET, SOCK_STREAM

with open('index.html', 'r') as f:
    index_html = f.read()
with open('style.css', 'r') as f:
    style_css = f.read()

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(('localhost', 11111))
ss.listen()

while True:
    sc, _ = ss.accept()
    request = sc.recv(1024).decode()
    if request.startswith('GET / HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\n\n' + index_html
    elif request.startswith('GET /style.css HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\nContent-Type: text/css\n\n' + style_css
    else:
        reply = 'HTTP/1.1 404 Not Found\n\nPage not found.'
    
    sc.send(reply.encode())
    sc.close()

ss.close()
