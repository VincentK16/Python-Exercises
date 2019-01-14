#Bubble Sort algorithm: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

def buble_sort(lst):
    sorted=False
    while not sorted:
        swaps = 0
        non_swaps=0
        for index in range(len(lst)-1):
            
            if lst [index] > lst [index+1]:
                swaps +=1
                lst [index],lst[index+1] = lst [index+1], lst[index]
                print(swaps)
            else:
                non_swaps +=1
            print(lst)
        if swaps == 0:
            sorted = True
            print ("Buble sort return", lst)
                                
buble_sort([2,1,4,9,6,5])

#Output=[1,2,4,5,6,9]
