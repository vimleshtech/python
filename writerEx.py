data = open(r'C:\Users\vkumar15\Desktop\words.txt','r')

w1 =open(r'C:\Users\vkumar15\Desktop\odd.txt','w')
w2 =open(r'C:\Users\vkumar15\Desktop\even.txt','w')

f = True

for r in data.readlines():

     if f:
          w1.write(r)
          f = False
     else:
          w2.write(r)
          f = True

w1.close()
w2.close()

          
     

