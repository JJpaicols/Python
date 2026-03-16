#PROCESSO SERVER: colui che eroga servizi, per esempio di comunicazione

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

    IP_PORTA = ("127.0.0.1",12000)

    s.bind(IP_PORTA)#assegno i valori al socket 's'

    #ora il socket può essere usato per comunicare

    BUFFER_SIZE = 4096
    #i dati sono stringhe binarie 
    dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE)#BLOCCANTE!!!!!!
    stringa = dati.decode()#trasforma i dati binari
    print(stringa)

    #chiudo il socket
    s.close()

if __name__ == "__main__":


