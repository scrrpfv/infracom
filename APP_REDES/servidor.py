from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

def Handle_Request(socket_client):
    request = socket_client.recv(1024).decode()
    print(f'A requisição foi {request}')
    reply = input('mensagem: ')
    socket_client.send(reply.encode())
    socket_client.close

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 13345))
server_socket.listen()
print('Aguardando solicitacao...')

while True:
    socket_client, addr_client = server_socket.accept()
    print(f'Recebendo de {addr_client}')
    Thread(target=Handle_Request, args=(socket_client,)).start()
    