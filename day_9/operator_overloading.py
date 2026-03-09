class MyDataType:
    def __init__(self,val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, *ano_obj):
        total = self.val
        for i in ano_obj:
            total += i.val
        return MyDataType(total)
    
    def __sub__(self, *ano_obj):
        total = self.val
        for i in ano_obj:
            total -= i.val
        return MyDataType(total)
   
    def __mul__(self, *ano_obj):
        total = self.val
        for i in ano_obj:
            total = total*i.val
        return MyDataType(total)
    
    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val
    
    def __trudiv__(self, ano_obj):
        return self.val / ano_obj.val

    def __mod__(self, ano_obj):
        return self.val % ano_obj.val

    ## self.val
    ## obj -> self.val
    ##ano_obj (obj2) --> obj2.val --> ano_obj.val


obj1 = MyDataType(10)
obj2 = MyDataType(20)
obj3 = MyDataType(30)

sum = obj1 + obj2 + obj3
print(sum)
sub = obj1 - obj2 - obj3
print(sub)
mul = obj1 * obj2 * obj3
print(mul)

# print(MyDataType(10) + MyDataType(20) + MyDataType(30))




