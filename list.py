## list
#in
#not in
#loop

#break
#continue



## tuple
## dict
# string

#list

#a = [111,222,1,2,23,44]
#print (a)

#print(max(a)) #return highest value
#print(min(a))#return lowest value
#print(sum(a))#return total (sum of all elements)
#print(len(a)) # return count of elements 

#a.sort()
#print(a)  # print sorted data in ascending 
#print(a[2]) 
#print(a[1:3]) #slicing

#print(a[::-1])  # print sorted data in descending

#append value : at last position
#a.append(100)
#print(a)


#insert : add new element at given position
#a.insert(3,2223344)
#print(a)

#remove element
#a.remove(100)
#a.remove(a[2])

#print(a)


## add data dynamically in list
#sales = []
#s = int(input('size of list  :'))
#for i in range(0,s):
    
#    sales.append(int(input('enter data  :')))
    

#print(sales)


#in
#if 100 in sales:
#    print ('match ')
#else:
#    print('not match')
    

    
#WAP which finds the locations and values of largest and second largest element in a one dimensional array.

a=[2,5,12,43,32,11,97]
a.sort()


print(len(a)-1,a[len(a)-1])
print(len(a)-2,a[len(a)-2])



####
# plz press 1 for addition , 2 for sub, 3 for mul , 0 for exit



#a = int( input('enter data :'))
#b = int( input('enter data :'))

#break :  to terminate the iterations


#while True:
    
#    ch = int(input('enter your choice:  plz press 1 for addition , 2 for sub, 3 for mul , 0 for exit'))
        
#    if ch  == 1:
#        c = a+b
#        print (c)

#    elif ch ==2:
#        c = a-b
#        print (c)

#    elif ch ==3:
#        c = a*b
#        print (c)
#    elif  ch == 0:
#        print('you have enter 0 for exit ')
#        break
#    else:
#        print('invalid choice ')


        
        
#continue :  to terminate the current interation

#i =0
#while i<10:
    
#    i =i+1
    
#    if i%3 == 0:
#       continue

#    print(i)


#to shift negative numbers to left 3, -5, 1, 3, 7, 0, -15, 3, -7, -8

lis=[3, -5, 1, 3, 7, 0, -15, 3, -7, -8]
count=len(lis)-1
print(count)

l1=[]
l2=[]


for d in lis:
        
    #print(d)
    if d<0:
       l1.append(d)   
    else:
        l2.append(d)

            
## tuple
days = ('mon','tue','we','thu')
if 'mon' in days:
    print('match')
else:
    print('nont match')
    
## dict
words = {1:'one',2:'two',3:'three'}

i = int(input('enter key to search : '))
print(words[i])


    
# string

s ="raman sinha"
print(len(s))

d = list(s)
print(d)


d = s.split(' ')
print(d)

d = s.replace('a','xy')
print(d)


d = d.upper()
print(d)



d = d.lower()
print(d)

print(s[1:3])# slicer 












