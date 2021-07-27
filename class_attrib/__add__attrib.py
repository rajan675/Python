class Sum:
    def  __init__(self, num):
        self.num=num
    def __add__(self, num2):
        return self.num + num2.num
n1=Sum(3)
n2=Sum(4)
n3=Sum(6)
sum= n1 + n2
print(sum)