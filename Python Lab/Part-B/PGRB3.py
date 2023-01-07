# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueLargeError(Error):
    """Raised when the input value is too large"""
    pass

# you need to guess this number
number = 50
# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueSmallError
        elif i_num > number:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("This value is small, try again!")
        print()
    except ValueLargeError:
        print("This value is large, try again!")
        print()
        print("Congratulations! You guessed it correctly.")
