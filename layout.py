def parse_layout(chapter):
    file = open(f"layout{chapter}.txt","r")
    output = open(f"layout{chapter}.rpy","w")

    structure = {}
    title = ""

    for line in file.readlines():
        array = line.split("\t")
        if len(array) == 1:
            title = array[0].replace('\n','')
        else:
            destination = array[1].replace('\n','')
            if len(array) > 2:
                direction = array[2].replace('\n','')
                if len(array) > 3:
                    subcode = array[3].replace('\n','')
                else:
                    subcode = None
            else:
                direction = None
                subcode = None

            if not title in structure:
                structure[title] = []
            if not destination in structure:
                structure[destination] = []

            structure[title].append([destination,subcode])
            if direction != '1':
                structure[destination].append([title,subcode])

    for object in structure:
        print(f"{object} goes to {structure[object]}")

parse_layout(1)
