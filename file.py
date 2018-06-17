#file hadling
# r - read
# w - write
# a - apped
# w+ -read and write
# a+ - read and append

f = open('C:\Users\Tech Vision\Desktop\AWS Session -01.txt','r')

#print f.read() #read all contents

#read first line
#print f.readline()

#read all lines and convert to list
data = f.readlines()

print data[2]
'''
for d in data:
    print d
'''



## wap to print row count
## wap to print row count in which row is present


f= open('C:\Users\Tech Vision\Desktop\AWS Session -01.txt','r')
num_lines=0
open(f,'r')
for line in f:
    print ("number of lines:")
    print num_lines









