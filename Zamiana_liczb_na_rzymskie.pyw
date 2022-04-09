#-*- coding:utf-8 -*-#
from tkinter import *
window=Tk()
window.config(background="black")
window.title("Rzymskie liczby")
window.resizable(False, False)

def klik(x=0):
    x=entry.get()
    lista=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    try: got=int(x)
    except ValueError:
        result.config(text="Podaj liczbę całkowitą")
        return
    if got>3999:
        result.config(text="Maksymalna wartość: 3999")
        return
    elif got<1:
        result.config(text="Liczba musi być dodatnia")
        return
    a=""
    c=0
    for i in nums:
        b=got//i
        a+=lista[c]*b
        got-=i*b
        c+=1
    result.config(text=a)
    
result=Label(window, bg="black", fg="white", font="arial 12")
result.grid(row=4, column=0, sticky=S, pady=3) 

text=Label(window, text="Rzymskie liczby", font="Elephant 25 bold", bg="black", fg="white")
text.grid(row=0, column=0, sticky=N, pady=10)

zero=Label(window, text="", bg="black", font="15").grid(row=1, column=0)

entry=Entry(window, text="Wpisz liczbę", width=40, background="white")
entry.bind("<Return>",klik)
entry.grid(row=2, column=0, sticky=S)

but=Button(window, text="Konwertwuj", width=10, bg="white", command=klik)
but.grid(row=3, column=0, pady=10, sticky=S)

window.mainloop()
