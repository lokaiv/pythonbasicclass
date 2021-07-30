file = open('Anwonho', 'rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end = '')
file.close()