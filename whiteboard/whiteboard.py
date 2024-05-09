# Fizz Buzz 
# Given a random number as an input to a function,
# return "FIZZ" if the number is even and "BUZZ" if the number is odd

# input: 5
# output: "BUZZ"

# input: 4
# output: "FIZZ

def fizz_buzz(number):
    if number % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"
print(fizz_buzz(5))
print(fizz_buzz(4))