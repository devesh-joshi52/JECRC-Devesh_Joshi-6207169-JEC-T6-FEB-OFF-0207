## Create a function which will take n numbers of input from user and return the sum of only int & floating point numbers.
# Please make sure that, user is capable of passing all  types of values.

# def sum_numbers(*args):
#     total = 0

#     for i in args:
#         if type(i) == int or type(i) == float:
#             total += i
#     print(f'Sum is: {total}')

# sum_numbers(2,3,4,5,6,)


'''Synatx
def func_name(**kwargs):
    Statement
    Block

func_name(k1=v1, k2=v2, ...., kn=vn)
# All the key names should be a string but you can't use quotes

'''
# def print_details(**kwargs):
#     print(kwargs)

# print_details(username='user123', password='****', logged_in_device=['Android', 'Windows', 'Linux'])


# def sum_numbers(*args):
#     total = 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#             total += i
#     print(f'Sum is: {total}')

# sum_numbers(*eval(input('Enter a list of values: ')))
# ## sum_numbers(*[1, 2, 3, 4, 5])
## sum_numbers(*[1, 2, 3, 4, 5])





## Create a function which will return a list of prime numbers. Please make sure that user can pass n input.
## For checking whether a number is prime or not, you can create one function.

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num/2) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_nums(*args):
    primes = []
    for num in args:
        if isPrime(num):
            primes.append(num)
    return primes


print(find_prime_nums(*eval(input("Enter a list of nums: "))))
