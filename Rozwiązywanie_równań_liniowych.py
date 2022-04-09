#-*- coding: utf-8 -*-#

'''Program do rozwiązywania równań liniowych'''
#autor: Marcin Kapłon. 2019

while True:
    try:
        menu=1
        func=input("Podaj równanie liniowe ").replace(" ","").lower()
        funclist=func.split("=")
        if "x" in funclist[1]:
            funclist.reverse()
        c=float(funclist[1])
        if "+" in funclist[0]:
            var=funclist[0].split("+")
            if "x" in var[1]: var.reverse()
            if var[0]=="x": var[0]="1x"
            if var[0]=="-x": var[0]="-1x"
            a=float(var[0].replace("x",""))
            b=float(var[1])
            print("x={}".format((c-b)/a))
        else:
            pom=funclist[0].replace("-","-m")
            var=pom.split("-")
            if var[0]=="": var.remove("")
            if len(var)==2:
                if "x" in var[1]: var.reverse()
            var[0]=var[0].replace("m","-")
            if len(var)==2: var[1]=var[1].replace("m","-")
            else: var.append(0)
            if var[0]=="x": var[0]="1x"
            if var[0]=="-x": var[0]="-1x"
            a=float(var[0].replace("x",""))
            b=float(var[1])
            print("x={}".format((c-b)/a))
    except:
        print("Podaj poprawną postać równania!")
            

        
        
