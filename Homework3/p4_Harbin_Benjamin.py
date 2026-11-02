def ed_read(filename, From = 0, to = -1):
    try:
        
        file_str = filename.readline()
        return file_str[From:to]
    except:
        raise IndexError("last index is out of range")

def ed_find(filename, search_str):
    indexes = []
    content = ed_read(filename)
    beg = 0 
    end = len(search_str)
    while end < len(content):
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
    
    if occurence == -1:
        for i in lst:
            part1 = content[0:i]
            part2 = content[i+len(search_str):]
            new_content = part1 + replace + part2
        return new_content
    count = 0
    while count <= occurence:
        part1 = content[0:lst[count]]
        part2 = content[count+len(search_str):]
        new_content = part1 + replace + part2
        count += 1
    return new_content

def ed_append(filename, string):
    with open(filename,"a", encoding = "utf-8") as f1:
        f1.write(string)
    return len(string)
            
def main():
    fn = "file1.txt"
    ed_append(fn, "0123456789")

