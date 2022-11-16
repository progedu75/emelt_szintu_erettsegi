hianyzasok = []
with open('naplo.txt', 'r', encoding='utf8') as forrasfajl:
	for sor in forrasfajl:
		sor = sor.strip().split()
		if sor[0] == '#':   # dátumot találtunk
			honap = int(sor[1])
			nap = int(sor[2])
		else:   # hiányzás-bejegyzést találtunk
			vezeteknev = sor[0]
			keresztnev = sor[1]
			hianyzas = sor[2]
			hianyzasok.append([honap, nap, vezeteknev + ' ' + keresztnev, hianyzas])
	print(hianyzasok)

print()
print('2. feladat:')
print(f'A naplóban {len(hianyzasok)} bejegyzés van.')

print()
print('3. feladat:')
igazolt = 0
igazolatlan = 0
for i in hianyzasok:
	igazolt += i[3].count('X')
	igazolatlan += i[3].count('I')
print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra..')

print()
# 4. feladat:
def hetnapja(honap, nap):
	napnev = ["vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", " szombat"]
	napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
	napsorszam = (napszam[honap - 1] + nap)	% 7
	hetnapja = napnev[napsorszam]
	return hetnapja

print('5. feladat:')
honap = int(input('A hónap sorszáma= '))
nap = int(input('A nap sorszáma= '))
print(f'Azon a napon{hetnapja(honap, nap)} volt')

print()
print('6. feladat:')
napnev = input('A nap neve= ')
orasorszam = input('Az óra sorszáma= ')

szerdak = []
for i in hianyzasok:
	if hetnapja(i[0], i[1]) == napnev:
		szerdak.append(i)

szerdai_hianyzasok = 0
for i in szerdak:
	if i[3][2] == 'X' or i[3][2] == 'I':
		szerdai_hianyzasok += 1
print(f'Ekkor összesen {szerdai_hianyzasok} óra hiányzás történt.')

print()
print('7. feladat:')
hianyzok = []
for i in hianyzasok:
	h = i[3].count('X') + i[3].count('I')
	hianyzok.append([i[2], h])

print(hianyzok)





j0