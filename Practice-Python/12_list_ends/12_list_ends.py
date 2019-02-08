import random

def listend():

   list_new=[list_1[0], list_1[-1]]
   return list_new

if __name__ =='__main__':

   list_1=list(random.sample(range(0,20), random.randint(0,15)))
   
   result=listend()
   print("List:{}".format(list_1))
   print("First and Last: {}".format(result))
