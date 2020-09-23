
# 0.导入模块
# 1.创建服务器socket
# 2.绑定端口
# 3.设置监听模式
# 4.等待客户端链接，如果有客户端链接，返回新的socket服务客户端，返回客户端的ip和端口
# 5.接收数据
# 6.发送数据
# 7.关闭新的socket，关闭服务器socket

# 0.导入模块


if __name__ == '__main__':
    # 1.创建服务器socket
    #   AF_INET: ipv4地址类型
    #   SOCK_STREAM:tcp协议


    # 设置端口复用：关闭socket时立刻释放端口，无需等待1~2分钟。不是表示一个端口可以给多个程序使用
    #   参数1：设置当前socket
    #   参数2：设置端口复用选项
    #   参数3：设置端口复用选项的值（True表示开启端口复用）


    # 2.绑定端口
    #   bind(元组)
    #   元组格式: (本地ip，端口号)


    # 3.设置监听模式
    #   listen:
    #       1) 设置当前tcp_server_socket为被动链接的socket，这个socket不能收发消息
    #       2) 128 允许最大等待链接的个数(推荐)


    # 4.循环等待客户端链接，如果有客户端链接，返回新的socket服务客户端，返回客户端的ip和端口
        #   accept: 返回一个元组类型 (新的服务器客户端的socket, 客户端的ip和端口信息)


        # 5.循环接收数据
            #   1024: 这次recv接收的最大字节个数


            # 6.发送数据


        # 7.关闭新的socket，关闭服务器socket


    # tcp_server_socket.close()

