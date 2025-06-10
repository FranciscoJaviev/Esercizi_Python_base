#Nome Script: Esame di Python base.py 
#Descrizione: creare uno script con interfaccia che calcoli il perimetro e l'area di alcune forme geometriche base
#Versione: 1.0
#Autore:[Francisco J. Scognamiglio]
#Data:[31.10.25 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]

'''
Pseudocodice:
ho creto un calcolatore che calcoli l'area e il perimetro di alcune formule geometri in un interfaccia grafica.
Ho creato una funzione principale chiamata "operazione" nella quale sono state inserite quattro funzioni che richiamano le figure geometriche;
per ogniuna di queste ho creto una interfaccia che mi permette di inserire i valori corrispondenti a ciascuna figura.
Alla fine ho creato l'interfaccia principale che mi permette di scegliere la figura geometrica sulla quale voglio calcolare il perimetro e l'area

'''

import math
import tkinter as tk
from tkinter import messagebox
   
def operazione():
    #ho chiusto tutto il mio cadice con un try-except così da poter visualizzati eventuali errori sia
    #nel codice che quelli dovuti  ad un eventuale utente
    try:
     scelta = operation_var.get()
     if scelta == "quadrato":

      #creo la funzione corrispondente che mi permette di calcolare il perimentro e l'area del quadrato
      def quadrato():
       l = float(lato.get())
       perimetro = l*4
       area = l**2
       risultato1.config(text=f"Perimetro: {perimetro}")
       risultato2.config(text=f"Area: {area}")

      #creo l'interfaccia corrispondente al quadrato dove posso scrivere il valore del lato e tramite
      #il tasto "calcola", avere visualizzato i risultati nella stessa interfaccia
      root = tk.Tk()
      root.title("Calcolo perimetro e area")
      root.geometry("200x330")
      label1 = tk.Label(root, text="Lato:")
      label1.pack()
      lato = tk.Entry(root)
      lato.pack()
      btn_calculate = tk.Button(root, text="Calcola", command=quadrato)
      btn_calculate.pack()
      risultato1 = tk.Label(root, text="Perimetro: ")
      risultato1.pack()
      risultato2 = tk.Label(root, text="Area: ")
      risultato2.pack()
      root.mainloop() 

      #si reitera lo schema precedente per tutte le altre funzioni
     elif scelta == "triangolo":
      def triangolo():
        l = float(lato.get())
        b = float(base.get())
        h = float(altezza.get())
        area = (b+h)/2
        perimetro = (b+2*l)/2
        risultato1.config(text=f"Perimetro: {perimetro}")
        risultato2.config(text=f"Area: {area}")

      root = tk.Tk()
      root.title("Calcolo perimetro e area")
      root.geometry("200x300")
      label1 = tk.Label(root, text="Lato:")
      label1.pack()
      lato = tk.Entry(root)
      lato.pack()
      label2 = tk.Label(root, text="Base:")
      label2.pack()
      base = tk.Entry(root)
      base.pack()
      label3 = tk.Label(root, text="Altezza:")
      label3.pack()
      altezza= tk.Entry(root)
      altezza.pack()
      btn_calculate = tk.Button(root, text="Calcola", command=triangolo)
      btn_calculate.pack()
      risultato1 = tk.Label(root, text="Perimetro: ")
      risultato1.pack()
      risultato2 = tk.Label(root, text="Area: ")
      risultato2.pack()
      root.mainloop()
     elif scelta =="rettangolo":
      def rettangolo():
       l_min = float(minimo.get())
       l_max = float(massimo.get())
       perimetro = (2*(l_min+l_max))
       area = l_min*l_max
       risultato1.config(text=f"Perimetro: {perimetro}")
       risultato2.config(text=f"Area: {area}")
      
      root = tk.Tk()
      root.title("Calcolo perimetro e area")
      root.geometry("200x300")
      label2 = tk.Label(root, text="Lato massimo:")
      label2.pack()
      massimo = tk.Entry(root)
      massimo.pack()
      label3 = tk.Label(root, text="Lato minimo")
      label3.pack()
      minimo= tk.Entry(root)
      minimo.pack()
      btn_calculate = tk.Button(root, text="Calcola", command=rettangolo)
      btn_calculate.pack()
      risultato1 = tk.Label(root, text="Perimetro: ")
      risultato1.pack()
      risultato2 = tk.Label(root, text="Area: ")
      risultato2.pack()
      root.mainloop()
     elif scelta =="cerchio":
      def cerchio():
       raggio = float(r.get())
       perimetro = math.pi*raggio
       area = math.pi*raggio**2
       risultato1.config(text=f"Perimetro: {perimetro}")
       risultato2.config(text=f"Area: {area}")

      root = tk.Tk()
      root.title("Calcolo perimetro e area")
      root.geometry("200x300")
      label = tk.Label(root, text="Raggio:")
      label.pack()
      btn_calculate = tk.Button(root, text="Calcola", command=cerchio)
      btn_calculate.pack()
      risultato1 = tk.Label(root, text="Perimetro: ")
      risultato1.pack()
      risultato2 = tk.Label(root, text="Area: ")
      risultato2.pack()
      r = tk.Entry(root)
      r.pack()
      root.mainloop()
    except Exception as e:
     print(f"Errore rilevato: {type(e).__name__} - {e}")



#schermata iniziale
root = tk.Tk()
root.title("Calcolo perimetro e area")
root.geometry("600x200")

#tasto per la scelta della figura
label_op = tk.Label(root, text="Figura:")
label_op.pack()
operation_var = tk.StringVar(value='figura')
operations = ['quadrato', 'rettangolo', 'triangolo', 'cerchio']
dropdown = tk.OptionMenu(root, operation_var, *operations)
dropdown.pack()
#tasto che mi permette di avviare il calcolo del perimetro e dell'area della figura scelta
btn_calculate = tk.Button(root, text="Calcola", command=operazione)
btn_calculate.pack()
root.mainloop()