#Nome Script: esercitazione11.py 
#Descrizione:esercitazioni varie fatte sui decoratori
#Autore:[Francisco J. Scognamiglio]
#Data:[26 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]


#Implementare un decoratore che converte l'output di 
#una funzione in maiuscolo

def messaggio (fuk):
    def wrapper(*arg, **kwargs):

        print ("il saluto è:")
        parola_iniziale = fuk (*arg, **kwargs)
        parola_finale = parola_iniziale.upper()
        return parola_finale
    
    return wrapper


@messaggio
def saluto():

    parola = "ciao"
    
    return parola
    

print(saluto())

#Scrivere un decoratore che controlla se l'input 
#di una funzione è non negativo.

def positivo(func):
    def wrapper (*arg, **kwargs):

        
        funzione = func(*arg, **kwargs)
        print("la funzione è positiva?")
        if funzione > 0: print ("positiva")
        else: print ("negativa")

        return funzione
    
    return wrapper


@positivo
def funzione_1():
    
    return numero


numero = int(input("il numero è:"))
funzione_1()




#Creare un decoratore che limita il numero di volte che una funzione
#può essere chiamata.

def chiamata(func):
    
    def wrapper (*arg, **kwargs):
     for chiama in range(4):
        if chiama < 4:
         saluto = func(*arg,**kwargs)
        return saluto
    return wrapper

@chiamata

def ciclo():
    saluto = "ciao"
    print (saluto)
ciclo()

#Implementare un decoratore `@authenticate` che richiede una password 
#prima di eseguire la funzione decorata.

def autenticate (func):
    def wrapper (*arg, **kwargs):
        password = int(input("mettere la password: "))
        if password == "1234":
         pas = func (*arg, **kwargs)
         return pas
        else: 
           print("ritenta")
           return password
    return wrapper

@autenticate

def messaggio():
    messaggio = "segreto"
    return messaggio
print(messaggio())
    

#Scrivere un decoratore `@type_check` che assicura che gli argomenti 
#passati a una funzione corrispondano ai tipi attesi.


def numero(correct_type):
 def type_check(func):
    def wrapper (*arg):
        if not isinstance(arg, correct_type):
           print("non è corretto")
           
        messaggio = func(*arg)
        return messaggio
    return wrapper
 return type_check

@numero(int)

def cubo(x):
    cubica = x**3
    return cubica

print(cubo(3))


#creare una classe Moto e con proprietà marca, modello, cilindrata stampare con il metodo speciale __str__

class Moto:
   def __init__(self, marca, modello, cilindrata):
      self.marca = marca
      self.modello = modello
      self.cilindrata = cilindrata

   def __str__(self):
      return  f"moto di marca: {self.marca}, modello: {self.modello} \ndi cilindrata {self.cilindrata} cc"
   def motorino (self):
     print (f"moto di marca: {self.marca}, modello: {self.modello} \ndi cilindrata {self.cilindrata} cc")
   def __repr__(self):
      return f"Moto(moto di marca: {self.marca}, modello: {self.modello} \ndi cilindrata {self.cilindrata} cc)"
   
   
moto = Moto("Ducati", "Ducati Monster Senna", 937)   
print (moto)
moto.motorino()
print(repr(moto))