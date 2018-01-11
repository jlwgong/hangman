# This function tells a user whether or not a number is prime

def isPrime(number):

    # this will tell us if the number is prime, set to True automatically
    # We will set to False if the number is divisible by any number less than it
    number_is_prime = True

    # loop over all numbers less than the input number
    for i in range(2, number):

        # calculate the remainder
        remainder = number % i

        # if the remainder is 0, then the number is not prime by definition!
        if remainder == 0:
            number_is_prime = False

    # return result to the user
    return number_is_prime
