import random
lehetoseg = ['I', 'F']
print('\n1. feladat:')
print(f'A pénzfeldobás eredménye: {random.choice(lehetoseg)}')

print('\n2. feladat:')
usertipp = input('Tippeljen! (F/I): ')
tipp = random.choice(lehetoseg)

print(f'A tipp {usertipp.upper()}, a dobás eredménye {tipp} volt.')
if usertipp == tipp:
    print('Ön eltalálta!')
else:
    print('Ön nem találta el!')
