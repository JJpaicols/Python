# Programma che calcola la somma dei primi n numeri dispari

# Chiede all'utente quanti numeri dispari sommare
n = int(input("Quanti numeri dispari vuoi sommare? "))

somma = 0
numero = 1  # primo numero dispari

for i in range(n):
    somma += numero
    numero += 2  # passa al successivo numero dispari

print("La somma dei primi", n, "numeri dispari è:", somma)
