# FizzBuzz Challenge
# Author: Christopher
# Date: 9/8/2017
##
def fizzBuzz():
    counter = 1

    while(counter <= 100):
        if ((counter / 3).is_integer() or (counter / 3) == 1.0) and ((counter / 5).is_integer() or (counter / 5) == 1.0):
            print("FizzBuzz")
        else:
            if((counter / 3).is_integer() or (counter / 3) == 1.0):
                print("Fizz")
            else:
                if((counter / 5).is_integer() or (counter/5) == 1.0):
                    print("Fizz")
                else:
                    print(counter)
        counter = counter + 1
    return

fizzBuzz()    
            
