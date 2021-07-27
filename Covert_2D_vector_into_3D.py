class C2dVec:
    def __init__(self, i, j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

c2=C2dVec(3, 9)
c3=C3dVec(8,4,5)
print(c2)
print(c3)