class Even:
    Print="Even,Odd"
    def Digit(self, num):
        self.num=num
        if num%2==0:
            print(f"The given number {self.num} is Even")
        else:
            print(f"The given number {self.num} is Odd")
e=Even()
e.Digit(10)
