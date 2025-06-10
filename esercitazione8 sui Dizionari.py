#Nome Script: esercitazione8.py 
#Descrizione:esercitazioni varie fatte sui Dizionari
#Autore:[Francisco J. Scognamiglio]
#Data:[17 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]




#Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
#Successivamente tutte le coppie chiave-valore

dizionario = {"nome":"Luigi","cognome":"Serpione"}

for x in dizionario: print (x)

for x, y in dizionario.items() :print (x,y)

persona = {"nome":"Attila","cognome":"Filiberto", "età":28}

#Accedere al valore dell'elemento con chiave "età" del dizionario precedente

print(persona["età"])

#Aggiungere un nuovo elemento "email" con valore 
#"mario.rossi@email.com" al dizionario precedente.

persona.update({"e-mail":"attila-filip@gmail.com"})
print(persona)

#Rimuovere elemento presente nella chiave "cognome"

persona.pop("cognome")
print(persona)

#creare nuovo dizionario che contenga le chiavi del dizionario precedente

persona2 = dict(persona)
print(persona2)


#creare una lista con elementi le chiavi del dizionario,
#successivamente con i soli valori del dizionario.

lista_elementi = []
for n in dizionario: 
    print (dizionario[n])
    lista_elementi.append(dizionario[n])
print (lista_elementi)

lista_chiavi = []
for i in dizionario:
    lista_chiavi.append(i)
    
print(lista_chiavi)

chiavi = list(dizionario.keys())
print (chiavi)


#modificare l'età
persona.update({"età": "35"})

print(persona)

#contare il numero di elementi del dizionario

numero = len(persona)
print(numero)





