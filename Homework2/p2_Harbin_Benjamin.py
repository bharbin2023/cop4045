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

#d
def lettersInWord(s):
    freq = {}
    for letter in s.lower():
        freq[letter] = freq.get(letter, 0) + 1
    return freq
def compareLetters(str1, str2):
    w1 = lettersInWord(str1)
    w2 = lettersInWord(str2)
    if w1 == w2:
        return True
    return False

def createTuple(str1, str2):
    newTuple = (i,j)
    return newTuple
#e
def wordAndLength(wordList, dict):
    for word in wordList:
        dict[word] = len(word)
#a
#print(abEqcd())

#b
'''
list = ['One', 'SEVEN', 'three', 'two', 'Ten']
list = lowerTuple(list)
print(list)
'''
#c
'''
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
'''

#d
'''
lst1 =  ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 =["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"] 
aTuple = ()
for i in lst1:
    for j in lst2:
        if len(i) == len(j) and compareLetters(i,j):
           aTuple += (createTuple(i,j),)

            #compare i and j characters
print(aTuple)
'''
#e
dict = {}
s = ["one", "two", "three"]
wordAndLength(s, dict)
print(dict)

