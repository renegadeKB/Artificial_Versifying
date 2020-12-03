#to do
#make basic take in 6 numbers',' export poem
#then make a function to take in strings',' and make them "encrypted" in the versifying latin way
#make the function that then takes in numbers and accesses them



#IDEAS FOR FURTHER COMPLEXITY
#make a way to count english vowel length and make the poem based off of that
#make a proper english translation',' lacking the
import sys,os,time
import random as rand

def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def printHelp():
    print('\nusage: '+sys.argv[0]+' inputString\n\tinputString: must be six digits, no spaces. IE 123456')
    sys.exit(1)

def randChar(length):
    choices =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    outputString =''
    for i in range(0,length):
        outputString += rand.choice(choices)
    return outputString

def avEncode(chart):
    output = []
    for subChart in chart:
        #first 8 characters are filler
        i = 0
        j=7
        encString =''
        finished = 0
        while(finished < 9):
            while(True):
                word = subChart[j]
                if(word == '*'):
                    encString += '?'
                elif i >= len(word):
                    #at the end of the string
                    encString += '*'
                    subChart[j] = '*'
                    finished+=1
                else:
                    encString += word[i]
                j-=1
                if(j < 0):
                    j = 8
                elif(j == 7):
                    break
            i+=1
        output.append(encString)
    return output



def main():


    if len(sys.argv) != 2 or len(sys.argv[1]) != 6:
        printHelp()
    output = ''
    for char in sys.argv[1]:
        try:
            int(char)
        except ValueError:
            printHelp()
    chart = [['pessima','turpia','horrida','tristia','turbida','aspera','sordida','impia','perfida'],['dona','verba','vota','iura','bella','fata','facta','dicta','damna'],['aliīs','reor','vides','mālīs','viro','inquam','tibi','Mihi','scio'],['producunt','concedunt','causabunt','promittunt','portabunt','monstrabunt','procurant','prædicunt','confirmant'],['iurgia','dogmata','tempora','crimina','fœdera','pignora','somnia','sidera','pocula'],['semper','prava','sola','plane','tantum','certa','quædam','multa','sæpe']]
    encoded = avEncode(chart)
    i = 0

    for char in sys.argv[1]:
        j = 0
        counter = int(char)+1
        if(counter == 10):
            counter = 1

        while(True):
            clear()

            print(output,end='\n')
            #could just do 9 - i and get that character, then add 9 until *
            while(counter < 9):
                print('counter:',counter,'current letter:',encoded[i][j], end = '\r')
                time.sleep(.2)

                j+=1
                counter+=1
            if(encoded[i][j]=='*'):
                break
            print('counter:',counter,'new added letter:',encoded[i][j], end = '\r')
            time.sleep(.5)
            output+=encoded[i][j]
            counter = 0
        output+=' '
        i+=1



    print()
    print(output)

main()
