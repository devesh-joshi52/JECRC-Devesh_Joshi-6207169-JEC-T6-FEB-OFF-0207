''' --Herarchical--
It is a type of inheritance in which the properties will be derived from single parent class to multiple than one child class
'''

class Parent:
    gold = '2Kg'
    silver = '10Kg'
    no_of_flats = 12

class SmallestBrother(Parent):
    name = "Rickon"

class ElderBrother(Parent):
    ny_name = 'Rob'

class Sister(Parent):
    sis_name = 'Sansa'

print(SmallestBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)
