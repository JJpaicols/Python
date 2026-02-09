class Punto ():
    #costruttore
    def __init__(self, x, y): #self è come this in Java
        self.x = x
        self.y = y
    
    def __str__(self): #metodo per rappresentazione in stringa 
        #deve ritornare una stringa
        return f"Punto({self.x}, {self.y})"


    
    

def main():
    a = Punto(1, 2) #istanza di punto
    b = Punto(3, 4) #istanza di punto
    print(a.x, a.y, b.x, b.y) #stampa gli attributi dell'istanza

if __name__ == "__main__":
    main()