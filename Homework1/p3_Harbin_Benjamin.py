def find_dup_str(s,n):
    i = 0
    j=0
    dupe = 0 
    
    if n >= 4:
        return ""
    while i < len(s):
        s1 = s[i:i+n]
        j=i+1
        while j < len(s):
            if s[j:j+n] == s1:
                return s1
            j+=1
        i+=1
    return ""

def main():
    s = input("Enter a string: ")
    n = int(input("Length of duplicate string you want found: "))
    print(find_dup_str(s, n))

if __name__ == "__main__":
    main()