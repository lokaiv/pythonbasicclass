file = open('Anwonho', 'rt')

line_list = file.readlines()
for line in line_list:
    print(line, end = '')

file.close()