#MIPS byline expandable disassembler
#Author: Eric Bauer



def hexdecode(char):
    hexdict= {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15,
        }

    if char in hexdict:
        return hexdict[char]
    else:
        return 'invalid'


class decoder:
    def __init__(self):
        commhex=''
        commbin=0

    def run(self):
        while(1):
            commbin=0
            commhex=input("Please enter an 8-digit hex command  (or'exit' to quit)\n")
            if commhex =='exit' or commhex=='quit':
                print('Goodbye.')
                break
            elif len(commhex)!=8:
                print('Not a valid command.')
            
            
            for x in range(8):
                val=hexdecode(commhex[7-x])
                if str(val)==val:
                    print('whoops')
                    print(val)
                    break
                commbin+= pow(16,x)*val
            print(commhex)
            print(bin(commbin))
            print(commbin)
         

    
object1=decoder()
object1.run()
