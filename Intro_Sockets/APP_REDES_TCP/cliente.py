from socket import socket, AF_INET, SOCK_STREAM

while True:
    socket_client = socket(AF_INET, SOCK_STREAM)
    socket_client.connect(('172.20.4.79', 65535))
    msg = input('mensagem: ')

    if msg != 'exit':
        socket_client.send(msg.encode())
        resposta = socket_client.recv(1024).decode()
        print(f'A resposta foi {resposta}')
        socket_client.close()
    else:
        break