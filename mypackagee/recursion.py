# recursion functions
def sum_array(array):

    '''Returns sum of all items in array'''
    num_sum = sum(array) '''sumimng the numbers in the array'''
    return num_sum '''it returns the sum of the array '''

#-----------------------------------------------------------------------------------
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    """Recursive function to print Fibonacci sequence"""
    if n <= 1: # it checks if the value of n is less or equal to one

        return n # it returns n if the value of n is less or equal to one
    else:
        return(fibonacci(n-1) + fibonacci(n-2)) # perform the Fibonacci calculations

#------------------------------------------------------------------------------------
def factorial(n):

    '''Return the n factorial'''
    if n == 0: # checks if n is equal to zero
        return 1
    else:
        return n * factorial(n-1) # compute the the n factorial
#------------------------------------------------------------------------------------
def reverse(word):

    '''Return word in reverse'''
    result = ''
    for i in reversed(word): # it sort the words in a reverse odder
        result += i # increament the value of in result by 1

    return result # turns the sorted word
