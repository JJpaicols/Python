input_name = input("Please, enter ur name: ->")

if input_name:

    first_letter = input_name[0].upper()

    others_letters = input_name[1:].lower()

    formatted_name = first_letter + others_letters

    print(f"Ur formatted name is --> {formatted_name} ")

else:

    print("U did not enter a name...")
