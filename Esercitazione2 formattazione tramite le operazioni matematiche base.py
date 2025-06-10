#Nome Script: es2.py 
#Descrizione: esercitazioni per imparare ad utilizzare la formattazione tramite le 
            # operazioni matematiche base

#Autore:[Francisco J. Scognamiglio]
#Data:[5 febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIT]



#primo tipo di formattazione 

#Nel terminal mi comparirà la scritta "il mio numero è" e
#digiterò un numero, si ripeterà due volte e in conclusione vi uscirà la somma


numero =int(input("il mio numero è"))
numero2 = int(input("il mio numero è")) 
somma = numero + numero2
print ("la somma è:", somma) 

print ("-----------")

#Francisco J. Scognamiglio 6 febbraio 2025


print ("----------")
#secondo tipo di fommattazione

#Definire una costante per il valore di pi greco e usarla per calcolare la circonferenza di un cerchio di raggio 5. 
PI_GRECO = 3.1415
raggio = 5 
print (f"la circonferenza del cerchio è:  {2 * raggio * PI_GRECO}")


print ("---------")
#Definire una costante per il valore della gravità terrestre e usarla per calcolare il peso di un oggetto di massa 10 kg.

costante_g = 9.81
massa = 10 
print (f"il peso della massa è: {costante_g * massa}")


print("---------")
#Definire una costante per il tasso di cambio euro-dollaro e usarla per convertire 100 euro in dollari.

tasso = 1.04
dollari = 100
print (f"100 dollari valgo in euro: {dollari / tasso}")


print ("fine esercitazione2")
