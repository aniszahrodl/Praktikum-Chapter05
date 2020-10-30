import random

a= random.randint(0,100)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!')

tebakanBenar= False

while not tebakanBenar:
    b=int(input('Tebakan anda:'))
    if b==a:
        print('Yeee... Bilangan tebakan anda BENAR :-)')
        break
    elif b>a:
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    elif b<a:
        print('Hehehe... Bilangan tebakan anda terlalu kecil')

