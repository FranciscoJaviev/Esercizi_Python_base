#Nome Script: esercitazione13.py 
#Descrizione:esercitazioni varie fatte sulle Classi
#Autore:[Francisco J. Scognamiglio]
#Data:[6 Marzo 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]



#Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno.
#Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da 
#Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore()

class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def accelera (self): 
        print("l'auto " +self.marca, "accellera ")   

    def frena (self):
        print("l'auto " +self.modello, "frena ")
         
automobile = Veicolo("Ferrari","Testa Rossa", "2024")
automobile.accelera()
automobile.frena()

class Auto(Veicolo):

    def __init__(self, nome, modello, anno, colore):
        super().__init__(nome, modello, anno )
        self.colore = colore
        

    def cambio_colore (self,nuovo_colore):
        self.nuovo_colore = nuovo_colore
        print (f"la {self.marca} ha colore {self.nuovo_colore}")

           
automobile1 = Auto("ferrari","testa rossa", "2024", "rossa")
automobile1.cambio_colore("giallo")
   

#Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo,
#in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: 
#Enzo, Anno: 2004, Colore: Rosso”.

class Auto:
    def __str__(self,nome,modello,anno,colore):
        super().__str__(nome, modello, anno, colore)
        print ("la mia auto")

automobile2 = Auto("ferrari","testa rossa", "2024", "rossa")
automobile2.__str__()



#crea una calsse scuola: nome, cognome, età, con metodo sezine con sotto classe docenti, collaboratori, diriggenti, amministrazione
#nella sottoclasse docenti aggiungi metodo la materia insegna  e vicari, per i collaboratori il piano in cui lavorano, stanza e amministratore per gli amministatori
#per i diriggenti metodi diriggente e vice diriggenti per tutti lo stipendio

class Datipersonali:
    def __init__(self, nome, cognome, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo

    def get_indirizzo(self):
        return  self.indirizzo
    def get_età(self):
        return self.indirizzo
    def set_indirizzo (self, indirizzo):
        self._indirizzo = indirizzo 
    def personale(self):
        raise NotImplementedError("Questo metodo deve essere sovrascritto dalle classi figlie")


class Personale (Datipersonali):
    def __init__(self, nome, cognome, indirizzo, stipendio):
        super().__init__(nome, cognome, indirizzo)
        self.stipendio = stipendio
        
    def get_stipendio(self):
        return self.stipendio
    def set_stipendio(self,stipendio):
        self.stipendio = stipendio
    def personale(self):
        return f"{self.nome} {self.cognome} in via{self.indirizzo}. Con stipendio {self.stipendio}"
        

class Collaboratori(Personale):
    def __init__(self, nome, cognome, indirizzo, stipendio, piano, mansione):
        super().__init__(nome, cognome, indirizzo, stipendio)
        self.mansione = mansione
        self.piano = piano

    def get_piano(self):
        return self.piano
    def set_piano(self,piano):
        self.piano = piano
    def personale(self):
        return f"{self.nome} {self.cognome} in via{self.indirizzo}. Con mansione {self.mansione} \nprende stipendio {self.stipendio}"

        
class Docenti(Personale):
    def __init__(self, nome, cognome, indirizzo, stipendio, materia):
        super().__init__(nome, cognome, indirizzo, stipendio)
        self.materia = materia
    def get_materia(self):
        return self.materia
    def set_materia(self,materia):
        self.materia = materia
    def personale(self):
        return f"{self.nome} {self.cognome} in via{self.indirizzo}.\nMateria di insegnamento {self.materia} \nprende stipendio {self.stipendio}"

class Alunni (Datipersonali):
    def __init__(self, nome, cognome, indirizzo, voto):
        super().__init__(nome, cognome, indirizzo) 
        self.voto = voto
    def get_materia(self):
        return self.voto
    def set_materia(self, voto):
        self.voto = voto
    def personale(self):
        return f"{self.nome} {self.cognome} \nin via {self.indirizzo}. Con voto {self.voto}"
 
def persone (personale):
    for persone in personale:
        print(persone.personale())


personale =[
 Collaboratori("Luca", "Mat", "via...", "2000Euro", "primo piano", "bidello"),
 Docenti("Lucia", "Satta", "via..", "2100Euro", "Matematica"),
 Alunni ("Andrea", "Mastropiedo", "via.", "6/10") ]

persone(personale)