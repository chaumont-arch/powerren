def parse_landing(chapter):
    file = open(f"landing{chapter}.txt","r")
    output = open(f"landing{chapter}.rpy","w")

    title = ""
    phrases = []

    for line in file.readlines():
        array = line.split("\t")
        value = len(array) - 1
        words = array[-1].replace('\n','')

        if (value == 0) and (words != ''):
            title = words
        elif value == 1:
            phrases.append(words)
        elif (value == 0) and (words == ''):
            output.write(f"label {title}_menu:\n")
            output.write(f"\tscene {title}-{chapter}\n")
            for phrase in phrases:
                output.write(f"\t\"{phrase}\"\n")
            output.write(f"\tjump {title}_menu\n\n")

            title = ""
            phrases = []
        else:
            raise Exception(f"Unfamiliar combo {words == ''} in level {value}")
