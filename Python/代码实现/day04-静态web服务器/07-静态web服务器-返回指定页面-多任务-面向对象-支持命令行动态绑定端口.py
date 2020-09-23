# 1. 判断有没有传递参数 
# 2. 判断参数必须是整数
# 3. 把端口号的字符串强制转换成int


# 面向对象:
#   静态web服务器
# 抽象类:
#   类名: HttpWebServer
#   属性: tcp_server_socket
#   方法: __init__, handler_client, start

import socket
import threading
import sys


class HttpWebServer(object):

    # 类创建对象时自动调用的魔法方法(实现实例属性的初始化)
    def __init__(self, port):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(("", port))
        self.tcp_server_socket.listen(128)

    # 启动web服务器方法
    def start(self):
        # 1.2. 循环等待客户端连接
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            print("客户端链接: ", ip_port)

            # 一旦有客户端请求创建子线程服务客户端
            sub_thread = threading.Thread(target=self.handler_client_request, args=(new_socket, ip_port))
            # 防止主线程无法关闭
            sub_thread.setDaemon(True)
            # 启动线程对象，创建子线程并执行
            sub_thread.start()

    # 实例方法(self)，类方法(cls)，静态方法(既不需要访问实例属性，也不需要访问类属性)
    @staticmethod
    def handler_client_request(new_socket, ip_port):
        # 2. 接收到浏览器发送的http请求报文
        recv_data = new_socket.recv(1024)
        # 2.1. 判断浏览器关闭（客户端下线）
        if len(recv_data) == 0:
            print(ip_port, "浏览器断开链接")
            new_socket.close()
            return

        recv_str = recv_data.decode("utf-8")
        # 2.2. 提取请求资源路径
        #   按照空格分割请求报文 (GET /index.html HTTP/1.1\r\n ....)
        #   [0]: GET
        #   [1]: /index.html
        #   [2]: ....
        #   split(分割字符， maxsplit=最大分割次数)
        recv_list = recv_str.split(" ", maxsplit=2)
        request_path = recv_list[1]
        print("请求资源路径: ", request_path)

        # 2.3. 如果没有请求指定页面，那么设置默认首页
        if request_path == "/":
            request_path = "/index.html"

        # 3. 读取指定页面的数据，构建响应报文并返回
        try:
            #   3.1 读取指定页面的数据
            #       无论什么请求，我都返回一个指定页面 static + 请求资源路径
            #       "r":读出字符串数据  "rb":读出二进制数据 (支持读任意文件)
            with open("static" + request_path, "rb") as file:
                file_data = file.read()

        except Exception as e:
            #   3.2. 请求资源路径，找不到指定文件或者目录
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_head = "Server: NBW/1.0\r\n"

            with open("static/error.html", "rb") as file:
                response_body = file.read()

            response_data = (response_line + response_head + "\r\n").encode("utf-8") + response_body

            new_socket.send(response_data)

        else:
            #   3.3. 请求资源路径，能够找到资源，并返回响应报文

            response_line = "HTTP/1.1 200 OK\r\n"
            response_head = "Server: NBW/1.0\r\n"
            response_body = file_data

            response_data = (response_line + response_head + "\r\n").encode("utf-8") + response_body
            new_socket.send(response_data)

        finally:
            new_socket.close()


if __name__ == '__main__':



    # 1. 判断有没有传递参数

        # argv个数是2个，表示有传递参数
        # 2. 判断参数必须是整数


            # 结束程序




    # 3. 把端口号的字符串强制转换成int


    # 创建静态web服务器的对象

    # 启动静态web服务器





