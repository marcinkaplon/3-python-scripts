# -*- coding:UTF-8 -*- #
import os
os.system("title Wisielec")
haslo=input('''Witaj w programie Wisielec.
Wpisz hasło, które będzie musiał zgadnąć twój przeciwnik: ''')
haslo=haslo.lower()
sz=10
lit=[]
x=00
slowa=haslo.split(" ")
c="  ".join([len(i)*"_ " for i in slowa])
while not c.lower()==haslo.lower():
    os.system("cls")
    if sz==0:
        import os
        sz=-1
        print("Przegrałeś/aś! Hasło to {}".format(haslo))
        os.system("pause >nul")
        break
    print('twoja liczba szans -',sz)
    print('litery, które już zgadywałeś/aś -',lit)
    print("\n\n",c)
    x=input('wpisz literę ')
    while not len(x)==1:
        print('Możesz wpisać tylko jedną literę ')
        x=input('wpisz literę')
    if x not in lit:
        lit+=[x]
    if x in haslo:
        for i in range(len(haslo)):
            if x==haslo[i]:
                c=c[:2*i]+x+c[2*i+1:]
    if not x in haslo:
        sz-=1
    if not "_" in c:
        c=haslo
if sz>=0:
    os.system("cls")
    print('Udało się! Zgadłeś/aś hasło!')
os.system("pause >nul")

    
    
