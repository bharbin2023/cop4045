#part a function(s)
def abEqcd():
    abcdList =[]
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                   if a**2 + b**2 == c**2 + d**2:
                       abcdList.append((a,b,c,d))
    return tuple(abcdList)

#part b functions
def lowerTuple(list):
    newList = []
    for i in list:
        if len(i) < 5:
            newList.append((i.lower(), len(i)))
    return newList

#part c functions
def getFirstMidLast(name):
    name = name.split(" ")
    return name
def MiddleInitial(midInitial):
    midInitial = midInitial[0] + '.'
    return midInitial
def newNameFormat(nameList):
    newName = " ".join(nameList)
    return newName
#a
#print(abEqcd())

#b
'''
list = ['One', 'SEVEN', 'three', 'two', 'Ten']
list = lowerTuple(list)
print(list)
'''
#c
nameList = []
newNameFormatList = []
n = int(input("How many names do you want to enter? "))
for i in range(n):
    name = input("\nEnter a first, middle, and last name: ")
    nameList.append(name)

for i in nameList:
    i = getFirstMidLast(i)
    i[1]= MiddleInitial(i[1])
    newNameFormatList.append(newNameFormat(i))
print(newNameFormatList)