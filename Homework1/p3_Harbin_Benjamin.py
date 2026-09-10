def find_dup_str(s,n):
    i = 0
    j=0
    
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


s = input("Enter a string: ")
n = int(input("Length of duplicate string you want found: "))
print(find_dup_str(s, n))

def find_max_dup(s):
    maxDup = ""
    n=0
    while n < 4:
        maxDup = find_dup_str(s,n)
        n+=1
    return maxDup
s = input("Enter a string: ")
print(find_max_dup(s))
    