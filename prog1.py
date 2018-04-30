a =1 # here a is variable / temp. memory and 1 is data or values 

print(type(a)) # int

a =222.2
print(type(a)) # float



a ='222.2'
print(type(a)) # str



a =True 
print(type(a)) # bool

a =[111,222,111,'22333']
print(type(a)) # list or array (collection of data)

a =("mon","tue","wed","thu") # tuple , is read only
print(type(a))
print(a[1])

#key:value 
d ={'a':'alpha','b':'beta','t':'tata'} # dict
print(type(d))
print(d['t'])



# 3.0+   default data type is string when data will come from console
# <3.0 default data type be as it is : exmple '1' - str,  1 - int


###input and output
a = input('enter name : ')
print('your data is  = ',a)

hs = input('enter score in hindi  : ')
es = input('enter score in english  : ')
cs = input('enter score in comp. sc.  : ')

#type cast/ convert before addition

total  =int( hs) + int(es)+ int(cs)


print('total score is  : ',total)
avg = total/3

print(avg)

if avg>80:
     print('Grade A')
elif avg>60:
     print('Grade B')
else:
     print('Grade C ')

     

     













































