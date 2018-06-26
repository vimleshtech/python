##dynamic list
'''
data = [] # declare empty list

for i in range(0,5):
    d = input('enter data :')
    data.append(d)


print data
'''


## create crud (create, read, updte, delete) app

sale = []

while True:

    op = input('enter 1. for add 2. for read 3. for update 4. delete and 5. for exit')
    
    if op==1:
        d =input('enter data :')
        sale.append(d)
    elif op==2:
        print sale

    elif op ==3:
        i =input('enter idex to update :')
        u = input('enter new value :')
        sale[i] = u
    elif op==4:
        u = input('enter data to remove :')
        if u in sale:
            sale.remove(u)
        else:
            print  'data is not exist'
    elif op==5:
        print 'end of program'
        break
    else:
        print 'invalid choice'
        


    


            



            
        

    

        
            
    
        

        


        
