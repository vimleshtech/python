##
emp =[]
    

while True:

    op = input('press 2 for average 3. show data card 4.maximum 5.minimum 6.exit')

    if op==1:
        d = input('enter data ')
        emp.append(d)
        
        
    elif op==2:        
        avg=sum(emp)/len(emp)        
        print avg        
    elif op==3:        
        print emp
    elif op==4:
        print max(emp)
    elif op==5:   
        print min(emp)
    elif op==6:
        print 'exit'
        break


        
    
            
