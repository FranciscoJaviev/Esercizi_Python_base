#Nome Script: esercitazione12.py 
#Descrizione:esercitazioni varie fatte sulle Classi
#Autore:[Francisco J. Scognamiglio]
#Data:[3 Marzo 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]



#Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso.
#Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, 
#ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:
    def __init__(self, nome, cognome, età, sex):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.sex = sex

    def presentati(self):
        print ("Ciao mi chiamo "+ self.nome, "e ho" +self.età)
        
        
amico1 = Persona("Marco","Giola","32", "maschio")    

amico1.presentati()




#Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
#Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
#Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

class Animale:
    def __init__(self, nome, suono, specie):
        self.nome = nome
        self.suono = suono
        self.specie = specie
        
    def emetti_suono(self):
        if self.nome == "gatto":
         print("Sono un "+ self.nome, "il mio verso è "+ self.suono)
        elif self.nome == "cane":
         print ("Sono un "+ self.nome, "il mio verso è "+ self.suono)

animale1 = Animale("gatto","Miao", "canino")
animale1.emetti_suono()



#Creare una classe Automobile che abbia gli attributi “marca”,
#“modello” e “anno”. Aggiungi un metodo “descrivi” che stampi 
#una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.

class Automobile:
   def __init__(self, marca, modello, anno):
      self.marca = marca
      self.modello = modello
      self.anno = anno

   def descrivi(self): 
       print(f"Questa è una {self.marca} {self.modello} del {self.anno}")
   

auto = Automobile("Toyota","Corolla","2017")
auto.descrivi()


#Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, 
#“matricola” e “stipendio”. Aggiungere un metodo “aumenta_stipendio” 
#che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” 
# che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, 
# matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipedio = stipendio

    def aumenta_stipendio(self):
        self.stipedio = (self.stipedio*0.1)+self.stipedio
        print (f"Impiegato {self.nome} {self.cognome}, matricola {self.matricola}, stipendio {self.stipedio:.3f} Euro")

    def stampa_dettagli (self):
        print (f"Impiegato {self.nome} {self.cognome}, matricola {self.matricola}, stipendio {self.stipedio} Euro")



impiegato1 = Impiegato("Gianluigi", "Pierantonio", "24692545", 2900)
impiegato1.stampa_dettagli()
impiegato1.aumenta_stipendio()

    





#Esercizio 5
#Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
#Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
#Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese

#La classe dovrà avere i seguenti metodi:
#Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
#Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
#Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
#Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta


class GestoreMagazino(Prodotto):
    def __init__(self, nome, prezzo, scorta, costo_magazzinaggio):
        super().__init__(nome, prezzo, scorta)
        self.prodotti = {}
        self.costo_magazzinaggio = costo_magazzinaggio
        
    def aggiungi_prodotto(self,prodotto):
        self.prodotti[prodotto.nome] = prodotto
           
    def rimuovi_prodotto(self, nome_prodotto):
        self.prodotti.pop(nome_prodotto)
        

    def calcola_costi_magazzinaggio(self, nome):
        costi = 0
        for nome, prodotto in self.prodotti.items():
            costi += prodotto.scorta * self.costo_magazzinaggio
        return costi
        
p1 = Prodotto("telefono", 500, 10)
p2 = Prodotto("computer", 1000, 5)

gm = GestoreMagazino(10)

gm.aggiungi_prodotto(p1)
gm.aggiungi_prodotto(p2)

print(gm.calcola_costi_magazzinaggio())

gm.rimuovi_prodotto("telefono")

print(gm.calcola_costi_magazzinaggio())





