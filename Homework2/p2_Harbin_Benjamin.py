def line_number(file1,file2):
    try:
        with open(file1, "r") as f:
            with open(file2, "w") as f2:
                for i, line in enumerate(f):
                    f2.write(f"{i+1} {line}")

    except FileNotFoundError:
        print(f"Could not find a file")
        raise

file1 = input("Enter a file you would like to read from: ")
file2 = input("Enter a file you would like to write to: ")

line_number(file1, file2)
