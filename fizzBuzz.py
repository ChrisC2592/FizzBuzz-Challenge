# FizzBuzz Challenge
# Author: Christopher
# Date: 9/8/2017
##
def fizzBuzz():
    counter = 1

    while(counter <= 100):
        if ((counter % 3) == 0) and ((counter % 5) == 0):
            print("FizzBuzz")
        else:
            if ((counter % 3) == 0):
                print("Fizz")
            else:
                if ((counter % 5) == 0):
                    print("Buzz")
                else:
                    print(counter)
        counter = counter + 1
    return

fizzBuzz()
