def alias_lookup(chapter, name):
    file = open(f"alias{chapter}.txt","r")

    for line in file.readlines():
        array = line.split("\t")
        if array[0] == name:
            return array[1].replace("\n","")
    
    return name
