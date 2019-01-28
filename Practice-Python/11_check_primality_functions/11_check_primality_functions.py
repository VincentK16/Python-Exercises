def isprimary(num):
   list = range(2,num//2 +1) #range(2, 7), meaning the input number will be divided by number 2 to 6. Not to start from 1 is not a prime number. We are using'//' here for integer division instead of float division '/'
   print(list)
   primary = True
   for element in list:
      if num%element == 0:
         primary = False
         break

   if primary:
      print("{} is a primary number!".format(num))
   else:
      print("{} is not a primary number!".format(num))

if __name__=='__main__':
    num= int(input('What is your favoruite number?'))
    isprimary(num)
