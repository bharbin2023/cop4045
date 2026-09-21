
def line_number(file1,file2):
    try:
        with open(file1, "r") as f:
            with open(file2, "w") as f2:
                i= 1
                for line in f:
                    f2.write(f"{i}. {line}")
                    i+=1

    except FileNotFoundError:
        print(f"Could not find a file")
        raise FileNotFoundError

def parse_functions(file):  
    try:
        parsFuncTup = ()
        with open(file,"r") as file:
            i =0
            fileLines = file.readlines()#creates a list to loop through instead of just the file
            
            for line in fileLines:
                tempTup = ()
                cleanLine = line.strip()
                if line.strip()[:3] == "def":
                    tempTup += (i+1,)
                    tempTup += (cleanLine[cleanLine.find(' ')+1:cleanLine.find('(')],)#finding index where func def starts and ends
                    tempTup += (cleanLine[cleanLine.find('(')+1:cleanLine.find(')')],)#getting the parameters between the ()
                    tempTup += funcDef(i, fileLines)#gets the function definitions
                    parsFuncTup += (tempTup,)
                i+=1
            return parsFuncTup
    except FileNotFoundError:
        print("Could not find the file")
        raise FileNotFoundError

def funcDef(i:int, fileLines:list[str])->tuple: #loops throu
    definition = ""
    j = i
    while len(fileLines[j].strip()) != 0 and j < len(fileLines):
        definition += fileLines[j]
        j+=1
        
    return (definition,)
def sortTuple(tup:tuple)->tuple:#returns a alphabetically ordered tuple with selection sort
    i=1
    tupList = list(tup)
    lowestIndex = 0
    while i < len(tup):
        if tupList[i][1] < tupList[lowestIndex][1]:
            temp = tupList[i]
            tupList[i] = tupList[lowestIndex]
            tupList[lowestIndex] = temp
        i+=1
            
    return tuple(tupList)
#file1 = input("Enter a file you would like to read from: ")
#file2 = input("Enter a file you would like to write to: ")

#line_number(file1, file2)
funcTuple = parse_functions("funs.py")
for tup in funcTuple:
    print(tup)

funcTuple = sortTuple(funcTuple)
for tup in funcTuple:
    print(tup)