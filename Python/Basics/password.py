password = input ("inserisci un password ->")
password_blanked = '*'* len(password)
print(f"hai inserito la passsword {password_blanked}")
first_letter_password = password [0]
last_letter_password = password [-1]
print(f"\nla prima lettera della passowrd è {first_letter_password} e l'ultima è {last_letter_password}")
