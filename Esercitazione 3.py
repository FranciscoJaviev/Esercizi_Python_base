
#Nome Script: esercitazione3.py 
#Descrizione: esercitazioni nella quale creare un programma che mi dica dato un numero se è pari o dispari

#Autore:[Francisco J. Scognamiglio]
#Data:[6 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]

numero1 = int(input("il mio numero è:"))
a = 2 
b = 0

print (f"il numero diviso 2 è = {numero1 / a}")
print (f"il resto è: {numero1 % a}")
print(f"il risultato: {numero1 % a} è uguale a {b}? {numero1%a == b}")
print(f"il risultato:{numero1 % a} è diverso a {b}? {numero1%a != b}")

#risoluzione del problema

messaggi = ["pari", "dispari"]
numero = int(input("inserisci il numero"))
risultato = messaggi [(numero1 % 2)]
print (risultato)

print ("fine esercitazione 3")

#Nome Script: esercitazione3.py 
#Descrizione:esercitazioni varie fatte durante la lezione

#Autore:[Francisco J. Scognamiglio]
#Data:[6 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]




#Dichiarare una variabile "numero_intero" e assegnargli 
#un valore **intero**. Mandare a schermo il tipo della 
#variabile per conferma.


numero_intero = 3
print (type(numero_intero))


print ("----------")

#Creare una lista "misti" contenente un numero intero, 
#un numero float, una stringa e un valore booleano. 
#Mandare a schermo il tipo della variabile per conferma.


misti = [4.9, False, "Francisco", 97]
print (type(misti))

print("---------")

#Incrementare "numero1" di 1 e decrementare "numero2" di 3.
#Mandare a schermo i nuovi valori.


numero1 = 3
numero2 = 6
print ("il primo numero è:",numero1, "il secondo numero è:", numero2)

numero1 += 1
numero2 -= 3
print ("il numero incrementato di 1 è:", numero1, "il numero decrementato di 3", numero2 )


print("fine esercitazione3.2")


#('C:\User\hp\Document\Corso AI Cefi\Il_mio_pacchetto')
#from Il_mio_pacchetto import matematica 

#print(matematica.somma(10, 5))   # Output: 15
#print(matematica.sottrai(10, 5))

import math
seno_di_45_gradi = math.sin(math.radians(45))
seno_arrot = round(seno_di_45_gradi, 3)
print(f"nuovo risultato{seno_arrot}")