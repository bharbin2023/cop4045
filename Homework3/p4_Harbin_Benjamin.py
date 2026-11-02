def ed_read(filename, From = 0, to = -1):
    try:
        with open(filename, 'r', encoding = "utf-8") as f1:
            file_str = f1.read()
        if to == -1:
            return file_str[From:]
        else:
            return file_str[From:to]
    except IndexError:
        print("Index out of bounds")
        return ""
        

def ed_find(filename, search_str):
    indexes = []
    content = ed_read(filename)
    print(content)
    beg = 0 
    end = len(search_str)
    
    while end <= len(content):
        if content[beg:end] == search_str:
            indexes.append(beg)
        beg+=1
        end+=1
    return indexes
    
    

def ed_replace(filename, search_str, replace, occurence = -1):
    lst = ed_find(filename, search_str)
    content = ed_read(filename)

    if len(lst) == 0:
        return content
    new_content = ""
    if occurence <= -2:
        raise IndexError("Out of bounds")
    if occurence == -1:
        new_content = content.replace(search_str,replace)
    else:
        part1 = content[0:lst[occurence]]
        part2 = content[lst[occurence]+len(replace):]
        new_content = part1 + replace + part2

    with open(filename, "w", encoding="utf-8") as f1:
        f1.write(new_content)
    return new_content
    
         

def ed_append(filename, string):
    with open(filename,"a",encoding = "utf-8") as f1:
        f1.write(string)
    return len(string)
def main():
    fn = "file1.txt"
    ed_append(fn, "0123456789")
    ed_append(fn, "0123456789")
    

    print(ed_read(fn, 3, 9))
    print(ed_read(fn,3))
    
    lst = ed_find(fn,"345")
    print(lst)
    
    ed_replace(fn, "345", "ABCDE", -1) # changes the file to 0123456789012ABCDE6789
    print(ed_read(fn))
    # assume we reset the file content to 01234567890123456789 (not shown)
    ed_replace(fn, "345", "ABCDE", 3) # changes the file to 012ABCDE6789012ABCDE6789
    
    

if __name__ == '__main__':
    main()
