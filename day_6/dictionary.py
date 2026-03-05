##Dictionatry

'''
1. get
2. pop
3. popitem
4. clear
5. update
6. key
7. values 
8. items
'''

'''--get()--'''
# d = {1:1, 2:2, (1,2,3):(1,2,3)}
# print(d.get(2))



# user = {
#     'username' : 'user123',
#     'password' : '*****',
#     'location' :  'INDIA'
# }
# print(user)

# print(user.pop('location'))
# print(user)

# print(user.pop('username', 'password'))
# print(user)

# print(user.pop('password'))
# print(user)



'''--popitem--'''
# user = {
#     'username' : 'user123',
#     'password' : '*****',
#     'location' :  'INDIA'
# }
# print(user.popitem())
# print(user.popitem())
# print(user.popitem())


'''--update--'''
# user = {
#     'username' : 'user123',
#     'password' : '*****',
#     'location' :  'INDIA'
# }

# user.update({'password':'123'})## inside of it you should pass one dictionary
# print(user)
# user.update({'password':'asdfghjkl' , 'is_logged_in' : 'True'})
# print(user)



'''--keys--  ||  --values--  ||  --items--'''
# user = {
#     'username' : 'user123',
#     'password' : '*****',
#     'location' :  'INDIA'
# }
# print(user.keys())
# print(user.values())
# print(user.items())
