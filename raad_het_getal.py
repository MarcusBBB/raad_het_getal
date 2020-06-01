import random

ja = ['ja', 'j', 'yes', 'zeker' , 'graag', 'leuk', 'oke', 'y']
nee = ['nee', 'n', 'no', 'stop', 'quit']

# startvraag en bepaal getal
def start():
    while spelen == True:
        begin = input('Wil je raad het getal spelen? ')
        if begin in ja:
            getal = random.randint(1,20)
            return getal, True
        elif begin in nee:
            getal = None
            return getal, False
        else:
            print('Ik kan je reactie niet plaatsen')

def raden(getal):
    keuze = int()
    while keuze != getal:
        keuze = int(input('Oké, welk getal raad je tussen de 1 en de 20? '))
        if keuze > getal:
            print('te hoog!')
        elif keuze < getal:
            print('te laag!')
    print('Goed geraden!!! \n Nog een keer?')
    return

spelen = True
while spelen == True:
    getal, spelen = start()
    if getal != None:
        raden(getal)

print('bedankt voor het spelen!')







