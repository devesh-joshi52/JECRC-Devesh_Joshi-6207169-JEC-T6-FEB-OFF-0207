import json

file = open('temp.txt', 'a+')
data = {
    'fullname' : 'Devesh Joshi',
    'userid': 885068022,
    'password' : '*********',
}

# print(f'Original Data: {data}')
# print(f'Type of Encrypted Data: {type(data)}')
# print()


enc_data = json.dump(data)
file.write(enc_data)

file.seek(0)


enc_data = file.read()
print(type(enc_data))

ori_data = json.load(enc_data)
print(ori_data, type(ori_data))

# print(f'Encrypted Data: {enc_data}')
# print(f'Type of Encrypted Data: {type(enc_data)}')
# print()


dec_data = json.loads(data)





file.close()