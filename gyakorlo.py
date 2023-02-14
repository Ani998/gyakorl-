import random

print ('Üdvözöllek!\nGondoltam egy számot 1 és 10 között.\n Mit tippelsz melyik szám az?')
guess = random.randint(1, 10)
win = False

while not win:
    guess = int(input('Tipp:'))
if guess > number:
    print (f'Nem, én kisebb számra gondoltam, ({number})')
elif guess < number:
    print (f'Nem, én nagyobb számra gondoltam, ({number})')
else:
    print(f'Gratulálok eltaláltad. :)')
print('Viszlát!')
win = True
