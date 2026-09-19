
def line_number(file1,file2):
    try:
        with open(file1, "r") as f:
            with open(file2, "w") as f2:
                for i, line in enumerate(f, i=1):
                    f2.write(f"{i}. {line}")

    except FileNotFoundError:
        print(f"Could not find a file")
        raise
def parse_functions(file):
    funcLines = ()
    with open(file,"r") as f:
        for i, line in enumerate(f, start =1):
            if line[0:3] == "def":
                funcLines += (i,)
    
    return funcLines

#file1 = input("Enter a file you would like to read from: ")
#file2 = input("Enter a file you would like to write to: ")

#line_number(file1, file2)
funcTuple = parse_functions("funs.py")
print(funcTuple)