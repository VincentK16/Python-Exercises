
a=[1,4,9,16,25,36,49,64,81,100]

print("Original List: {}".format(a))
#Approach 1
newlist= filter(lambda x:x%2==0, a)
print("Approach 1 - Even element: {}".format(newlist))

#Approach 2
even = [number for number in a if number%2 ==0]
print("Approach 2 - Even element: {}".format(even))

userinput = input("Enter any 6 numbers you like (seperated by comma ','): ")
userinput_2 = list(userinput)
output = filter(lambda x:x%2==0, userinput_2)
print ("Even element: {}".format(output))

#print (type (a))
#print (type(newlist))
#print (type(even))
#print (type(userinput))
#print (type(userinput_2))
#print (type(output))
