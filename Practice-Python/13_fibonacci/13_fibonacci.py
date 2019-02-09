def generateFibonacci(num):
   list=[1,1]
   for x in range(1, num-1):
      list.append(list[x-1]+list[x])
      print("List:{}".format(list))
   return list

if __name__ =='__main__':
    number=int(input("How many fibonaccies ? "))
    result=generateFibonacci(number)
    print("The Fibonacci are: {}".format(result))


