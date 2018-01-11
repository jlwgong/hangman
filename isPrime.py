# This function tells a user whether or not a number is prime

def isPrime(number):

    number_is_prime = True

    for i in range(2, number):

        remainder = number % i

        if remainder == 0:
            number_is_prime = False

    return number_is_prime
