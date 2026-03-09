#using the same method name or operator to perform two or more different operations.

class Temp:
    def sum(self, a, b):
        print(a+b)

    ## Monkey Patching.
    # It is a process of storing the prev method's address inside a variable before overriding the method
    # area's address. Using that var, we can access the prev method's method area. 
    add_two_sum = sum

    def sum(self, a, b, c):
        print(a+b+c)

obj = Temp()
obj.add_two_sum(10,20)
obj.sum(10,20,30)

## In python, if we want to perform method overloading then it will act as method overriding.

## In other programming languages, based upon no of arguments, the respective method bolck will get executed.
# But in python , it never happens

## Method Overriding is a phenomenon of overriding the prev method's address with the latest one.

