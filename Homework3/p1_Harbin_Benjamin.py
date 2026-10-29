class NVector:
    def __init__(self, *args)->None:
            if (len(args) == 1):
                self.vector = list(args[0])
            elif(len(args) > 1):
                self.vector = list(args)     
    def getVector(self)->list:
         return self.vector
    
    def zeroes(self, n):
            return (NVector([0 for i in range(n)]))
    
    def __len__(self)->int:
        return len(self.vector)

    def __getitem__(self, i:int):
            return self.vector[i]

    def __setitem__(self, i, value):
        self.vector[i] = value

    def __repr__(self):
        return f"NVector({self.vector})"

    def __eq__(self, vector : NVector)->bool:
        return self.vector == vector.getVector()

    def __ne__(self, vector : NVector):
        return self.vector != vector.getVector()
    def __add__(self, param):   
        if type(param) == int:
            self.vector = [(x + param) for x in self.vector]
            return self.vector

        elif type(param) == NVector:
            param_vector = param.getVector()
            j = 0
            while j < param.__len__():
                    self.vector[j] += param[j]
                    j+=1
            return self.vector
            
    def __radd__(self, param): 
            
        return self.__add__(param)

    def __mul__(self, param):  
            
        if type(param) == int:
            return sum((x * param) for x in self.vector)

        elif type(param) == NVector:
            j = 0
            copy_vector = self.vector
            while j < len(param):
                copy_vector[j] *= param[j]
                j+=1
            return sum(copy_vector)
    def __rmul__(self, param):
        return self.__mul__(param)

def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false
    otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b
   

if '__name__' == '__main__':
    n1 = NVector((3,0,-1,1))
    n2 = NVector(3,0,-1,1)
    n1[3] = 10

    testif(n1[3] == 10, "setitem works", "setitem failed")

