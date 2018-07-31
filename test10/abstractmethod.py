#接口类
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass

    @abstractmethod
    def get(self, money):
        print("Payment get%d" % money)

    def total(self,money):
        print("Payment total %d" % money)

    def __init__(self,name):
        print(self)
        self.name = name

class AppPay(Payment):
    def pay(self,money):
        print("AppPay pay %d"%money)

    def get(self,money):
        print("AppPay get %d" % money)

app = AppPay("safly")
app.pay(100)
app.get(200)
app.total(400)
# 不能实例化
# TypeError: Can't instantiate abstract class Payment
# with abstract methods get, pay
# a = Payment("safly")