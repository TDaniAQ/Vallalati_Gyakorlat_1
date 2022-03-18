# Fájlkezelés

file = open("minta.txt", "r")

szamok = file.read().split()

for i in range(len(szamok)):
    szamok[i] = int(szamok[i])

print(szamok)

file.close()

file2 = open("letrehozott.txt", "w+")
for i in range(len(szamok)):
    dupla = szamok[i]*2
    file2.write(str(dupla) + " ")

file2.close()