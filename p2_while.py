num = 1
while num <= 10:
    print(f'Következő szám: {num}')
    num += 1

print('Befejeztem a futást')

while True:
    actual_value = input('Adj meg adatot: ')
    print(actual_value + "\nOK")
    if actual_value == 'quit':
        break
