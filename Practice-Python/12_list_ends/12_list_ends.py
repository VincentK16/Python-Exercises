import random

def listend(list):

   list_new=[list[0], list[-1]]
   return list_new

if __name__ =='__main__':

   list_1=list(random.sample(range(0,20), random.randint(0,15)))
   result=listend(list_1)
   list_2=list(random.sample(range(0,20), random.randint(0,15)))
   result_2=listend(list_2)
   print("List 1:{}".format(list_1))
   print("List 2: {}".format(list_2))
   print("First and Last: {}".format(result))
   print("First and Last for list 2: {}".format(result_2))
