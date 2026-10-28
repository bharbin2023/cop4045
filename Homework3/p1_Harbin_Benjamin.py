class NVector:
    def __init__(self, *args)->None:
            if (len(args) == 1):
                self.vector = list(args[0])
            elif(len(args) > 1):
                self.vector = list(args)     
    def getVector(self)->list:
         return self.vector
    
    def __len__(self)->int:
        return len(self.vector)

    def __getitem__(self, i:int):
         return self.vector[i]

    def __setitem__(self, i, value):
        self.vector[i] = value

    def __repr__(self):
        return f"NVector({self.vector})"

    def __eq__(self, vector : NVector)->bool:
        if vector == self.vector: return True
        else:
             return False

    def __ne__(self, vector : NVector):
         if vector != self.vector: return True
         else:
            return False
    def __add__(self, param):   
        if type(param) == int:
            self.vector = [(x + param) for x in self.vector]
            return self.vector
    
        elif type(param) == NVector:
            param_vector = param.getVector()
            j = 0
            while j < len(param):
                 self.vector[j] += param[j]
                 j+=1
            return self.vector
        
                 
                 
            
    def __radd__(self, param): 
            self.vector = [(x + param) for x in self.vector]
            return self.vector
    
         



n1 = NVector((3,0,-1,1))
n2 = NVector(3,0,-1,1)

print(n1.getVector())
print(n1.__len__())
print(n1.__getitem__(-2))
n1[2] = 4
print(n1.getVector())
print(n1)
print(10 + n2)
print(n2 + n1)
