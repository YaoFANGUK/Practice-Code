"""
This document implements a http server
need:
- 实现代码，模拟实现服务器，获取通过浏览器客户端访问服务器的请求信息
- 并将请求报文进行分行显示
"""

import socket
import threading


class HttpServer:
    def __init__(self, port):
        # 1. create a http socket server
        self.http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 2. set port reusability
        self.http_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT)
        # 3. bind a port
        self.http_server_socket.bind(('',port))
        # 4. set into listen mode
        self.http_server_socket.listen(128)

    # 5. create a request handler
    @staticmethod
    def request_handler(new_socket, port):
        print(f'a request from {port} has been received')
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            print('The clinet has colsed the connection')
            new_socket.close()
            return
        recv_str = recv_data.decode('utf-8')
        for _ in recv_str.splitlines():
            print(_)

        new_socket.close()

    def start(self):
        while True:
            # 4. waiting for a connection with client
            new_socket, ip_port = self.http_server_socket.accept()
            # 6. create sub thread to handle request
            threading.Thread(target=self.request_handler, args=(new_socket, ip_port),daemon=True).start()


if __name__ == '__main__':
    HttpServer(9099).start()
    type()