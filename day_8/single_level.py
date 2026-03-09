# --Single Level--
# We will have a single parent and child class. Also the properties will be derived only one time. 

class Parent:
    bank_balance = '50L'

    def __init__(self, members): ##PC
        self.members = members
    
    def desc(self):
        print('I am the parent class')

# Child Class or Sub Class 
# The class in which we are going to derive the properties, is known as Child class
class Child(Parent):
    def __init__(self, child_name, *args): ##CC
        self.child_name = child_name
        super().__init__(args)

    def desplay(self):
        super().desc()    


# obj = Child()
# print(Child.bank_balance)
obj = Child('Devesh', 'Mom', 'Dad')
print(obj.members)
print(obj.child_name)
obj.desc()  #or  Child.desc(obj)