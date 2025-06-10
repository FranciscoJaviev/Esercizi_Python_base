#Nome Script: esercitazione6.py 
#Descrizione:esercitazioni varie fatte sulle liste
#Autore:[Francisco J. Scognamiglio]
#Data:[12 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]


#Creare una lista vuota e assegnarla a una variabile.
lista = []

print ("-----------")

#Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile
lista =[1, 2, 3, 4, 5]


#Accedere all'elemento con indice 2 della lista precedente.
print(lista[2])

print ("-----")
#Aggiungere un altro elemento alla lista
lista.append(6)

print (lista)

print ("-----")
#Rimuovere l'elemento con indice 3 dalla lista precedente.
lista.pop(3)
print (lista)


print("----------")
#Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
lista2 =[1, 2, 3, 4, 5, 6]

print (lista2[:3])


print("-----")
#Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
lista4 = lista2.copy()
del lista2[1]
del lista2[2]
del lista2[3]
print (lista2)


print ("-----")
#Ordinare la lista precedente in ordine decrescente.
lista3 =[1,2, 3, 4, 5, 6]

lista3.sort(reverse=True)
print (lista3)

#Contare quante volte l'elemento "2" appare nella lista precedente.

lista5 = [12, 45, 72, 122, 2]

#contegio_2 = lista5.count(2)
#print (contegio_2)
contegio_2 = 0
i = 2
for n in lista5:
    if i == n:
        contegio_2 +=1
print (contegio_2)

print("------fine esercizi sulle liste------")

print("----esercizi sulle stringhe-----")

#Descrizione:esercitazioni varie fatte sulle stringhe

stringa = "ciao mano"
print(stringa.upper())


print ("----------")

#Assegnare una stringa "Benvenuti a Roma" ad una 
#variabile "stringa" e utilizzare il metodo lower() 
#per convertirla in minuscolo in una nuova variabile

stringa_1 = "Benvenuti a Roma"
print (stringa_1.lower())


print("----------")

#Assegnare una stringa "Il meglio deve ancora venire" 
#ad una variabile "stringa" e utilizzare 
#il metodo split() per dividere la stringa 
#in una lista di parole.

stringa_2 = "Il meglio deve ancora venire"
print (stringa_2.split())


print("---------")

#Assegnare una stringa "Hello World" ad una variabile 
#"stringa" e utilizzare il metodo replace() 
#per sostituire "World" con "Python".


stringa_3 = "Hello Word"
print (stringa_3.replace("Word", "Paython"))


print("--------")

#Assegnare una stringa " Ciao " ad una variabile
#"stringa" e utilizzare il metodo strip() per 
#rimuovere gli spazi vuoti all'inizio e alla fine 
#della stringa..

stringa_4 = " Ciao "
print (stringa_4.strip())


print("---------")
#Assegnare una stringa "abcdefg" ad una 
#variabile "stringa" ed estrarre i primi tre caratteri

stringa_5 = "abcdefg"
print(stringa_5[:3])


print("---------")
#Assegnare una stringa "Python" ad una variabile 
#"stringa" e utilizzare il metodo startswith()
#per verificare se la stringa inizia con "Py".

stringa_6 = "Python"
print (stringa_6.startswith("Py"))


print("--------")
#Assegnare una stringa "Ciao mondo" ad una variabile 
#"stringa" e utilizzare il metodo count() per contare 
#il numero di volte in cui la lettera "o" appare 
#nella stringa.

stringa_7 = "Ciao mondo 1238522"
print(stringa_7.count("2"))


print("--------")
#Assegnare una stringa "Ciao mondo" ad una variabile 
#"stringa". Mandare quindi a schermo gli ultimi 5 
#caratteri della stringa in maiuscolo, 
#sostituendo il carattere "o" con "k".

stringa_8 ="Ciao mondo"
print (stringa_8.replace("o","k"))

print(stringa_8[5:].upper())