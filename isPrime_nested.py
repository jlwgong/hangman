# Create a function that calls another function

# Task:
#   Create a function that tells us all the prime numbers up to some number
#   For example:
#         Output all the prime numbers up to 10
#         Output: 1, 2, 3, 5, 7


def isPrime(number):

    number_is_prime = True

    for i in range(2, number):

        remainder = number % i

        if remainder == 0:
            number_is_prime = False

    return number_is_prime



def get_prime_numbers(upper_range):

    for i in range(1, upper_range):

        if isPrime(i) == True:

            print(i, " is a prime number!")

    return None

