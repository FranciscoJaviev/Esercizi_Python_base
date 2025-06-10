#Nome Script: esercitazione14.py 
#Descrizione: esercitazioni sulla comprezione di codici con metodi speciali
#Autore:[Francisco J. Scognamiglio]
#Data:[7-8 Marzo 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]


#Esempio di decoratore personalizzato:

def mio_decoratore(func):                                       #qui sto creando il mio decoratore
    def wrapper(*args, **kwargs):                               #creo una funzione che eseguirà l'operazione decorante
        print("Sto eseguendo del codice prima della funzione.") #questo e il successivo print servono solo per delimitare in modo 
        #                                                       #visivo l'esucuzione decorante
        risultato = func(*args, **kwargs)                       #inizializzo la funzione func che avrà come parametri
        #                                                       #un qualsiasi parametro che io ci metto e una qualsiasi chiave così da non generare errore
        #                                                       #la funzione func acquisirà la funzione definita sotto il richiamo decorante (vedi sotto)
        print("Sto eseguendo del codice dopo la funzione.")
        return risultato                                        #return mi permette di ritornare, presa la funzione funk ed eseguita,
    #                                                           #nuovamente alla funzione stessa come fosse un ciclo
    return wrapper                                              #nuovamente facciamo in modo che eseguita l'operazione "wrapper"
#                                                               #questa ritorni al punto di partenza fino a quando non la facciamo ripartire

@mio_decoratore                  #si mette una chiocciola al nome del decoratore, proprio per creare la funzione
#                                #decoratrice, e la si mette sopra alla funzione che vogliamo decorare
def saluta():                    #la funzione saluta() mi stamperà la stringa "Ciao" ogni volta che la richiamerò
    print("Ciao!")               

# Uso
saluta()                         #sto richiamando la funzione saluta() che verrà decorata 



class Persona:                     #definisco una classe nella quale metterò una una serie di funzioni, metodi e in questo caso anche dei decoratori
    def __init__(self, nome):      #__init__ è un metodo magico che si mette quando si crea una classe nella quale metto degli attributi che utilizzo
        self._nome = nome          #e inizializzo con il metodo self. che mi permetterà di metterci elementi differenti per i diversi oggetti
    
    @property                      #è un decoratore che permette di leggere un dato senza poterlo modificarlo in modo diretto
    def nome(self):                #nel caso non fosse seguito dal decoratore setter l'elemento all'interno dell'oggetto non è modificabile
        return self._nome
    
    @nome.setter                  #questo decoratore @---.setter mi permette di modificare un elemento appartente al suo attributo dell'oggetto tramite
    #                             #una funzione che mette una serie di condizioni che verificano che l'elemento che voglio modificarepotendo aggiungere
    def nome(self, nuovo_nome):   
        if isinstance(nuovo_nome, str) and len(nuovo_nome) > 0:  #sia corretto
            self._nome = nuovo_nome
        else:
            raise ValueError("Il nome deve essere una stringa non vuota.")
    
    @nome.deleter                #decoratore che mi permette di cancellare dalla memoria un elemento protetto dal decoratore @property
    def nome(self):
        print("Sto cancellando il nome...")
        del self._nome


persona1 = Persona("Mario")               #creo un oggetto appartenente alla classe Persona. All'interno delle parentesi scrivo, nell'ordine
print(persona1._nome)                     #dichiarate all'inizio, gli elementi appartenteti agli attributi                                 
persona1.nome = "Luigi"                   #sto modificando il nome precedentemente dato
print(persona1._nome)

del persona1.nome                         #Cancello l'elemento appartente alla chiave nome

class Matematica:                         
    @staticmethod                         #decoratore che applica un metododo statico 
    def addizione(a, b):                  #metodo
        return a + b                      #ritorno del metodo subito dopo aver eseguito la somma, risultato visualizzato nel terminale


print(Matematica.addizione(5, 3))        #mi stampa la somma. richiamo il metodo tramite la classe d'appartenenza
#                                        #attribuendo gli argomenti ai paramentri corrispondenti

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def __repr__(self):                  #metodo utilizzato dai programmisti per visualizzare i metodi di tutte gli oggetti in modo più dettagliato
        return f"Persona(nome ='{self.nome}', età = {self.età})"

persona1 = Persona("Luigi", 25)
persona2 = Persona("Genoveffo", 23)
print(repr(persona1))  # Output ufficiale dettagliato con __repr__
print(repr(persona2))