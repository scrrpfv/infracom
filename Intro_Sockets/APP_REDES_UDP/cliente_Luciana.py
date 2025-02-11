from socket import socket, AF_INET, SOCK_DGRAM

socket_client = socket(AF_INET, SOCK_DGRAM)

msgs = ["Ola, eu sou um cliente",
        "Meu nome e Luciana",
        "Qual o meu nome?"]

for msg in msgs:
    input()
    socket_client.sendto(msg.encode(), ('127.0.0.1', 12701))
    resposta = socket_client.recv(1024).decode()
    print(f'A resposta foi {resposta}')


socket_client.close()
