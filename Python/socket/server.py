"""This document serves as a socket server"""

import socket
import threading


def client_request_handler(server_socket, ip_port):
    while True:
        # 6. receive data from client
        recv_data = server_socket.recv(1024)
        if len(recv_data):
            recv_str = recv_data.decode('utf-8')
            print(f'Data "{recv_str}" has been received!')
            # 7. send data to client
            sent_data = f'Hi, I am a server bot. I receive data "{recv_str}" from {ip_port}'.encode('utf-8')
            server_socket.send(sent_data)
        else:
            print('The client has closed the connection')
            break
    server_socket.close()


if __name__ == '__main__':
    # 1. create a server socket object
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # reuse a port
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
    # 2. bind a port
    tcp_server_socket.bind(('',9899))
    # 3. set listen
    tcp_server_socket.listen(128)
    while True:
        # 4. waiting for a client request
        new_socket, ip_port = tcp_server_socket.accept()
        # 5. create thread which calls a request handler
        threading.Thread(target=client_request_handler, args=(new_socket, ip_port), daemon=True).start()
