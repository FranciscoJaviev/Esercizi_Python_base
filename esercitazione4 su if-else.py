#Nome Script: esercitazione4.py 
#Descrizione: Esercitazioni varie utilizzando l'operatore if/else
#Autore:[Francisco J. Scognamiglio]
#Data:[7 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]




#Trovare quella operazione per portare "numero" a valere 1 
#senza riassegnarlo direttamente ad 1 e sottraendolo a se stesso


numero = int (input("il valore è:"))
numero -= numero -1
print (numero)




print ("---------")

#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" 
#se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo"


numero = int (input("il numero è:"))

if numero > 0: print ("Il numero è positivo")

elif numero == 0: print ("il numero è zero")

else: print ("il numero è negatovo")


print ("---------")

#If annidati funsionano se la variabile x rientra nel range assegnato altrimenti non lo considera

x = int (input("il numero è:"))
if x % 2 == 0:
    print ("pari")
    if(x>10):
        print("pari e maggiore di dieci")
else:
    print ("dispari")
    if (x<34):
        print ("dispari è minore di 34")
    else: print("dispari è maggiore di 34")

print ("----------")


#Scrivere un programma che chiede all'utente di inserire due numeri 
#e stampa "Il primo numero è maggiore" 
#se il primo numero è maggiore del secondo, 
#"Il secondo numero è maggiore" se il secondo numero è maggiore del primo,
#altrimenti stampa "I numeri sono uguali"

x = 65
y = 65

if x > y: print ("il numero x è maggiore di y")
elif x < y: print ("il numero x è minore di y")
else: print ("x è uguale a y")


print ("----------")


#Scrivere un programma che chiede all'utente di inserire una stringa e 
#stampa "La stringa è vuota" se la stringa è vuota, 
#altrimenti stampa "La stringa non è vuota"


stringa = input ("") 
if stringa == "": print ("la stringa è vuota")
else: print ("La stringa è piena")


print ("----------")

#Scrivere un programma che chiede all'utente di inserire una lettera, 
#stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), 
#altrimenti stampa "La lettera non è una vocale".


#simbolo = ["consolanti", "vocali"]
lettera = input ("la lettera è:")
vocali = "aeiou"

if  lettera in vocali: print ("La lettera è una vocale")
else: print ("la lettara è una consolante")

print ("----------")

#Scrivere un programma che chiede all'utente di inserire un numero
#e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso 
#tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".

numero = int(input("il numero è:"))

if 1 <= numero <= 10: print ("il numero è compreso tra 1 e 10")
else: print ("il numero non è compreso tra 1 e 10")


print ("----------")


#Scrivere un programma che chieda all'utente di inserire un numero intero.
#Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10".
#Se il numero è uguale a 10, stampare "Il numero è uguale a 10".
#Se il numero è minore di 10, stampare "Il numero è minore di 10".

numero = int (input("il numero è:"))

if numero > 10: print ("il numero è maggiore di 10")

elif numero == 10: print ("il numero è uguale a 10")

else: print ("il numero è minore di 10")

'''
print ("----------")

'''
#Scrivere un programma che chieda all'utente di inserire un carattere. 
#Se il carattere è una vocale (a, e, i, o, u) con isalpha(), 
#stampare "Il carattere inserito è una vocale". 
#Se il carattere è una consonante, stampare "Il carattere inserito è una consonante".
#Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".


carattere = input("il carattere è:")
vocali ="a,e,i,o,u"
consolanti = carattere.isalpha

print (carattere.isalpha())

if carattere in vocali: print ("il carattere è una vocale")  

elif  consolanti: print ("il carattere è una consolante")

else: print ("il carattere non è una lettera")


print ("----------")


#devo chiedere perchè devo invertire la condizione di if e elif, altrimenti non funziona

    
if consolanti: print("si")
else: print ("no")
#devo chiedere perchè se utilizzo solo if ed else non fuziona il vero falso




#Scrivi un programma che chieda all'utente di inserire tre numeri interi 
#che rappresentano i lati di un triangolo. Il programma deve verificare 
#se questi tre numeri formano un triangolo rettangolo. 
#Se i tre numeri soddisfano la condizione per essere un triangolo rettangolo 
#(cioè rispettano il teorema di Pitagora), allora stampa 
#"I tre numeri formano un triangolo rettangolo". Altrimenti, stampa 
#"I tre numeri non formano un triangolo rettangolo".


a = int(input("inserisci numero"))
b = int(input("inserisci numero"))
c = int(input ("inserisci numero"))

if a**2 + b**2 == c**2 or a**2 - c**2 == -(b**2) or -(b**2) + c**2 == a**2:
    
    print("è un triangolo")

else: print ("non è un triangolo")


print ("fine esercitazione4")
