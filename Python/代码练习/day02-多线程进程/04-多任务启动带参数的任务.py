#
# 1.导入模板
# 2.创建进程对象
    # 2.1 启动带参数的任务，需要创建进程对象时给对象传递参数
    #   1）使用元组传递参数 args=(参数1，参数2，....) 按照顺序传递给任务函数
    # sub_process = multiprocessing.Process(target=foo, args=(5,))
    #   2) 使用字典传递参数 kwargs={"key":value} 按照任务的参数名字传递参数，key是任务的参数名字
# 3.启动进程 （创建子进程)

