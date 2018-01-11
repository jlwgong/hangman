# Create a function that calls another function

# Task:
#   Create a function that tells us all the prime numbers up to some number
#   For example:
#         Output all the prime numbers up to 10
#         Output: 1, 2, 3, 5, 7


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


# print out all prime numbers in range
def print_prime_numbers(upper_range):

    # loop over all numbers in the given range
    for i in range(1, upper_range):

        # use isPrime function to check if that number is prime
        if isPrime(i) == True:

            # if that number is prime, print it out!
            print(i, " is a prime number!")

    # no results to return to the user, results are printed out already
    return None

# create a list of all prime numbers in range
def get_prime_numbers_list(upper_range):

    # create an empty list
    prime_numbers = []

    # loop over all numbers in the given range
    for i in range(1, upper_range):

        # use isPrime function to check if that number is prime
        if isPrime(i) == True:

            # if that number is prime, add it to the list of prime numbers
            prime_numbers.append(i)

    # return list of prime numbers to the user
    return prime_numbers
