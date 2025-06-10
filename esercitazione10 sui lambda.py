#Nome Script: esercitazione10.py 
#Descrizione:esercitazioni varie fatte sulle Lambda
#Autore:[Francisco J. Scognamiglio]
#Data:[21 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]


#Scrivi una lambda function che prenda un parametro e 
#restituisca il quadrato del numero.

quadrato = lambda x: x**2
print (quadrato(5))

print("---------")
#Scrivi una lambda function che prenda una lista e 
#restituisca una lista di tutti gli elementi della lista 
#originale moltiplicati per 2.

lista = [2, 6, 7, 8]

moltiplicazione = list(map(lambda x: x*2, lista))
print (moltiplicazione)

print("---------")
#Scrivi una lambda function che prenda una lista di parole e 
#restituisca una lista contenente solo le parole che 
#iniziano con la lettera "a".

lista_nomi = ["carlo", "alessio", "giulia", "federica"]

lettera_a = list(filter(lambda x: x[0]=="a",lista_nomi))
print (lettera_a)


print("----------")
#Scrivi una lambda function che prenda due numeri e 
#restituisca la somma dei loro quadrati.

somma_quadratica = lambda x,y: x**2 + y**2
print (somma_quadratica (3,5))

#Scrivi una lambda function che prenda una stringa e 
#restituisca True se la stringa è palindroma, altrimenti False.

lista_n = ["anna", "giancarlo","gennaro"]

polindromia = list(filter(lambda x: x == x[::-1], lista_n))

print (polindromia)

print("----------")
#Scrivi una lambda function che prenda una lista di parole e 
#restituisca la lunghezza media delle parole nella lista.

lista = ["anna", "giancarlo","gennaro"]

media_parole = lambda x: sum(len(x) for x in lista) / len(lista)
media_parole1 = list(map(lambda x: sum(len(x))/len(lista), lista))                                                                    
print (media_parole(lista))
print (media_parole1)
print("---------")

#Scrivi una lambda function che prenda una lista di numeri e restituisca la somma solo dei numeri pari.
liste = [2, 6, 7, 8]

somma_pari = lambda liste: sum(x for x in liste if x % 2 == 0)

print (somma_pari(liste))

#Scrivi una lambda function che prenda una lista di dizionari e restituisca una lista di tutte le chiavi dei dizionari.
lista_di_dizionari = [
    {"nome": "Alice", "età": 25},
    {"nome": "Bob", "città": "Roma"},
    {"professione": "Ingegnere", "età": 30}
]

lista = lambda lista_d: [chiave for dizionario in lista_d for chiave in dizionario.keys()]

print(lista(lista_di_dizionari))

print("---------")
#Scrivi una lambda function che prenda una lista di numeri e restituisca una lista di tutti i numeri maggiori di 10.
lista_n = [12, 10, 34, 7, 4]

maggiori_di_10 = lambda x: [x for x in lista_n if x> 10]

print (maggiori_di_10(lista_n))

print("---------")

#crivi una lambda function che prenda una lista di tuple e restituisca una lista di tuple ordinate per il secondo elemento di ciascuna tupla.
lista_tuple =[
(1,2,3),
(4,3,6),
(7,0,9),
]

ordina_per_secondo_elemento = lambda lista: sorted(lista, key=lambda tupla: tupla[1])

print(ordina_per_secondo_elemento(lista_tuple))