CMD_QUIT = 'quit'
CMD_HELLO = 'hello'

if __name__ == '__main__':
    while True:
        try:
            arguments = input('(): ').split()
        except KeyboardInterrupt as _:
            # pour gerer les interrupt comme ctrl-c proprement
            break
        else:
            if len(arguments) == 0:
                print('erreur: aucun arguments donne')
                continue

            commande = arguments[0]

            if commande == CMD_QUIT:
                break
            elif commande == CMD_HELLO:
                sujet = arguments[1] if len(arguments) >= 2 else 'world'
                print(f'hello {sujet}')
            else:
                print(f'erreur: commande "{commande}" inconnue')
