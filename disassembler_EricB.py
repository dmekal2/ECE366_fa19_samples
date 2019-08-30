#MIPS byline expandable disassembler
#Author: Eric Bauer
import numpy as np


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
            commhex= commhex.lower()
            if commhex =='exit' or commhex=='quit':
                print('Goodbye.')
                break
            elif len(commhex)!=8:
                print('Not a valid command.')
            
            
            for x in range(8):
                val=hexdecode(commhex[7-x])
                if str(val)==val:
                    break
                commbin+= pow(16,x)*val
            types = commbin>>26
            
            if types==0:
                #r-type
                self.rtype(commbin)
            elif types > 3:
                #i-type
                self.itype(commbin)
            else:
                print('Not a supported command.')

    def rtype(self,command):
        rs = 0x1f & (command >> 21)
        rt = 0x1f & (command >> 16)
        rd = 0x1f & (command >> 11)
        sh = 0x1f & (command >> 6)
        func = 0x3f & command

        if func == 0x20:#add
            print('add ${},${},${}'.format(rd,rs,rt))
            self.reg[rd]=self.reg[rs]+self.reg[rt]
        else:
            print('Not a supported command.')


    def itype(self,command):
        opcode= 0x3f & (command >> 26)
        rs = 0x1f & (command >> 21)
        rt = 0x1f & (command >> 16)
        imm = np.int16(0xffff & command)

        if opcode == 8:#addi 
            print('addi ${},${},{}'.format(rt,rs,imm))
        else:
            print('Not a supported command.')
            

    
object1=decoder()
object1.run()
