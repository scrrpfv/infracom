from socket import socket, AF_INET, SOCK_DGRAM

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12701))
print('Aguardando solicitacao...')

clients = {}

while True:
    request, addr_client = server_socket.recvfrom(1024)
    request = request.decode()
    print(f'Client: {addr_client[1]}; Request: {request}')
    reply = "Reply padrão"
    
    if request[:11] == "Meu nome e ":
        clients[addr_client[1]] = request[11:]
    
    if request == "Qual o meu nome?":
        reply = clients[addr_client[1]]
    
    server_socket.sendto(reply.encode(), addr_client)