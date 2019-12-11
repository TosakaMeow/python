import time

def relax():#定义一个函数，实现警告功能
    print("It`s time to relax!")
start = time.time() #建立程序初始时间戳
end = time.time()   #建立程序终止时间戳
time0 = int(input(),10) #获取需要计时的时间（单位秒），记得强制类型转换，input获取的输入为string类型
while end-start<=time0: #通过while不断刷新终止时间戳，直至两个时间戳之差大于规定时间
    end = time.time()
relax() #执行函数

