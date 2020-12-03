#to do
#make basic take in 6 numbers',' export poem
#then make a function to take in strings',' and make them "encrypted" in the versifying latin way
#make the function that then takes in numbers and accesses them



#IDEAS FOR FURTHER COMPLEXITY
#make a way to count english vowel length and make the poem based off of that
#make a proper english translation',' lacking the
import sys
def printHelp():
    print('\nusage: '+sys.argv[0]+' inputString\n\tinputString: must be six digits, no spaces. IE 123456')
    sys.exit(1)

def main():

    chart = [['pessima','turpia','horrida','tristia','turbida','aspera','sordida','impia','perfida '],['dona','verba','vota','iura','bella','fata','facta','dicta','damna'],['aliīs','reor','vides','mālīs','viro','inquam','tibi','Mihi','scio'],['producunt','concedunt','causabunt','promittunt','portabunt','monstrabunt','procurant','prædicunt','confirmant'],['iurgia','dogmata','tempora','crimina','fœdera','pignora','somnia','sidera','pocula'],['semper','prava','sola','plane','tantum','certa','quædam','multa','sæpe']]
    if len(sys.argv) != 2 or len(sys.argv[1]) != 6:
        printHelp()
    output = []
    i = 0
    for char in sys.argv[1]:
        if(char == '9'):
            char = '8'
        try:
            output.append(chart[i][int(char)-1])
        except ValueError:
            printHelp()
        i+=1
    print()
    print(' '.join(output))

main()
