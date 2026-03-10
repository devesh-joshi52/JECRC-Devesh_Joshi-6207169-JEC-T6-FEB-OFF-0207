import csv
from datetime import date
file = open('expense.csv', 'a+')

# w = csv.writer(file)
r = csv.reader(file)
file.seek(0)

print(list(r))

# w.writerow(['DATE', 'CATEGORY', 'AMOUNT'])

# w.writerows(
#     [
#         [date.today(), 'Travel', '1000'],
#         [date.today(), 'Food', '500'],
#         [date.today(), 'Entertainment', '1230'],
#     ]
# )

file.close()