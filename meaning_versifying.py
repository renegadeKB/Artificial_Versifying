#to do
#make basic take in 6 numbers',' export poem
#then make a function to take in strings',' and make them "encrypted" in the versifying latin way
#make the function that then takes in numbers and accesses them



#IDEAS FOR FURTHER COMPLEXITY
#make a way to count english vowel length and make the poem based off of that
#make a proper english translation',' lacking the
#friendlier GUI

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
    print(output)
    return output



def main():

    adverbs = ['1','4','5','9']

    if len(sys.argv) != 2 or len(sys.argv[1]) != 6:
        printHelp()
    output = ''
    for char in sys.argv[1]:
        try:
            int(char)
        except ValueError:
            printHelp()
    chart =  [['worst', 'ugly', 'abrasive', 'sorrowful', 'confusing', 'bitter', 'filthy', 'disloyal', 'dishonest'], ['gift', 'words', 'vows', 'laws', 'wars', 'fates', 'the finished', 'declared words', 'the damaged '], ['other', 'I think', 'you see', 'to the evil', 'for a man', 'I say', 'for you', 'for me', 'I know'], ['will produce', 'will yield', 'yield', 'promise', 'will bear', 'will show', 'take care of', 'declare', 'encourage'], ['quarrels', 'decrees', 'seasons', 'verdicts', 'pacts', 'wagers', 'dreams', 'stars', 'cups'], ['always', 'wicked', 'lone', 'clearly', 'only', 'certain', 'a certain', 'many', 'often']]
    encoded = avEncode(chart)
    i = 0

    outputList = []
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
                # time.sleep(.2)

                j+=1
                counter+=1
            if(encoded[i][j]=='*'):
                break
            print('counter:',counter,'new added letter:',encoded[i][j], end = '\r')
            # time.sleep(.5)
            output+=encoded[i][j]
            counter = 0
        outputList.append(output)
        output=''
        i+=1

    clear()

    print()
    outputList[0] = 'the ' + outputList[0]
    if(sys.argv[1][-1] in adverbs):
        outputList = outputList[0:3] + [outputList[-1]] + outputList[3:5]
    else:
        outputList = outputList[0:4] + [outputList[5],outputList[4]]
    if(sys.argv[1][2] == '3'):
        outputList[2] = 'that '+outputList[2]
    elif(sys.argv[1][2] == '2'):
                outputList = [outputList[2]+' that'] + outputList[0:2]+outputList[3:]

    elif(sys.argv[1][2] == '6'):
                outputList = [outputList[2]+' this'] + outputList[0:2]+outputList[3:]
                outputList[1] = '"' + outputList[1]
                outputList[-1] = outputList[-1]+'"'
    outputList[-2]
    print((' '.join(outputList)+'.').replace('".','."').capitalize())

main()
