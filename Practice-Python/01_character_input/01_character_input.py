if __name__ == "__main__":  
    name= raw_input("Please enter your name:")
    age= int(input("Please enter your current age: "))
    year=int(input("Current year:"))

    message = ('\n' + name + ', You will be 100 years old in year ' + str(year - age + 100))

    print (message)
