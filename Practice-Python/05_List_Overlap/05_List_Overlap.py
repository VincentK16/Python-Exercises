
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

list_1 = set(a)
list_2 = set(b)

match = []

for x in list_1:
   if x in list_2:
      match.append(x)
print('List 1: {}'.format(a))
print('List 2: {}'.format(b))
print('The overlapped numbers are: {}'.format(match))
