#array index start at 0 position 
data = [1111,222,33,44]
print type(data)

print data
data.append(100)
print data

data.insert(1,200)
print data 

data.pop()
print data 

data.remove(222)
print data


print max(data)
print min(data)
print sum(data)

data.sort()
print data

print len(data)

##acess value index
print data[2] # show 3rd element

#slicing
print data[0:2] # 0th ,1st index <less than 2
print data[:2] #from 0

print data[:-1]#last 

##print fron between
print data[2:4]

#print in reverse
print data[::-1]
























