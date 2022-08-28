def parse_landing(chapter):
    file = open(f"landing{chapter}.pwrr","r")
    output = open(f"landing{chapter}.rpy","w")
    alias = open(f"alias{chapter}.txt","w")

    title = ""
    phrases = []

    for line in file.readlines():
        #ex = Exception(f"Unfamiliar combo {words == ''} in level {value}")

        array = line.split("\t")
        value = len(array) - 1
        words = array[-1].replace('\n','')

        first = array[0].replace('\n','')
        try:
            second = array[1].replace('\n','')
        except:
            second = ''

        if first != '':
            title = first
            alias.write(f"{first}\t{second}\n")
        elif second != '':
            phrases.append(second)
        else:
            output.write(f"label {title}_menu:\n")
            output.write(f"    scene {title}-{chapter}\n")
            for phrase in phrases:
                output.write(f"    \"{phrase}\"\n")
            output.write(f"    jump {title}_menu\n\n")

            title = ""
            phrases = []

parse_landing(1)
