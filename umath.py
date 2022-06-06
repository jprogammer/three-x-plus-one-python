# three x plus one v0.1 © Jameson Sisk 2022

def three_x(number): # this function performs the three x plus one problem with a number as input
    print(number)
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = (3 * number) + 1
            print(number)

def even(number): # this can independently check to see if a number is even
    if number % 2 == 0:
        is_even = True
        print("Even")
    else:
        is_even = False
        print("Not Even")

def odd(number): # this can independently check to see if a number is odd
    if number % 2 != 0:
        is_odd = True
        print("Odd")
    else:
        is_odd = False
        print("Not Odd")
