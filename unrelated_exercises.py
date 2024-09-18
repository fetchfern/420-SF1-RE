
def nombre_valide():
    nbr_string = input('votre mot de passe: ')

    try:
        nbr_converti = int(nbr_string)
    except ValueError as _:
        print('nombre invalide')
        return

    if nbr_converti % 2 == 0 and '5' in nbr_string and (200 >= nbr_converti >= 100):
        print('nombre OK')
    else:
        print('nombre invalide')



if __name__ == '__main__':
    while True:
        nombre_valide()
