import time
print('当前时间戳：',time.time())
print('获取当前本地时间：',time.localtime())
print('格式化可读时间模式：',time.asctime())
print('格式化日期：',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
