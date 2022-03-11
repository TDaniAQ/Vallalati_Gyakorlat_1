# Változók

# int típusú
import math

a_int = 10  # int típusu változó létrehozása, és értékadás
print(a_int, type(a_int))  # "a_int" nevű változó értékének, és típusának kiírása
b_int = 15

ab_sum = a_int + b_int  # "a_int" és "b_int" változók összeadása
ab_szor = a_int * b_int  # "a_int" és "b_int" változók összeszorzása

print("a+b= " + str(ab_sum))  # ab_sum változó string típusra konvertálva, hogy kiírható legyen stringgel együtt
print("a*b= " + str(ab_szor))

# float típusú
a_float = 15.55
print(a_float, type(a_float))  # "a_float" nevű változó értékének, és típusának kiírása

# boolean típusú
a_boolean = False
print(a_boolean, type(a_boolean))

# string típusú
b_str = "String"  # string típusu változó létrehozása, és értékadás
print(b_str, type(b_str))  # "b" nevű változó értékének, és típusának kiírása

# két string típusu változó összefűzése, és kiírása
h = "hello"
w = "world"
hw = h + " " + w
print(hw)

# --------------------------------------------------------------------------------
# String metódusok
minta_string = "ez egy minta Szöveg !"
print(len(minta_string))  # szöveg hosszának megállapítása
print(minta_string.find("min"))  # szövegben részlet megtalálása
print(minta_string.capitalize())  # az első betű nagybetűvé alakítása
print(minta_string.upper())  # minden betű nagybetűvé alakítása
print(minta_string.lower())  # minden betű kisbetűvé alakítása
print(minta_string.isdigit())  # megnézi, hogy a szöveg szám-e (boolean)
print(minta_string.count("e"))  # megszámolja egy karakter / részlet előfordulásainak számát
print(minta_string.replace("Szöveg", "módosítás"))  # megkeres egy szövegrészletet, és

# --------------------------------------------------------------------------------
# Típus konverziók
x_float = 5.0  # float típusú változó megadása
x_int = int(x_float)  # int típusúvá konvertálás
x_string = str(x_float)  # string típusúvá konvertálás

y_int = 4
y_float = float(y_int)  # float típusúvá konvertálás

print(x_float, type(x_float))  # Ellenőrzés
print(x_int, type(x_int))
print(x_string, type(x_string))
print(y_float, type(y_float))
# --------------------------------------------------------------------------------
# Felhasználói adatmegadás
input_szo = input("Adjon meg egy szót: ")
print("A megadott szó: " + input_szo)

input_int = int(input("Adjon meg egy egész számot: "))
print("A megadott szám: " + str(input_int) + " a megadott szám típusa: " + str(type(input_int)))

input_float = float(input("Adjom meg egy számot: "))
print("A megadott szám: " + str(input_float) + " a megadott szám típusa: " + str(type(input_float)))
# --------------------------------------------------------------------------------
# Matematikai funkciók
test_float = 10.45
print(round(test_float))
print(math.ceil(test_float))  # Felfelé kerekítés
print(math.floor(test_float))  # Lefelé kerekítés
print(abs(test_float))  # Abszolút érték
print(pow(test_float, 2))  # Hatványozás
print(math.sqrt(test_float))  # Gyökvonás
print(max(test_float, 14, 45, 34, 13))  # Maximum keresés
print(min(test_float, 14, 45, 34, 13))  # Minimum keresés
# --------------------------------------------------------------------------------
# # IF és logikai operátorok (AND;OR;NOT)
if_test = int(input("Adjon meg egy számot: "))

if if_test > 100:
    print("A megadott szám 100-nál nagyobb!")
elif if_test >= 50:
    print("A megadott szám 50 és 100 között van!")
else:
    print("A megadott szám kisebb 50-nél")

if if_test >= 50 or 100 <= if_test:
    print("AND check TRUE")
else:
    print("AND check FALSE")

if if_test == 50 or if_test == 100:
    print("OR check TRUE")
else:
    print("OR check FALSE")

if not(if_test > 50 and if_test == 100):
    print("NOT check TRUE")
else:
    print("NOT check FALSE")
# # --------------------------------------------------------------------------------
# WHILE ciklus
while_int = 0
while while_int < 100:
    while_int += 1
    print(while_int)

# FOR ciklus
for i in range(11, 55):
    print(i)
# --------------------------------------------------------------------------------
# Listák
szinek = ["piros", "kék", "zöld", "fehér", "fekete", "barna"]

for i in range(0, len(szinek)):
    print(szinek[i])

szinek.append("lila")
szinek.remove("barna")
szinek.pop()  # utolsó elem kivétele
szinek.insert(0, "sárga")
szinek.sort()
# szinek.clear()

targyak = ["toll", "lámpa", "füzet", "pohár"]  # 2D Lista

szinek_targyak = [szinek, targyak]

print(szinek_targyak[1][3])
# --------------------------------------------------------------------------------
# Mátrixok
test_matrix = [['Elem1', '001', 1], ['Elem2', '002', 2], ['Elem3', '003', 3], ['Elem4', '004', 4], ['Elem4', '004', 4]]

print(test_matrix[2])
print(test_matrix[2][0])
print(test_matrix[-1])

# --------------------------------------------------------------------------------
