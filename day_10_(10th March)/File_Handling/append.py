file = open('jecrc.txt', 'a+')

# file.write("JECRC is the world's best university !")
# file.write("JECRC is also popular for it's placements !")

file.writelines([
    '\nHere, food is good\n',
    'ECO System is good\n',
    'Faculties are very supportive\n'
])
file.seek(0)
print(file.read())
file.close()