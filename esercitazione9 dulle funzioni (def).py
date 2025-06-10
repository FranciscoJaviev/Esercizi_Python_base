#Nome Script: esercitazione9.py 
#Descrizione:esercitazioni varie fatte sui Funzioni
#Autore:[Francisco J. Scognamiglio]
#Data:[19 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]




#Scrivi una funzione che prende una lista di numeri e 
#restituisce la somma di tutti gli elementi.


def somma (n1,n2,n3):
    somma = n1 + n2 + n3
    return somma

somma (2,3,4)

#Scrivi una funzione che prende una stringa e
#restituisce la stringa invertita.

def stringa_invertita(a):
    
    #stringa = "annibale"
    invertita = stringa[::-1]
    return invertita

#stringa_invertita ()


#Scrivi una funzione che prende una lista di parole e 
#restituisce una lista contenente solo le parole che 
#iniziano con una lettera specificata.

def lista_lettere_a (b):
    
    lista_a = []
    #lista_parole = ["annibale", "ruggero", "topolone", "annuccia", "a"]

    for n in lista_parole:
     if n [0] == "a":
      lista_a.append(n)
    
    return lista_a

#lista_lettere_a()


#Scrivi una funzione che prende una lista di parole e restituisce 
#una lista contenente la lunghezza di ciascuna parola.


lista = ["luigi", "massimo", "gianpiero","anassagora"]


def lunghezza_parole (c):
  lunghezza = []
  for n in lista_parole:
    numero_lettere = len(n)
    lunghezza.append(numero_lettere)

  return lunghezza

#lunghezza_parole()


#Scrivi una funzione che prende una lista di numeri e 
#restituisce una lista contenente solo i numeri pari.


lista = [34, 57, 563, 86, 121, 78]

def numeripari (d):
  
   numeri_pari = []

   for n in lista_numeri:
    if n%2 == 0:
      numeri_pari.append(n)
  
   return numeri_pari    

#numeripari()


#Scrivi una funzione che prende una lista di numeri e 
#restituisce il valore massimo.

lista = [76, 57, 63, 86, 12, 97]

def numero_massimo(e):

  massimo = [max(lista_numeri)]
   
  return massimo


#numero_massimo()



#Scrivi una funzione che prende una lista di parole e 
#restituisce la parola più lunga

def parola_più_lunga (lista_parole):

  for n in lista_parole:

    if len (n) > len(0):
      print (n)

  return len (n)   


lista_parole = ["anna", "paolo", "zorro", "tergicristalli","annassagora"]

for n in lista_parole:
  lunghezza = len (n)
  parola_maggiore = (max(lunghezza))

print (parola_maggiore)
print (lunghezza)

#Scrivi una funzione che prende una lista di numeri e 
#restituisce la media dei numeri.

def media (*arg):
    
    somma = sum (*arg)
    media = somma / len(lista_numeri)
    return media



#Scrivi una funzione che prende una lista di numeri e 
#restituisce una lista contenente solo i numeri maggiori 
#di un valore specificato.
lista_numeri = [23, 56, 87, 92, 23]


def lista_maggiori(lista_numeri):
   numero = int (input("inserisci numero:"))
   maggiori = []
   for n in lista_numeri:
      if n > numero:
         maggiori.append(n)
   return maggiori
         



stringa = "giorgione"

lista_parole = ["anna", "paolo", "zorro", "tergicristalli","annassagora"]

lista_numeri = [23, 56, 87, 92, 23]

a = print(numero_massimo(lista_numeri))
print("----------")
b = print(numeripari(lista_numeri))
print("----------")
c = print(lunghezza_parole(lista_parole))
print("---------")
d = print(lista_lettere_a(lista_parole))
print("--------")
e = print(stringa_invertita(stringa))
print ("----------")

f = print(parola_più_lunga(lista_parole))

print ("---------")
g = print (media (lista_numeri))
print ("---------")
h = print(lista_maggiori(lista_numeri))


