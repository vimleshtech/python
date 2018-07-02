a =[[1,'raman','male','india',23333],[2,'adi','male','india',2333],[3,'ankita','female','india',23339],[4,'chahat','female','india',233731],[5,'tanya','female','india',23567],[6,'arya','male','india',23673],[7,'mohit','male','india',233764],[8,'rahul','male','india',23387]]

print(type(a))



#w2 =(r'\a\male.txt','w')
#w1 =(r'\a\female.txt','w')

'''

print(w1)
print(w2)
'''
s = input('enter type of data to be searched:')
c = 0
for d in a:
    if s==d:
       c = c+1
    print('no of times:',c)

