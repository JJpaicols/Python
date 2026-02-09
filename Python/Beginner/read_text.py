# Nome del file di input
NOME_FILE = "testo.txt"

def analizza_testo_base():
    """
    Legge il file, conta le occorrenze delle lettere (a-z) 
    e calcola la frequenza percentuale, usando solo costrutti base.
    """
    
    # 1. Inizializzazione
    conteggio = {}
    totale_lettere = 0
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    # 2. Apertura e Lettura del File
    try:
        # Tenta di aprire il file. Se fallisce, il programma terminerà qui.
        file = open(NOME_FILE, 'r', encoding='utf-8')
        contenuto = file.read()
        file.close()
    except FileNotFoundError:
        print(f"ERRORE: File '{NOME_FILE}' non trovato. Assicurati che esista.")
        return # Termina la funzione in caso di errore
    
    # 3. Iterazione e Conteggio
    for carattere in contenuto:
        # Conversione in minuscolo
        carattere_minuscolo = carattere.lower()
        
        # Verifica se il carattere è una lettera dell'alfabeto
        if carattere_minuscolo in alfabeto:
            # Aggiorna il conteggio
            
            # Verifica se la lettera è già nel dizionario
            if carattere_minuscolo in conteggio:
                conteggio[carattere_minuscolo] = conteggio[carattere_minuscolo] + 1
            else:
                # Inizializza il conteggio se è la prima occorrenza
                conteggio[carattere_minuscolo] = 1
            
            totale_lettere = totale_lettere + 1

    # 4. Calcolo e Stampa dei Risultati
    
    if totale_lettere == 0:
        print("Nessuna lettera valida trovata nel testo.")
        return

    print("--- Risultati Analisi ---")
    print(f"Totale lettere valide contate: {totale_lettere}")
    print("-" * 25)

    # Prepara le chiavi ordinate per la stampa
    lettere_ordinate_chiavi = sorted(conteggio.keys())
    
    print("## Conteggio Lettere")
    for lettera in lettere_ordinate_chiavi:
        print(f"Lettera '{lettera}': {conteggio[lettera]}")

    print("\n## Frequenza Percentuale")
    
    # Calcola e stampa le frequenze
    for lettera in lettere_ordinate_chiavi:
        conteggio_l = conteggio[lettera]
        
        # Calcolo della frequenza percentuale
        frequenza = (conteggio_l / totale_lettere) * 100
        
        # Stampa formattata
        print(f"Lettera '{lettera}': {frequenza:.4f}%")

    print("-" * 25)

# ----------------------------------------------------
# Esecuzione del Programma
# ----------------------------------------------------

# NOTA IMPORTANTE: Per far funzionare questo codice, DEVI creare 
# manualmente un file chiamato 'testo.txt' nella stessa cartella 
# in cui salvi ed esegui il programma Python. 

if __name__ == "__main__":
    analizza_testo_base()
