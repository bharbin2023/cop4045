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
    count = 0
    content = ed_read(filename)
    lst = ed_find(filename, search_str)
    if  lst == []:
        return content
    if occurence >= 0:
        while count <= occurence
        part1 = content[0:list[0]]

def main():
    fn = "file1.txt"

