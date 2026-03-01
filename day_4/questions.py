'''#Question 1'''
# units = int(input("Enter units: "))
# total_bill = None

# if units > 0:
#     if units <= 100:
#         total_bill = units*5
#     elif 100 <= units <= 300 :
#         total_bill = 100*5 + (units-100)*7
#     else:
#         total_bill = units*10

#     if total_bill > 5000:
#         total_bill = total_bill*0.95
    
#     print(f'Total bill: {total_bill}')
# else:
#     print("Invalid input. Units must be greater than 0.")




'''#Question 2 loan approval system'''
# salary = int(input("Enter your salary: "))
# CIBIL_score = int(input("Enter your CIBIL score: "))
# if salary > 25000 and CIBIL_score > 700:
#     if salary > 50000 and CIBIL_score > 750:
#         print("Instant approval!")
#     else:
#         print("Loan approved after verification.")
# else:
#     print("Loan not approved.")




'''#Question 3 Check leap year'''
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


'''#Question 4 change lowercase to uppercase and uppercase to lowercase using ascaii values'''

# char = input('Enter a character: ')
# if 'a' <= char <= 'z':
#     uppercase_char = chr(ord(char) - 32)
#     print(f"Uppercase of '{char}' is '{uppercase_char}'")
# elif 'A' <= char <= 'Z':
#     lowercase_char = chr(ord(char) + 32)
#     print(f"Lowercase of '{char}' is '{lowercase_char}'")
# else:
#     print(f"'{char}' is not a alphabet.")





'''#Question 5 '''
# name = str(input('Enter user_name :'))
# result = None
# ans = ''
# for i in name :
#     if 65<= ord(i) <= 90 :
#         result = ord(i) + 32
#         ans += chr(result)
#     elif 97<= ord(i) <= 122 :
#         result = ord(i) -32
#         ans += chr(result)
#     else:
#         ans += i
# print(ans)




'''#Question 6'''
# list1 =eval(input("Write elements of list :"))
# # list1 = [1, 'Hello', 2.2, 99.9]
# max = list1[0]
# for i in list1 :
#     if type(i) in [int, float]:
#         if i > max:
#             max = i
# print(max)





'''#Question 7'''
# coll = {'a':1, 'b':2}
# new_coll = {}
# for i in coll:
#     new_coll[coll[i]] = i
# print(new_coll)



'''#Question 8'''
# coll = eval(input('Enter a collection'))
# new_coll = {}
# for i in coll:
#     if type(i) in [str, tuple]:
#         if len(i) % 2 == 0:
#             new_coll[i] = i[0] + i[-1]
#         else :
#             new_coll[i] = i[len(i)//2]
# print(new_coll)



## Whwnwvwe python intrepreter will wncounter "break" keyword it woll simply stop itd execution on this particular line and
## make the interpreter



col1 = [1, 1.2, 3, 4,5, 'hi']
i, flag = col1[0], True

for j in col1:
    if type(i) == type(j):
        flag = True
    else :
        flag = False
        break
if flag:
    print('Homogeneous collection')
else:
    print('Heterogeneous collection')