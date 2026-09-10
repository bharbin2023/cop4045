def find_Pythagorean(n):
    Pythag = []
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            for c in range(b+1, n+1):#c must always be greater than a & b
                print(a, b, c)
                if (a**2 + b**2) == c**2:
                    print("Triple")
                    Pythag.append((a, b, c))
    return Pythag

def printPythagTriples(list_of_triples):
    for i in list_of_triples:# prints the tuples
        print(i)

def main():
    maxNum = int(input("Enter a max number: "))
    PythagTriples = find_Pythagorean(maxNum)
    printPythagTriples(PythagTriples)

if __name__ == '__main__':
    main()