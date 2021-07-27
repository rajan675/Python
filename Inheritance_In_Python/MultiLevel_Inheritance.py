class Dada:
    Identity="Human"
    def getDetails(self):
        print("I am Dada")
class Papa(Dada):
    def getInfo(self):
        print("I am Papa son of Dada")
class Beta(Papa):
    def getKnowledge(self):
        print("I am Beta son of Papa and grandson of Dada")

d=Dada()
p=Papa()
b=Beta()
print(b.Identity) #Inherits the identity of Dada // Child of child
b.getDetails()
b.getInfo()
b.getKnowledge()