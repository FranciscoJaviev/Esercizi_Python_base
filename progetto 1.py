#Nome Script: progetto1.py 
#Descrizione: creare un programmino che permetta all'utente di vedere i prodotti presenti nel negozio 
            # successivamente avere la possibilità di prendere l'oggetto oppure aggiungerlo
#Autore:[Francisco J. Scognamiglio]
#Data:[febbraio 2025] 
#Copyright: [FranciscoJ.Scognamiglio] [2025]
#Licenza:[MIt]



la_mia_variabile = True

lista_prodotti = ("tv", "P.C", "Smartphon")
numero_prodotti = [3, 3, 3]

while la_mia_variabile:

    print (lista_prodotti)
    print(numero_prodotti)

    scelta = input("quale è la tua scelta?")
    if "e" in scelta:
       la_mia_variabile = False

    elif "acquisto" in scelta:

        prodotto = input("inserisci prodotto d'acquisto:")
   
        if "tv" in prodotto: 
            print ("acquisto  tv effettuato . Arrivederci")
            numero_prodotti[0] -= 1
        elif "P.C." in prodotto:
            print ("acquisto P.C. effettuato. Arrivederci") 
            numero_prodotti[1] -= 1
        else: print ("acquisto Smartphon affettuato. Arriverci") 
        numero_prodotti[2] -= 1
    
    elif "aggiungere" in scelta: 
        
        prodotto = input("quale prodotto desideri aggiungere?")
    
        if "tv" in prodotto: 
          print ("prodotto 1 aggiunto. Grazie")
          numero_prodotti[0] += 1
        elif "P.C" in prodotto: 
          print ("prodotto 2 aggiunto. Grazie")
          numero_prodotti[1] += 1
        else: print ("prodotto 3 aggiunto. Grazie")
        numero_prodotti[2] += 1

    else: print ("ripetere l'operazione")



prodotti = {"prodotti":["tv", "P.C.","smartphon"] ,"numero_dispositivi":[2,2,2]}

la_mia_variabile = True

schermata_iniziale = ("aquisto ordine tasto 1""\n""restituisci prodotto tasto 2")

while la_mia_variabile:
    print (schermata_iniziale)

    scelta = input("Fai la tua scelta:")
    if "s" in scelta: la_mia_variabile = False

    elif "1" in scelta:
        for x,y in prodotti.items(): 
         print(x,y)
    
        acquisto = input("inserisci prodotto d'acquisto:")
        if "tv" in acquisto:
            tv = prodotti["numero_dispositivi"][0]
            if tv > 0:
                 print("prodotto acquisto")
                 prodotti["numero_dispositivi"][0] -= 1
            else: print ("prodotto finito")
        elif "P.C." in acquisto:   
            pc = prodotti["numero_dispositivi"][1]
            if tv > 0:
                 print("prodotto acquisto")
                 prodotti["numero_dispositivi"][1] -= 1
            else: print ("prodotto finito")
        elif "smartphon" in acquisto:
            smart = prodotti["numero_dispositivi"][2]
            if tv > 0:
                 print("prodotto acquisto")
                 prodotti["numero_dispositivi"][2] -= 1
            else: print ("prodotto finito")
        else: print("prodotto non trovato")  


    elif "2" in scelta:
        print (prodotti)
        reso = input("inserisci prodotto reso:")
        if "tv" in reso:
            print ("Reso della tv fatta")

            tv = prodotti["numero_dispositivi"][0]
            prodotti["numero_dispositivi"][0] += 1

        elif "P.C." in reso:  
            print ("Reso del P.C. fatta")
           
            pc = prodotti["numero_dispositivi"][1]
            prodotti["numero_dispositivi"][1] += 1
         
        elif "smartphon" in reso:
            print("Reso dello smartphon fatta")

            smart = prodotti["numero_dispositivi"][2]
            prodotti["numero_dispositivi"][2] += 1

        else: 
            quantità = input("numero prodotto restituito:")
            prodotti["prodotti"].append(reso)
            prodotti["numero_dispositivi"].appende(quantità)


