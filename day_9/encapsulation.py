'''

How to provide security to the data?
    To provide security, we have to use access specifiers.
        1. public
        2. protected (Soft Barrier->'_')
        3. private

Access Specifier:
    It described who can access the class members(properties & methods)

'''

## Example 
# class Temp:
#     a, b, *c, d = 'HELLO'

#     def greeting(self):
#         print('Good Afternoon: ')


# print(Temp.a, Temp.b, Temp.c, Temp.d)


## --Protected Access Specifier--
# class Temp:
#     # Soft Barrier
#     _a = 10
#     _b = "I Love CPP !"

# obj = Temp()
# print(obj.__a)
# print(obj._b)


## --Private Access Specifier--
# class Temp:
#     __a = 10
    
#     def __status(self):
#         print("I Love CPP !")

#     def get(self):
#         print(self.__a)

#     def set(self, new_val):
#         self.__a = new_val        

# obj = Temp()  
# print(obj.__a)  ## cant access like this
# obj.__status()  ## cant access like this



'''
1. By using Syntax
2. get & set method
3. by using @property decorator(setter)
'''

##--By using Syntax--
'''
obj_name/class_name._CN__prop_name/__method_name (Accessing)
obj_name/class_name._CN__MemberName = NewValue (Modifier)
'''

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()

# def new_method():
#     print('Method defination got changed !')

# obj._Temp__a = '0123456789'
# obj._Temp__status = new_method
# print(obj._Temp__a)
# # obj._Temp__status()

# obj = Temp()
# obj.get()
# obj.set(1)
# obj.get()
# print(obj._Temp__a)


## By using @pr