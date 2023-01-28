from tkinter import *
import random

root = Tk()
root.title("Rolador de dados")
root.geometry("600x450")


# pegar os numeros dos dados
def pegar_numero(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return (2)
    elif x == '\u2682':
        return (3)
    elif x == '\u2683':
        return (4)
    elif x == '\u2684':
        return (5)
    elif x == '\u2685':
        return (6)


# rolar dados
def rolar_dados():
    # rolagem de dados aleatorio
    d1 = random.choice(dado)
    d2 = random.choice(dado)
    d3 = random.choice(dado)
    d4 = random.choice(dado)

    # Numero dos dados
    sd1 = pegar_numero(d1)
    sd2 = pegar_numero(d2)
    sd3 = pegar_numero(d3)
    sd4 = pegar_numero(d4)

    # update dos labels
    dLabel1.config(text=d1)
    dLabel2.config(text=d2)
    dLabel3.config(text=d3)
    dLabel4.config(text=d4)

    # update sub labels
    sub_dLabel1.config(text=sd1)
    sub_dLabel2.config(text=sd2)
    sub_dLabel3.config(text=sd3)
    sub_dLabel4.config(text=sd4)

    #update total
    total = sd1 + sd2 + sd3 + sd4
    total_label.config(text=f"O total foi de {total}")


# Lista de dados
dado = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', ]

# Frame
frame = Frame(root)
frame.pack(pady=20)

# Labels dos dados

dLabel1 = Label(frame, text='', font=("Helvetica", 100), fg="green")
dLabel1.grid(row=0, column=0, padx=5)
sub_dLabel1 = Label(frame, text="")
sub_dLabel1.grid(row=1, column=0)

dLabel2 = Label(frame, text='', font=("Helvetica", 100), fg="purple")
dLabel2.grid(row=0, column=1, padx=5)
sub_dLabel2 = Label(frame, text="")
sub_dLabel2.grid(row=1, column=1)

dLabel3 = Label(frame, text='', font=("Helvetica", 100), fg="grey")
dLabel3.grid(row=0, column=2, padx=5)
sub_dLabel3 = Label(frame, text="")
sub_dLabel3.grid(row=1, column=2)

dLabel4 = Label(frame, text='', font=("Helvetica", 100))
dLabel4.grid(row=0, column=3, padx=5)
sub_dLabel4 = Label(frame, text="")
sub_dLabel4.grid(row=1, column=3)

# total
total_label = Label(root, text='', font=("Helvetica", 24), fg="grey")
total_label.pack(pady=40)

btn = Button(root, text="Rolar Dados", command=rolar_dados, font=("Helvetica", 12))
btn.pack(pady=20)

rolar_dados()

root.mainloop()
