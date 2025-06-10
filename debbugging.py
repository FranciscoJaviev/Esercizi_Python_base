#se faccio partire il debbugging (dopo aver messo degli step) noterò che mi si apre una finestrella 
# in alto con delle frecette. La prima (curva con puntino) serve per l'esecizio uno quello che vedo è il processo step per step, analizzando
#così bene quello che fa la mia funzione for


"""esercizio 1"""

n = 0

for i in range (4):
    n = n+1
    
print(n)





# nel caso invece dell'esecizio 2 con le funzioni per avere lo stesso procedimento devo utilizzare le freccia successive.
#quelle dritte con il puntino. Hanno la stessa funzione ma servono per script nella quale abbiamo delle funzioni (def)
#anche in questo caso potrò analizzare il processo passo dopo passo


"""esercizio 2"""

def saluta(nome):
    messaggio = crea_messaggio (nome)
    stampa_messaggio(messaggio)

def crea_messaggio(messaggio):
    print(messaggio)

def  stampa_messaggio(nome):
    return f'ciao{nome}'

saluta("Francisco")


nome ="vasilic"
cognome ="javier"