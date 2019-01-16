input_number = input("PLease enter a number:")

divisor_list = []

for x in range(1, input_number +1):
    if input_number%x == 0:
        divisor_list.append(x)

print("\nList of all the divisor for {} is: ".format(input_number))  
print (divisor_list)

