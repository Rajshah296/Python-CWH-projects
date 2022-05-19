def factorial(no) :
    """ param : number
        return : Factorial of a number. """
    return 1 if no == 0 else no * factorial(no - 1)

def fibo(no) : 
    """ param : integer
        returns : Fibonacci series value of the number on that position(The position is the argument passed). """
    return 0 if no == 1 else 1 if no == 2 or no == 3 else fibo(no - 1) + fibo(no - 2) 

def main() : 
    no = int(input("Enter the number : "))
    print(factorial(no))
    print(fibo(no))
if __name__ == '__main__' : 
    main()