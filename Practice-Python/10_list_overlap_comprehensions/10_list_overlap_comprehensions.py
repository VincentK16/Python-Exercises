import random

list1=list(random.sample(range(0,20), random.randint(1,15)))
list2=list(random.sample(range(0,20), random.randint(1,15)))

print("List 1:", list1)
print("List 2:", list2)

common = set([elem for elem in list1 if elem in list2])
common_list = list(common)
print("Common:", common_list)



