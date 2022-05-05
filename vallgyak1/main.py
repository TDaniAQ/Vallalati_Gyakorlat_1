import termekablak
import kategoriaablak
import tkinter as tk
import sqlite3
import os

conn = sqlite3.connect('test.db')
#
# conn.execute(
#     '''
#     CREATE TABLE TERMEKEK
#  (
#  ID             INT NOT NULL    PRIMARY KEY,
#  NAME           CHAR(50)    NOT NULL,
#  PRICE            INT     NOT NULL,
#  STOCK        INT,
#  SOLD         INT,
#  KATEGORIA_ID INT   NOT NULL,
#  FOREIGN KEY(KATEGORIA_ID) REFERENCES KATEGORIA(ID)
#  );
#  '''
# )
#
# conn.execute(
#     '''
#     CREATE TABLE KATEGORIAK
#  (
#  ID           INT    NOT NULL   PRIMARY KEY,
#  NAME            CHAR(50)     NOT NULL
#  );
#  '''
# )

# UPDATE üressel, több azonos nevű termék
# Lekért adatok feldolgozása
# Milyen termékek a táblában, jelölőnégyzet -> milyen termékekről szeretnénk adatokat
# Vizuális adatmegjelenítés
# Táblázat -> minden értelmes infó -> jelölőnégyzetek -> választott adatok grafikus megjelenítése ->
# gomb amiből csak 1-et választhatok


def open_documentation():
    os.startfile("dokumentacio.docx")


window = tk.Tk()
window.title("Főoldal")
window.minsize(700, 200)
tk.Label(window, text="Vállalati gyakorlat 1 - Adatkezelés pythonban", font=("Arial", 20)).grid(row=0, column=1)

termekek_gomb = tk.Button(window, text="Termékek", width=30, height=5, command=termekablak.termek_ablak)
kategoria_gomb = tk.Button(window, text="Kategóriák", width=30, height=5, command=kategoriaablak.kategoria_ablak)
dokumentacio_gomb = tk.Button(window, text="Dokumentáció", width=30, height=5, command=open_documentation)

termekek_gomb.grid(row=1, column=0)
kategoria_gomb.grid(row=1, column=1)
dokumentacio_gomb.grid(row=1, column=2)

n_rows = 4
n_columns = 3
for i in range(n_rows):
    window.grid_rowconfigure(i, weight=1)
for i in range(n_columns):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()

# kereső termék neve alapján, törlés név -> id alapján,