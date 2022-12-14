#This takes landing files and makes two things:
#1. A landing label for each location in the approriate chapters.
#2. Create an alias file, showing how to display each location ingame.

def output(mode, chapter_index, message):
    if mode == "landing":
        format = "rpy"
    else:
        format = "txt"

    for index in chapter_index:
        file = open(f"{mode}{index}.{format}","a")
        file.write(message.replace('*',index)) #? * as a wildcard for chapter index
        file.close()

def parse_landing(chapter):
    file = open(f"landing{chapter}.pwrr","r")
    #output = open(f"landing{chapter}.rpy","w")
    #alias = open(f"alias{chapter}.txt","w")
    #output.write("#Autogenerated, do not edit.\n\n")

    title = ""
    phrases = []

    file_to_read = file.readlines()
    file.close()

    chapter_index = file_to_read.pop(0).replace('\n','').split("\t")
    file_to_read.pop(0)
    output("landing",chapter_index,"#Autogenerated, do not edit.\n\n")

    for line in file_to_read:
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
            output('alias',chapter_index,f"{first}\t{second}\n")
        elif second != '':
            phrases.append(second)
        else:
            output('landing',chapter_index,f"label {title}_menu:\n")
            output('landing',chapter_index,f"    scene {title}\n")
            for phrase in phrases:
                output('landing',chapter_index,f"    \"{phrase}\"\n")
            output('landing',chapter_index,f"    jump {title}_menu\n\n")

            title = ""
            phrases = []

#parse_landing("A")
