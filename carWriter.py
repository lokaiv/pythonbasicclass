import csv

with open('차량관리.csv', 'rt') as file:
    csv_maker = csv.writer(file,delimiter = ',')
    csv_maker.writerow([1, '08RU1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25DA1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28HA1234', '2020-10-20,14:20'])

print('차량관리.csv created')