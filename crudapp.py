# CRUD : CREATE ,READ ,  UPDATE,  DELETE 
#remove
#update
#sort
#search
## declare empty list
emps  = []
while True:
    op  = input('enter 1. for add 2. for show and 3. remove 4. update 5.search 6.sort 7. for exit')    
    if op ==1:
        eid = input('enter eid :')
        ename = raw_input('enter ename :')
        sal = input('enter sal :')
        row=[]
        row.append(eid)
        row.append(ename)
        row.append(sal)
        emps.append(row)

    elif op ==2:
        #emps[0][1]
        for row in emps:
            print row

    elif op==3:
        eid = input('enter eid to remove')
        if eid in row:
            emps.remove(row)
        else: 
            print'not found'
    elif op==4:
        eid=input('enter eid to update')
        if eid in row:
            ip=input('1. update name 2. update salary 3. update eid')
            if ip==1:
                v=emps.index(eid)
                ename=raw_input('enter new name')
                emps.insert([v][1],ename)
            if ip==2:
                v=emps.index(eid)
                esalary=input('enter new salary')
                emps.insert([v][2],esalary)
        
         
    #elif op==5:
    #elif op==6:

    elif op ==7:
        break
    

    else:
        print 'invalid choice'


        
