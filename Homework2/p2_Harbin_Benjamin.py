#part a function(s)
def abEqcd()->tuple:
    abcdList =[]
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                   if a**2 + b**2 == c**2 + d**2:
                       abcdList.append((a,b,c,d))
    return tuple(abcdList)

#part b functions
def lowerTuple(words: list[str])->list[tuple[str,int]]:
    newList = []
    for i in words:
        if len(i) < 5:
            newList.append((i.lower(), len(i)))
    return newList

#part c functions
def getFirstMidLast(name:str)->list[str]:
    ListofName = name.split(" ")
    return ListofName
def MiddleInitial(midInitial:str)->str:
    midInitial = midInitial[0] + '.'
    return midInitial
def newNameFormat(nameList:list[str])->str:
    newName = " ".join(nameList)
    return newName

#d
def lettersInWord(s:str)->dict[str,int]:
    freq = {}
    for letter in s.lower():
        freq[letter] = freq.get(letter, 0) + 1
    return freq
def compareLetters(str1:str, str2:str)->bool:
    w1 = lettersInWord(str1)
    w2 = lettersInWord(str2)
    if w1 == w2:
        return True
    return False


#e
def wordAndLength(wordList:list[str], wordDict: dict[str,int]):
    for word in wordList:
        wordDict[word] = len(word)

#f
def findVowels(text, vowels, locations):
    i = 0
    while i < len(text):
        if text[i].lower() in vowels:
            locations[i] = text[i].lower()
        i+=1
#a
print(abEqcd())

#b
wordList = ['One', 'SEVEN', 'three', 'two', 'Ten']
wordList = lowerTuple(wordList)
print(wordList)

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


#d
lst1 =  ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 =["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"] 
aTuple = ()
for i in lst1:
    for j in lst2:
        if len(i) == len(j) and compareLetters(i,j):
           aTuple += ((i,j),)

            #compare i and j characters
print(aTuple)

#e
wordDict = {}
s = ["one", "two", "three"]
wordAndLength(s, wordDict)
print(wordDict)

#f
text = "Hello World"
whereVowels = {}
vowels = ['a','e','i','o','u']
findVowels(text, vowels, whereVowels)
print(whereVowels)