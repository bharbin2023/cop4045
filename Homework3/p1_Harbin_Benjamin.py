class NVector:
    def __init__(self, *args):
            if (len(args) == 1):
                 self.vector = list(args[0])
            elif(len(args) > 1):
                 self.vector = list(args)     

    def getVector(self):
        return self.vector
    
    def __len__(self):
         return len(self.vector)

    def __getitem__(self, i):
         return self.vector[i]

n1 = NVector((3,0,-1,1))

print(n1.getVector())
print(n1.__len__())
print(n1.__getitem__(-2))