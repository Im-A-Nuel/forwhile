import random

def generate_angka_komputer(batas):
    hasil=random.randrange(0, batas+1)
    return hasil


def game(angka_komputer):
    print('Program Tebak ===')
    menang=False
    while menang==False:
        tebakan=int(input('Masukan tebakan anda : '))
        if tebakan==angka_komputer:
            print('tebakan anda benar, Anda menang!!!')
            menang=True
        else:
            print('tebakan anda salah!')
        

angka_komputer=generate_angka_komputer(100)
game(angka_komputer)
