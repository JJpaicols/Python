n = int(input("Quanti numeri di fibonacci vuoi = -> "))

a, b = 1, 1 

if n > 2:
    
    # Stampa i primi due numeri
    print(a, end=" - ")
    print(b, end=" - ")
    
    # Calcola e stampa i restanti n-2 numeri
    for i in range(n - 2):
        
        # Aggiornamento compatto (Il nuovo b è la somma, il nuovo a è il vecchio b)
        a, b = b, a + b
        
        # Stampa l'ultimo numero calcolato
        print(b, end=" - ")
        
elif n == 2:
    print(a, end=" - ")
    print(b)

elif n == 1:
    print(a)
    
else:
    print("Non valido.")
