# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)


# user = {
#     'username': 'admin',
#     'password': '****'
# }

# un = input('Enter your username: ')
# pwd = input('Enter your password: ')

# if un == user['username'] and pwd == user['password']:
#     print('Login successful!')
# else:
#     print('Invalid username or password.')

# print('The program has ended !!')


char = input('Enter a character: ')
if chr in 'aeiouAEIOU':
    print(f'{char} is a vowel.')
elif chr in '0123456789' :
    print(f'{char} is a digit.')
elif chr not in 'asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM1234567890':
    print(f'{char} is a special character.')
else :
    print(f'{char} is a consonant.')