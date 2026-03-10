file = open('temp.txt', 'w+')
# file.write('This is the first line')
file.writelines([
    'First line\n',
    'Second line\n',
    'Third line\n',
    'Fourth line\n',
    'Fifth line\n',
    'Sixth line\n',
])

##To make the python interpreter to point a specific index, we use seek (index).
file.seek(0)
print(file.read())


file.close()


