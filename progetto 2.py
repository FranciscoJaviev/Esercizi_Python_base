#Nome Script: progetto2.py 
#Descrizione: script basato su funzioni per calcolare il perimetro e l'araea di alcune figure geometriche
#Autore:[Francisco J. Scognamiglio]
#Data:[15 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]

#le definizioni devono essere messe prima del ciclo

def quadrato():
     lato = float(input("il lato del quadrato è: "))
     perimetro = lato*4
     area = lato**2
     print(perimetro)
     print (area)

def triangolo():
  b = float(input("la base misura:"))
  l = float(input("il lato misura:"))
  h = float(input("l'altezza misura:"))
  area = (b+h)/2
  perimetro = (b+2*l)/2
  print(perimetro)
  print(area)

def rettangolo():
  l_min = float(input("la lato minore è: "))
  l_max = float(input("il lato mggiore è: "))
  perimetro = (2*(l_min+l_max))
  area = l_min*l_max
  print(perimetro)
  print(area)


def cerchio():
   raggio = float(input("il raggio misura: "))
   perimetro = P_GRECO*raggio
   area = P_GRECO*raggio**2
   print (perimetro)
   print(area)
  

#Costanti 
P_GRECO = 3,1415926535
risposta = "il_risultato_è"




def menu():
   
   print("Benvenuto nel programma di calcolo delle figure geometriche")
   while True:
 
    print("digita 1 calcola perimetro del quadrato")
    print("digita 2 calcola area del quadrato")
    print("digita 3 calcolare perimetro triangolo")
    print("digita 4 calcolare area triangolo")
    print("digita 5 per calcolo circonferenza cerchio")
    print("digita6 per area cerchio")

    scelta_1 = input("fai la tua scelta ")
        
    if  "1" in scelta_1:
       quadrato()
    elif "2" in scelta_1:
      triangolo()
    elif "3" in scelta_1:
     rettangolo()
    elif "4" in scelta_1:
     for x in range(1,5):
      cerchio()
    elif "a" in scelta_1:
      break
    else:
      print("scelta sbagliata")

menu()




















