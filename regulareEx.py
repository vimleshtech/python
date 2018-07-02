import re # pattern matching

'''
/d  : digit
/w  : chars
/D   : non digit
/W   : non char
[a-z,0-9]  :
(.*)   : group , . any char, *  any no. of times
{min length, max lenght}

match()
search()
group()
etc.
'''
data  = input('read data  :')
o =  re.match(r'(.*) are (.*)',data)

if o:
     print ('data is matched')
else:
     print ('data is not matched ')
     
##email account validation
email = input('enter email id :')
o =  re.match(r'(.*)@gmail.com',email)

if o:
     print ('valid gmail email id')
else:
     print('not valid email id')
     

     






