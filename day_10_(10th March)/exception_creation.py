'''

raise --> It is a keyword, which helps us to throw an error in between a program.

Exception Creation,

1. Custom Exception, (raise)
2. User-defined Exception, (raise)
3. Assertion Exception, (assert)
'''

'''
Custome Exception:
    1. We use pre-built Exception classes according to our requirement

    raise ValueError('message')

    ValueError: message
'''

# num = 16
# if num >= 18:
#     print('You are eligible for driving and voting')
# else:
#     raise ValueError('Age should be greater than or equal to 18 !')



















'''
Assertion Exception

-- Assertion exception can be created by using one keyword called "assert".

assert <condition>, print(ERROR)
print(output)
'''

s = input("Enter a string: ")
assert s == s[::-1], print("It is not a palindromic string !")
print("It is a palindromic string !")