#PROCESSO CLIENT: colui che eroga servizi, per esempio di comunicazione del server

import socket  #built-in

def main():
    '''
    un socket è un END-POINT di comunicazione, ogni programma che vuole comunicare deve avere un socket al 
    suo interno.
    '''
    #1) creare un SOCKET
    #2) solo sul server: legare il SOCKET a indirizzo IP+PORTA
    #   la porta è un numero (16 bit) che indirizza un processo nel computer
    #   le porte < 1024 si chiamano WELL-KNOWN(ben note), sono usate da servizi di default, DA NON USARE
    #                      IPV4                UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket con le caratteristiche: 

    messaggio = "ciao"

    DESTINATARIO = ("127.0.0.1", 12000)
    s.sendto(messaggio.encode(), DESTINATARIO)

    #chiudo il socket
    s.close()

if __name__ == "__main__":
    main()
    
