def zacina(seznam):
    slovo = []
    zacatek = []
    for zvire in seznam:
        zacatek = zvire[0]
        if zacatek == 'k':
            slovo.append(zvire)
            print(slovo)

zvirata = ['pes', 'kočka', 'králík', 'had']
zacina(zvirata)
