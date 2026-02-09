def leggi_registro(nome_file):
    """Restituisce un dizionario {nome: [voti]}."""
    registro = {}

    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue

            parti = riga.split(";")
            nome = parti[0].strip()
            voti = list(map(int, parti[1:]))  # converte tutti i voti in int

            registro[nome] = voti

    return registro


def calcola_media(voti):
    """Restituisce la media di una lista di voti."""
    if not voti:
        return 0
    return sum(voti) / len(voti)


def classifica(registro):
    """
    Restituisce una lista di tuple (nome, media) 
    ordinata per media decrescente.
    """
    lista_medie = []

    for nome, voti in registro.items():
        media = calcola_media(voti)
        lista_medie.append((nome, media))

    # ordina per media decrescente
    lista_medie.sort(key=lambda x: x[1], reverse=True)

    return lista_medie


def stampa_podio(classifica):
    """Stampa i primi 3 della classifica (usa slicing)."""
    podio = classifica[:3]
    print("🏆 PODIO:")
    for posizione, (nome, media) in enumerate(podio, start=1):
        print(f"{posizione}. {nome} — media {media:.2f}")


def trova_insufficienti(classifica):
    """Restituisce la lista degli studenti con media < 6."""
    return [(nome, media) for nome, media in classifica if media < 6]
