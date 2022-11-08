import random
import tkinter as tk

#Choose number
#Random number gets deployed
#Find out which player got closer to the random number
def calcul(player1,player2):
    NumarAleator = str(random.randrange(10, 99))

    Jucator1 = int(player1)
    Jucator2 = int(player2)

    Numar1 = [int(Jucator1) for Jucator1 in str(NumarAleator)[0]]
    Numar2 = [int(Jucator2) for Jucator2 in str(NumarAleator)[1]]
    Diferenta1 = (Jucator1-int(NumarAleator[0]))
    Diferenta2 = (Jucator2-int(NumarAleator[1]))
    DiferentaTotal1 = abs(Diferenta1)
    DiferentaTotal2 = abs(Diferenta2)

    Label1.destroy()
    Label2.destroy()
    tab1.destroy()
    tab2.destroy()
    buton.destroy()


    nrAleator.config(text = f"> Numarul aleator este: {NumarAleator} \n")
    primaCifra.config(text = f"> Prima cifra a numarului aleatoriu: {Numar1} \n")
    aDouaCifra.config(text = f"> A doua cifra a numarului aleatoriu: {Numar2} \n")
    comparareP1.config(text = f"> Rezultatul : {Numar1} - Numărul jucătorului 1 este = {DiferentaTotal1} \n")
    comparareP2.config(text = f"> Rezultatul : {Numar2} - Numărul jucătorului 2 este = {DiferentaTotal2} \n")
    if DiferentaTotal1 > DiferentaTotal2:
        rezultat.config(text = "> Jucatorul 1 a castigat <", bg = "light gray")
    elif DiferentaTotal1 == DiferentaTotal2:
        rezultat.config(text = "> Egalitate <", bg = " light gray")
    else:
        rezultat.config(text = "> Jucatorul 2 a castigat <", bg = "light gray")

def getEntry():
    text1 = tab1.get()
    text2 = tab2.get()
    calcul(text1, text2)

Interfata = tk.Tk()
Interfata.geometry("265x230")
Interfata.config(bg="light blue")
Label1 = tk.Label(Interfata, text = "Jucator 1", bg="light blue")
tab1 = tk.Entry(Interfata, bg="light gray")
Label2 = tk.Label(Interfata, text = "Jucator 2", bg="light blue")
tab2 = tk.Entry(Interfata, bg="light gray")
nrAleator = tk.Label(Interfata, text = "", bg="light blue")
primaCifra = tk.Label(Interfata, text = "", bg="light blue")
aDouaCifra = tk.Label(Interfata, text = "", bg="light blue")
comparareP1 = tk.Label(Interfata, text = "", bg="light blue")
comparareP2 = tk.Label(Interfata, text = "", bg="light blue")
rezultat = tk.Label(Interfata, text = "", bg="light blue")
buton = tk.Button(Interfata, text = "Joacă", command = getEntry, bg="gray")

Label1.grid(row = 0, column = 0)
tab1.grid(row = 0, column = 1)
Label2.grid(row = 1, column = 0)
tab2.grid(row = 1, column = 1)
nrAleator.grid(row = 2, column = 0)
primaCifra.grid(row = 3, column = 0)
aDouaCifra.grid(row = 4, column = 0)
comparareP1.grid(row = 5, column = 0)
comparareP2.grid(row = 6, column = 0)
rezultat.grid(row = 8, column = 0)
buton.grid(row = 3, column = 1)

Interfata.mainloop()
