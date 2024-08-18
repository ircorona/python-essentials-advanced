with open ('./text.txt', 'r+',encoding="UTF-8") as file:
    for line in file:
        print(line)
    file.write('Nuevas Cosas\n')
    file.write('Line 6\n')
    file.write('Line 7\n')