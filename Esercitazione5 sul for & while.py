#Nome Script: esercitazione5.py 
#Descrizione:esercitazioni varie fatte durante la lezione sul ciclo for e while

#Autore:[Francisco J. Scognamiglio]
#Data:[10-11 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]


#esercitazione con il for

for a in range(3):
    for b in range(4):
        for c in range(5):
            print (a, b, c)


print ("---------------")
#creare una stringa e reiterarla 

nome = "francisco"

for i in nome:
    print (i)


print ("----------------")

#creare una lista e calcolare il prezzo con l'iva

LaMiaLista = [33,67,12,89,76,]
iva = 13

for i in LaMiaLista:
    importo_iva = i*iva/100
    importo_finale = i + importo_iva

    print("il prezzo iniziale è:",i,"il prezzo finale",importo_finale)

print ("---------------")

#stampare tutti i numeri da 1 a 10 e i poi solo i numeri pari


for i in range (1, 11):
    print (i)
    

print ("---------------")
    
for i in range (2, 11, 2):
    print (i)


print ("---------------")

for i in range (1, 11, 2):
    
    print (i)

print ("---------------")
#stampare i nomi in una lista

lista = ["roma", "milano", "napoli",]
 
for citta in lista:
    print(citta)

print ("--------------")


#fare la somma tra i numeri di una lista in vario modo

lista = [23, 45, 5, 2]
somma = 0

for n in lista:
    somma = n +(n+1)
    print(somma)


print ("-------------")

lista = [23, 45, 5, 2]
somma1 = 0            

for n in lista:
    
    somma1 += n
    print (somma1)

    
print (somma1/4)

print ("-------------")

#stampare tutte le lettere di ogni parola della lista

lista = "roma napoli milano"

for nome in lista:
    print (nome)

print ("-------------")
#oppure

lista2 = ["roma","\n", "napoli","\n", "milano"]

for città in lista2:
    for lettera in città:

        print(lettera)

print ("----------")

#Contare quante volte una lettera compare in una stringa

nome = "Natasha, Vasile o Catalin, Antonio Junior, Giovanni, Anto Senior, Andrea, Michela, Eugenia" 

lettera_a = "a"
contegio_a = 0

for i in nome:
    
    if i == lettera_a: 
        contegio_a +=1
        
print (contegio_a)


print ("fine esercitazione 5")


#contare fino a 10 e stamparli
i = 1

while i <= 10:
    print (i)

    i +=1
 
    
print ("----------") 
#fare la somma di n numeri
somma = 0
k = 0

while k <= 4:
    somma += k
    
    k += 1

print (somma)

print ("----------")

#stampare numeri dispari se j parte da 1 trovo solo i numeri dispari se parto da 0 trovo i numeri pari
#ma per ora non va bene utilizzo gli if

j = 0
while j < 10:
    
    print (j)

    j +=2

j = 0

while j <= 10:
    
    resto = j % 2

    if resto == 0: print (j)

    j +=1



#stampare solo i numeri naturali

lista = [2, -45.5, -9]


while lista <= 4:

    if n == float: print ("avanti")
    elif n== str: print ("avanti")
    else: print ("print numero naturale")

    n +=1


#Chiedere all'utente di inserire una stringa.
#Stampare la stringa al contrario usando un loop while


n = 10

while n >= 1:

    print (n)
    n -= 1



#Calcolo fattoriale di un numero "n"

n = int(input("inserisci un numero:"))
fat = 1

for i in range(1, n+1):
    print (i)
    fat *= i       #fat è uguale a fat che moltliplica i
    print (fat)
print ("il fattoriale è", fat)



#Chiedere all'utente di inserire una lista di numeri 
#interi. Stampare la somma di tutti i numeri usando 
#un loop while.

lista_numeri = [12, 56, 27, 87]

i=0
somma = 0

n =0
while n < len(lista_numeri):
        somma += lista_numeri[i]
        i +=1
        
        n +=1
print(somma)    


print("-----")        

#Chiedere all'utente di inserire una stringa.
#Stampare solo le consonanti della stringa usando 
#un loop while.

stringa = "marco antonio augusto"
vocali = "aeiou"
i = 0

while i < len(stringa):
    
    if stringa[i] in vocali: print("+")

    else: print(stringa[i])

    i +=1






