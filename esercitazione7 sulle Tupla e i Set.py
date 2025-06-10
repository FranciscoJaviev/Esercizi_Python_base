#Nome Script: esercitazione6.py 
#Descrizione:esercitazioni varie fatte sulle Tupla e i Set
#Autore:[Francisco J. Scognamiglio]
#Data:[14 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]



#Creare una Tupla vuoata e asseganrla ad una variabile

variabile = ()

#aggiungere tre elementi

variabile = ("mela", "banana", "kiwi")
print (type(variabile))
#accedere all'elemento banana

print (variabile[1])

#crea nuova tubla con solo i primi due elementi della tubla precedente

variabile = list(variabile)
variabile.remove("kiwi")
variabile = tuple(variabile)
print (variabile)

#verificare se l'elemento "ananas" è presente

if "ananas" in variabile:
    print ("c'è ananas")
else: print ("non c'è ananas")


#creare nuova tubla con  elementi "pesca" e "arancia" e
#concatenarlo alla prima tupla

variabile_1 = ("pesca", "arancia")

variabile_2 = variabile + variabile_1

print (variabile_2)

#verificare la lunghezza della nuova tubla

print(len(variabile_2))

#creare una tubla contenente numeri interi da 1 a 5

tubla_numeri = (1, 2, 3, 4, 5)

#creare una tubla con il quadrato dei numeri precedenti

tubla_quadrato = list()
for n in tubla_numeri:
    tubla_quadrato.append(n**2)

print(tubla_quadrato)
tubla_quadrato = tuple(tubla_quadrato)
print(tubla_quadrato)
    



#contare il numero di occorrenzad dell'elemento "mela"
Occorenza = variabile_2.count("mela")
print(Occorenza)



#Creare un set vuoto e assegnarlo a una variabile

set()

#aggiungere "mela", "banana", "kiwi", "mela"

set_1 = {"mela","banana","kiwi","mela"}

#aggiungere elemento "pesca"

set_1.add("pesca")

print (set_1)


#eliminare "mela"
set_1.discard("mela")

print (set_1)


#verificare se "ananas" è presente nel set

print ("ananas" in set_1)

#creare nuovo set

set_2 ={"banana", "kiwi", "arancia"}


#Creare un set con numeri da 1 a 5 utilizzando un range

set_n =set(range(1,6))
print(set_n)

#creare un set dal set precedente con solo numeri pari

set_np = set(range(1,6,2))

print(set_np)

#creare un due set con 2 variabili uguali

ilset1 = {2, 4, 6, 7, 10}
ilset2 = {5 , 7, 12, 9}

ilset3 = ilset1.symmetric_difference(ilset2)
print(ilset3)

ilmioset4 = ilset1.intersection(ilset2)
print(ilset1)

