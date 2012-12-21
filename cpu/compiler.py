import fileinput
import sys
import re

filename = str(sys.argv[1]) # accept the name of the assembly file as a command line argument
reader = fileinput.input(filename)

count = 0 # we want to count the number of instructions for later

for line in reader: 
    words = line.split()
    numwords = len(words)
    if numwords >= 3: #all instructions must have 3 or more components

        #R type instructions

        if words[0] == "add":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rtbin = bin(int(words[3][1:]))
            rt = str(rtbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            instrbin = "000000" + rs + rt + rd + "00000" + "100000"

        elif words[0] == "sub":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rtbin = bin(int(words[3][1:]))
            rt = str(rtbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            instrbin = "000000" + rs + rt + rd + "00000" + "100010"

        elif words[0] == "mul":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rtbin = bin(int(words[3][1:]))
            rt = str(rtbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            instrbin = "000000" + rs + rt + rd + "00000" + "011000"

        elif words[0] == "div":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rtbin = bin(int(words[3][1:]))
            rt = str(rtbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            instrbin = "000000" + rs + rt + rd + "00000" + "011010"

        elif words[0] == "and":
            funct = bin(int('20',16))
            print "000000"

        elif words[0] == "or":
            funct = bin(int('20',16))
            print "000000"

        elif words[0] == "slt":
            print "000000"

        elif words[0] == "sllv":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            shamtbin = bin(int(words[3]))
            shamt = str(shamtbin)[2:].zfill(5)
            instrbin = "000000" + rs + "00000" + rd + shamt + "000000"

        elif words[0] == "srlv":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            shamtbin = bin(int(words[3]))
            shamt = str(shamtbin)[2:].zfill(5)
            instrbin = "000000" + rs + "00000" + rd + shamt + "000010"

        elif words[0] == "srav":
            rsbin = bin(int(words[2][1:]))
            rs = str(rsbin)[2:].zfill(5)
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            shamtbin = bin(int(words[3]))
            shamt = str(shamtbin)[2:].zfill(5)
            instrbin = "000000" + rs + "00000" + rd + shamt + "000011"

        elif words[0] == "beq":
            print "000000"

        elif words[0] == "j":
            print words[0]

        #I type instructions

        elif words[0] == "li":
            rdbin = bin(int(words[1][1:]))
            rd = str(rdbin)[2:].zfill(5)
            immbin = bin(int(words[2][0:]))
            imm = str(immbin)[2:].zfill(16)
            instrbin = "001111" + rd + "00000" + imm
        elif words[0] == "sw":
            rsbin = bin(int(words[1][1:]))
            rs = str(rsbin)[2:].zfill(5)
            complicated = str(words[2])
            ind_paren = complicated.find('(')
            #print str(ind_paren)
            first_part_bin = bin(int(complicated[:ind_paren]))
            first_part = str(first_part_bin)[2:].zfill(5)
            int_parencl = complicated.find(')')
            secon_part = bin(int(complicated[ind_paren+1+1:len(complicated)-1],2))[2:].zfill(16)
            instrbin = "101011" + first_part + rs + secon_part
            #print instrbin

        print hex(int(instrbin,2))[2:].zfill(8) # this is the print statement

    count = count + 1

for i in range(65536-count): # the CPU accepts exactly 2^16 entries in its instruction memory
    print str(0).zfill(8) # fill the hex file with the missing entries