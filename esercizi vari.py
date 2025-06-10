#Nome Script: esercizi_vari.py 
#Descrizione: esercitazioni varie fatte in classe 
#Autore:[Francisco J. Scognamiglio]
#Data:[febbraio/marzo 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]





#Calcolatrice (usa input, operatori e condizioni)
a = int(input ("scrivi un numero"))
b = int(input ("scrivi un'altro numero"))

def somma (a, b):
   totale = a + b
   return totale

c = somma(a, b)


def sottrazione (a,b):
   totale = a - b
   return totale

d = sottrazione (a, b)


def moltiplicazione (a,b):
   totale = a * b
   return totale

e = moltiplicazione (a, b)

def divisione (a,b):
   totale = a / b
   return totale

f = divisione (a, b)

print(c)
print(e)
print(f)





variabile_di_inizio = True

while variabile_di_inizio:

    inizio = input ("cosa vuoi fare?")
    if "a" in inizio:
      variabile_di_inizio = False
      
      
    elif "+" in inizio:
     a = int(input ("scrivi un numero"))
     b = int(input ("scrivi un'altro numero"))
     print(somma(a, b)) 
      
      
    elif "-" in inizio:
      a = int(input ("scrivi un numero"))
      b = int(input ("scrivi un'altro numero"))
      print(sottrazione(a, b))
      
      
    elif "*" in inizio:
      a = int(input ("scrivi un numero"))
      b = int(input ("scrivi un'altro numero"))
      print (moltiplicazione(a, b))
      
      
    elif "/" in inizio:
      a = int(input ("scrivi un numero"))
      b = int(input ("scrivi un'altro numero"))
      print (divisione(a, b))
      

    else: print("operazione non valida")






inizio = input ("cosa vuoi fare?")
if "+" in inizio:
    a = int(input ("scrivi un numero"))
    b = int(input ("scrivi un'altro numero"))
    somma = lambda numero1, numero2: numero1 + numero2 
    print (somma(a, b))

elif "-" in inizio:
    a = int(input ("scrivi un numero"))
    b = int(input ("scrivi un'altro numero"))
    sottrazione = lambda numero1, numero2: numero1 - numero2
    print (sottrazione(a, b))

elif "*" in inizio:
    a = int(input ("scrivi un numero"))
    b = int(input ("scrivi un'altro numero"))
    moltiplicazione = lambda numero1 , numero2: numero1 * numero2
    print(moltiplicazione(a, b))

elif "/" in inizio:
     a = int(input ("scrivi un numero"))
     b = int(input ("scrivi un'altro numero"))
     divisione = lambda numero1, numero2: numero1 / numero2
     print (divisione(a, b))

else: print("operazione non valida")




#Gestione di una rubrica (dizionari, liste)

#Convertitore di temperatura (funzioni)

temperatura_celsius = int(input("La temperatura è:"))

def convertitore_di_temperatura (temperatura_celsius):

    temperatura_faraday = (temperatura_celsius*1.8)+32

    return temperatura_faraday

concertitore = print (convertitore_di_temperatura(temperatura_celsius))




# calcolare perimetro e area di diverse figure geometriche

lato = float(input())

def quadrato_area(n):
    lato = int(input("il lato del quadrato è: "))
    area = lato**2
    return area

area_quadrato = print(quadrato_area())

def quadrato_perimetro(n):
    
    perimetro = lato*4
    return perimetro

perimetro_quadrato = print(quadrato_perimetro(lato))

b = int(input("la base misura:"))
l= int(input("il lato misura:"))
h = int(input("l'altezza misura:"))

def rettangolo_perimetro (b,l):

  perimetro = (b+2*l)/2
  return perimetro

perimetro_rettangolo = print(rettangolo_perimetro(b,l))

    
def rettangolo_area (b,h):

  area = (b+h)/2
  return area
  
area_triangolo = print (rettangolo_area(b,h))


l_min = int (input("la lato minore è: "))
l_max = int (input("il lato mggiore è: "))

def rettangolo_perimetro(l_min, l_max):

  perimetro = 2*(l_min+l_max)
  return perimetro

perimetro_rettangolo = print (rettangolo_perimetro(l_min, l_max)) 

def rettangolo_area(l_min, l_max):

  area = l_min*l_max
  return area

area_rettangolo = print (rettangolo_area(l_min, l_max))

raggio = int(input("il raggio misura: "))

def circonferenza(raggio):

  P_GRECO = 3.14
  perimetro = P_GRECO*raggio
  return perimetro

circonferenza_cerchio = print(circonferenza(raggio))


def area_cerchio(raggio):

  P_GRECO = 3.14
  area = P_GRECO*raggio**2
  return area

area_cerchio = print(area_cerchio(raggio))



import tkinter as tk
from tkinter import messagebox



# creare una piccola calcolatrice che indichi l'ora attuale a Roma e di una città avente 
#un fuso orario differente


import pytz
from datetime import datetime

def ora1():
 New_York_tz = pytz.timezone('America/New_York')
 New_York_tz_time = datetime.now(New_York_tz)
 
 result.config(text=f"l'orario a New York è: \n{New_York_tz_time}")
 

def ora2():
 Roma = datetime.now()
 result1.config(text=f"Orario attuale a Roma è: \n{Roma}")



root = tk.Tk()
root.title("Data New York")
root.geometry("300x250")

btn= tk.Button(root, text="Visualizza Orario New York", command = ora1)
btn.pack()
result = tk.Label(root, text="Fuso Orario: ")
result.pack()
btn1= tk.Button(root, text="Visualizza Orario Roma", command = ora2)
btn1.pack()
result1 = tk.Label(root, text="Orrio Attuale: ")
result1.pack()

root.mainloop()




#creare una calcolatrice che esegua tre calcoli con funzioni trascendenti

import math

def calcolo():
    try:
       
      num = float(entry_num1.get())
      operation = operation_var.get()
      if operation == "seno":
       result = math.sin(num)
      elif operation == "log":
       result = math.log(num)
      elif operation == "arctg":
       result = math.atan(num)
      
      result1.config(text=f"Risultato: {result}")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci numeri validi")  # 

    
root = tk.Tk()
root.title("Funzioni Trascendenti")
root.geometry("500x450")


num1 = tk.Label(root, text="numero:")
num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_op = tk.Label(root, text="Operazione:")
label_op.pack()
operation_var = tk.StringVar(value='+')
operations = ['seno', 'log', 'arctg']
dropdown = tk.OptionMenu(root, operation_var, *operations)
dropdown.pack()

btn_calculate = tk.Button(root, text="Calcola", command=calcolo)
btn_calculate.pack()
result1 = tk.Label(root, text="Risultato: ")
result1.pack()

root.mainloop()




def figura():
  try:
     
   l = float(lato.get())
   b = float(base.get())
   h = float(altezza.get())
   l_min = float(minimo.get())
   l_max = float(massimo.get())
   raggio = float(r.get())
   scelta = operation_var.get()

   if scelta == "quadrato":
     perimetro = l*4
     area = l**2
     
   
   elif scelta == "triangolo":
     area = (b+h)/2
     perimetro = (b+2*l)/2
     

   elif scelta == "rettangolo":
     perimetro = (2*(l_min+l_max))
     area = l_min*l_max
  

   elif scelta == "cerchio":
     perimetro = 3.1415926535*raggio
     area = 3.1415926535*raggio**2
    
   risultato1.config(text=f"Perimetro: {perimetro}")
   risultato2.config(text=f"Area: {area}")
  except ValueError:
    messagebox.showerror("Errore", "Inserisci numeri validi")


root = tk.Tk()
root.title("Calcolo perimetro e area")
root.geometry("500x450")
#quadrato
label1 = tk.Label(root, text="Lato:")
label1.pack()
lato = tk.Entry(root)
lato.pack()

#triangolo
label2 = tk.Label(root, text="Lato base:")
label2.pack()
base = tk.Entry(root)
base.pack()
label3 = tk.Label(root, text="Lato altezza:")
label3.pack()
altezza= tk.Entry(root)
altezza.pack()
#rettangolo
label4 = tk.Label(root, text="Lato minore:")
label4.pack()
minimo = tk.Entry(root)
minimo.pack()
label5= tk.Label(root, text="Lato maggiore:")
label5.pack()
massimo= tk.Entry(root)
massimo.pack()
#cerchio
label6 = tk.Label(root, text="Raggio:")
label6.pack()
r = tk.Entry(root)
r.pack()
#tasto scelta figura
label_op = tk.Label(root, text="Figura:")
label_op.pack()
operation_var = tk.StringVar(value='figura')
operations = ['quadrato', 'rettangolo', 'triangolo', 'cerchio']
dropdown = tk.OptionMenu(root, operation_var, *operations)
dropdown.pack()
#tasto per avviare il calcolo
btn_calculate = tk.Button(root, text="Calcola", command=figura)
btn_calculate.pack()
#risultato
risultato1 = tk.Label(root, text="Perimetro: ")
risultato1.pack()
risultato2 = tk.Label(root, text="Area: ")
risultato2.pack()

# Avvio del loop principale
root.mainloop()




#creazione di Array
import numpy as np

a_3d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
b_3d = a_3d.reshape((3,3))
print (b_3d)


print("-----")


c_3d = np.arange(9).reshape((3,3))
print(c_3d)


print("-----")



d_3d = np.linspace(2.0, 3.0, num=6)
print(d_3d)


print("------")



e_3d = d_3d.reshape((3,2))
print(e_3d)


print("-----")


f_3d = np.arange(32)
g_4d = f_3d.reshape(2,2,2,2,2)
print(g_4d)


#creare variabili globali, locali, enclusing, butyting


x = 10

def variabile():
  y = 5
  global x
  x += 5
  print(y)

  def somma():
    nonlocal y 
    #global x
    return y + x
    #y += x
    #print("io valgo:", y)
    
  somma()
  print ("io sono:", x)


variabile()

#fare una closure


def operazione(m):
    def somma(numero):
        risultato = numero + m
        def moltiplicatore(numero2):
         return numero2 * risultato
        return moltiplicatore
    return somma

risultato_finale = operazione (1)(2)


print(risultato_finale(4))



#utilizzare il whit
try:
 with open("pokemon.csv", "r") as file:
  content = file.read()
  print(content)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Errore rilevato: {type(e).__name__} - {e}")




