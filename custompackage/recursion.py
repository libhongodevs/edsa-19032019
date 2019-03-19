def sum_array(array):

    '''Return sum of all items in array'''

    if len(array) == 0:
        return 0
    else:
        return array[0] + sumArray(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    '''Return n!'''

    if n < 1:
        return 1
    else:
        x = n * factorial(n-1)
        return x

def reverse(word):

    '''Return word in reverse'''

    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]