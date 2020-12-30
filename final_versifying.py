#to do
#make basic take in 6 numbers',' export poem
#then make a function to take in strings',' and make them "encrypted" in the versifying latin way
#make the function that then takes in numbers and accesses them



#IDEAS FOR FURTHER COMPLEXITY
#make a way to count english vowel length and make the poem based off of that
#make a proper english translation',' lacking the
#friendlier GUI

import sys,os,time
import random
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def printHelp():
    print('\nusage: '+sys.argv[0]+""" inputString [-db] [-!v] [-c i]
\tinputString: must be six digits, no spaces. IE 123456
\t-db: Debug mode, outputs 100 random poems into outputs.txt
\t-!v: Speeds up the process by not printing.
\t-c x: choose a specific chart to generate from:
\t\t0: Original Latin
\t\t1: Translated
\t\t2: Translated with Hexameter (Default)
\t\t3: Latin with 2's word order
                                """)
    sys.exit(1)

def randChar(length):
    choices =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    outputString =''
    for i in range(0,length):
        outputString += random.choice(choices)
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
                    # encString += '?'
                    encString += randChar(1)

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

def versify(input, encoded, verbose):
    output = ''
    for char in input:
        try:
            int(char)
        except ValueError:
            printHelp()

    i = 0
    outputList = []
    for char in input:
        j = 0
        counter = int(char)+1
        if(counter == 10):
            counter = 1
        while(True):
            if(verbose):
                clear()
                print(output,end='\n')
            #could just do 9 - i and get that character, then add 9 until *
            while(counter < 9):
                if(verbose):
                    print('counter:',counter,'current letter:',encoded[i][j], end = '\r')
                    time.sleep(.1)
                j+=1
                counter+=1
            if(encoded[i][j]=='*'):
                break
            if(verbose):
                print('counter:',counter,'new added letter:',encoded[i][j], end = '\r')
                time.sleep(.3)
            output+=encoded[i][j]
            counter = 0
        outputList.append(output.lower())
        output=''
        i+=1
    return(' '.join(outputList)+'.').replace('".','."').capitalize().replace(' i ',' I ')

def main():
    cIndex = '2'
    debug = False
    verbose = True
    cIndexes = ['0','1','2','3']
    if len(sys.argv) < 2 or len(sys.argv[1]) != 6 or len(sys.argv) > 6:
        printHelp()
    i = 2
    while i < len(sys.argv):
        entry = sys.argv[i]
        if(entry == '-db'):
            debug = True
        elif(entry == '-!v'):
            verbose = False
        elif(entry == '-c'):
            cIndex = sys.argv[i+1]
            i+=1
            if cIndex not in cIndexes:
                printHelp()
        else:
            printHelp()
        i+=1
    chartDict = {
        '0':[['Pessima', 'Turpia', 'Horrida', 'Tristia', 'Turbida', 'Aspera', 'Sordida', 'Impia', 'Perfida'], ['dona', 'Verba', 'Vota', 'Iura', 'bella', 'fata', 'facta', 'Dicta', 'damna'], ['aliis', 'reor', 'vides', 'malis', 'viro', 'inquam', 'tibi', 'Mihi', 'scio'], ['Producunt', 'concedunt', 'causabunt', 'Promittunt', 'portabunt', 'monstrabunt', 'procurant', 'Prædicunt', 'confirmant'], ['iurgia', 'dogmata', 'tempora', 'crimina', 'fœdera', 'pignora', 'somnia', 'Sidera', 'pocula'], ['Semper', 'Prava', 'Sola', 'Plane', 'Tantum', 'Certa', 'quædam', 'Multa', 'sæpe']],
        '1':[['pathetic', 'hideous', 'abrasive', 'dejected', 'disordered', 'rancorous', 'polluted', 'disloyal', 'dishonest'], ['rewards', 'comments', 'pledges', 'decrees', 'battles', 'outcomes', 'triumphs', 'remarks', 'losses'], ['the rest', 'i think', 'you watch', 'for sin', 'for man', 'i say', 'for you', 'to me', 'I know'], ['will create', 'will withdraw', 'bring about', 'guarantee', 'will carry', 'will present', 'take care of', 'shall profess', 'empower'], ['bickerings', 'precedents', 'periods', 'evidence', 'promises', 'hostages', 'fantasies', 'galaxies', 'chalices'], ['always', 'wicked', 'lonely', 'clearly', 'only', 'certain', 'unique', 'many', 'often']],
        '2':[['for them', 'I think', 'you know', 'through spite', 'For a man', 'I say', 'for you', 'for me', 'I know'], ['pitiable', 'horrible', 'boisterous', 'morose', 'difficult', 'rancorous', 'tarnished', 'traitorous', 'fraudulent'], ['gifts', 'words', 'vows', 'laws', 'wars', 'fates', 'deeds', 'talks', 'costs'], ['will create', 'will give up', 'do produce', 'do maintain', 'will endure', 'will display', 'do dictate', 'do proclaim', 'do augment'], ['imminent', 'villainous', 'desolate', 'palpable', 'just those', 'definite', 'different', 'numerous', 'regular'], ['battles', 'edicts', 'seasons', 'verdicts', 'pledges', 'wagers', 'ideas', 'night stars', 'goblets']],
        '3':[['aliis', 'reor', 'vides', 'malis', 'viro', 'inquam', 'tibi', 'Mihi', 'scio'],['Pessima', 'Turpia', 'Horrida', 'Tristia', 'Turbida', 'Aspera', 'Sordida', 'Impia', 'Perfida'], ['dona', 'Verba', 'Vota', 'Iura', 'bella', 'fata', 'facta', 'Dicta', 'damna'], ['Producunt', 'concedunt', 'causabunt', 'Promittunt', 'portabunt', 'monstrabunt', 'procurant', 'Prædicunt', 'confirmant'], ['Semper', 'Prava', 'Sola', 'Plane', 'Tantum', 'Certa', 'quædam', 'Multa', 'sæpe'],['iurgia', 'dogmata', 'tempora', 'crimina', 'fœdera', 'pignora', 'somnia', 'Sidera', 'pocula']]}


    encoded = avEncode(chartDict[cIndex])


    if debug:
        fullOutput = []
        digits = ['1','2','3','4','5','6','7','8','9']
        while(len(fullOutput)< 100):
            input = random.choice(digits)+random.choice(digits)+random.choice(digits)+random.choice(digits)+random.choice(digits)+random.choice(digits)
            fullOutput.append(versify(input, encoded, False))

        with open('outputs.txt','w') as outFile:
            for outp in fullOutput:
                outFile.write(outp+'\n')
    else:
        print(versify(sys.argv[1], encoded, verbose))




main()
