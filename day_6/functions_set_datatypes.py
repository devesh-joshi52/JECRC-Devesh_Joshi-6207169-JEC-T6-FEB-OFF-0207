## FUnctions for Set Data Types
'''
1. add
2. remove
3. discard
4. pop :Randomly eleminate the values, single value at a time.
5. clear
6. union
7. intersection
8. difference
9. symmetric_difference
'''

from tokenize import Single3


s = {1, 2, True, False, 0, 3+9j} 
# print(s)## result ->{False, 1, 2, (3+9j)}

s.add(100)
# print(s)

# s.add([2,3,5]) ##error
s.add((1,2,3))
# print(s)

# s.remove(3+9j)
# print(s)
# s.remove(False)
# print(s)
# s.remove(10) ##error
# print(s)

# s.discard(1)
# print(s)
# s.discard(10) ##no error unlike remove
# print(s)


# s.pop()
# print(s)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
s1.union({2,3,8})
# print(s3)
# print(s1)