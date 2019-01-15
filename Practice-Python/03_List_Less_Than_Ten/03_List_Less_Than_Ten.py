#Approach 1 by using lambda and filter
a = [1,1,2,3,5,8,13,21,34,55,89]

newlist = filter(lambda x:x<5, a)

print('Approach 1:')
print(newlist)

#Approach 2 by using append method to a new list
result = []
for x in a:
    if x < 5:
       result.append(x)
print("Approach 2:")
print (result)
