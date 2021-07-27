class Dada:
    Identity="Human"
    def getDetails(self):
        print("I am Dada")
class Papa(Dada):
    def getDetails(self):
        super().getDetails()
        print("I am Papa son of Dada")
class Beta(Papa):
    def getDetails(self):
        super().getDetails()
        print("I am Beta son of Papa and grandson of Dada")

d=Dada()
p=Papa()
b=Beta()
# p.getDetails()
b.getDetails()