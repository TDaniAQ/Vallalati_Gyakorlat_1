import tkinter as tk


def gombnyomas():
    label2.config(text="Megnyomtad a gombot!", bg="green")


window = tk.Tk()
window.title("Teszt")
window.wm_minsize(1000, 500)

frame1 = tk.Frame(window)
frame1.pack(
    fill='x'
)

label1 = tk.Label(
    frame1,
    text="Tkinter tesztelése",
    font=("Arial", 15),
    fg="white",
    bg="blue",
)

label1.pack(
    fill='x',
    ipadx=10,
    ipady=10
)


btn_test = tk.Button(
    frame1,
    text="Gomb",
    bg='green',
    activebackground='red',
    command=gombnyomas,
    width=10
)

label2 = tk.Label(
    frame1,
    text="Nyomd meg a gombot",
    bg="red"
)

btn_test.pack(side="left")
label2.pack(side="right")

window.mainloop()
