import time


class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def now(s):
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回

    # def now(s):
    #     t=time.localtime() #获取结构化的时间格式
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回

    @staticmethod
    def now_s(): #用Date.now()的形式去产生实例,该实例用的是当前时间
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回

    # @staticmethod
    # def tomorrow_s():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
    #     t=time.localtime(time.time()+86400)
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday)
        

a=Date('1987',11,27) #自己定义时间
b=Date.now_s() #采用当前时间
c=Date.now(a) #采用当前时间
d=a.now_s()
e=a.now()
f=a.now()


print(a.year,a.month,a.day)
print(b.year,b.month,b.day)
print(c.year,c.month,c.day)