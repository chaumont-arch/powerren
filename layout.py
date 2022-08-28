import alias_lookup

def parse_layout(chapter):
    file = open(f"layout{chapter}.pwrr","r")
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
        if structure[object] != []:
            output.write(f"label {object}_move:\n")
            output.write("\tmenu\n")
            output.write("\t\t\"Where to?\"\n")
            for dest_combo in structure[object]:
                destination = dest_combo[0]
                evaluat = dest_combo[1] #?
                dest_str = alias_lookup.alias_lookup(chapter,destination) # Version to print in menus
                output.write(f"\t\t\"{dest_str}\":\n")
                if evaluat:
                    output.write(f"\t\t\tjump {evaluat}\n")
                else:
                    output.write(f"\t\t\tjump {destination}_landing\n")
            output.write(f"\t\t\"Cancel\":\n")
            output.write(f"\t\t\tjump {object}_landing\n\n")

parse_layout(1)
