import tkinter as tk
import sqlite3


def hozzaad():
    nev = nev_entry.get()
    ar = ar_entry.get()
    raktar = raktar_entry.get()
    eladott = eladott_entry.get()
    aru = [nev, ar, raktar, eladott]
    print(aru)
    arulista.append(aru)
    print(arulista)


def kiiras():
    kiir_text_field.delete(1.0, tk.END)
    for i in arulista:
        for e in range(0, 4):
            kiir_text_field.insert(tk.END, i[e] + " ")
            if e == 3:
                kiir_text_field.insert(tk.END, i[e] + "\n")


def ab_hozzaad():
    conn = sqlite3.connect('test.db')

    nev = nev_entry.get()
    ar = ar_entry.get()
    raktar = raktar_entry.get()
    eladott = eladott_entry.get()

    script = "INSERT INTO TERMEKEK (NAME,PRICE,STOCK,SOLD) \
          VALUES ('{}', {}, {}, {})".format(nev, ar, raktar, eladott)

    conn.execute(script)

    conn.commit()
    conn.close()


def ab_kiiras():
    conn = sqlite3.connect('test.db')

    cursor = conn.execute("SELECT NAME,PRICE,STOCK,SOLD from TERMEKEK")
    kiir_text_field.delete(1.0, tk.END)
    for row in cursor:
        print("NAME = ", row[0])
        print("PRICE = ", row[1])
        print("STOCK = ", row[2])
        print("SOLD = ", row[3], "\n")
        kiir_text_field.insert(tk.END, "Termék neve: " + str(row[0]) + ", termék ára: " + str(row[1]) + ", raktárkészlet: " + str(row[
            2]) + ", eladott mennyiség: " + str(row[3]) + "\n")

    conn.close()


# conn = sqlite3.connect('test.db')
#
# conn.execute(
#     '''
#     CREATE TABLE TERMEKEK
#  (
#  NAME           CHAR(50)    NOT NULL,
#  PRICE            INT     NOT NULL,
#  STOCK        INT,
#  SOLD         INT
#  );
#  '''
# )


window = tk.Tk()
window.title("Input / Output teszt GUI-val")
arulista = []
tk.Label(window, text="Termék neve:").grid(row=0)
tk.Label(window, text="Termék ára:").grid(row=1)
tk.Label(window, text="Raktárkészlet:").grid(row=2)
tk.Label(window, text="Eladott mennyiség:").grid(row=3)

nev_entry = tk.Entry(window, width=80)
ar_entry = tk.Entry(window, width=80)
raktar_entry = tk.Entry(window, width=80)
eladott_entry = tk.Entry(window, width=80)
btn_hozzaad = tk.Button(window, text="Termék hozzáadása", width=18, command=ab_hozzaad)
btn_kiir = tk.Button(window, text="Termékek listázása", width=18, command=ab_kiiras)
kiir_text_field = tk.Text(window)

nev_entry.grid(row=0, column=1)
ar_entry.grid(row=1, column=1)
raktar_entry.grid(row=2, column=1)
eladott_entry.grid(row=3, column=1)
btn_hozzaad.grid(row=4, columnspan=2)
btn_kiir.grid(row=5, columnspan=2)
kiir_text_field.grid(row=6, columnspan=2)

window.mainloop()
