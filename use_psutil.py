import psutil
# CPU逻辑数量
# print(psutil.cpu_count())
# CPU物理核心
# print(psutil.cpu_count(logical=False))
# CPU的用户/系统/空闲时间
# print(psutil.cpu_times())
# 每秒刷新CPU使用率
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
# 内存信息
# print(psutil.virtual_memory())
# 磁盘信息
# print(psutil.disk_partitions())     # 磁盘分区
# print(psutil.disk_usage('/'))       # 磁盘使用情况
# print(psutil.disk_io_counters())    # 磁盘IO
# 网络信息
# print(psutil.net_io_counters())     # 网络读写字节/包个数
# print(psutil.net_if_addrs())        # 获取网络接口信息
# print(psutil.net_if_stats())        # 获取网络接口状态
# print(psutil.net_connections())     # 获取网络连接信息
# 进程信息
print(psutil.pids())
p = psutil.Process(30630)
print([p.name(),p.exe(),p.cwd(),p.cmdline(),p.ppid(),p.parent(),p.children(),p.status(),p.username(),p.create_time(),p.terminal(),p.cpu_times(),p.memory_info()])
