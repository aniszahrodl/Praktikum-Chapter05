import random

a= random.randint(0,100)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!')
score= 100

while True:
    b=int(input('Tebakan anda:'))
    if b==a:
        print('Yeee... Bilangan tebakan anda BENAR :-)')
        print ('Score Anda:', score)
        break
    elif b>a:
        score = score -2
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    elif b<a:
        score = score -2
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
    if score<0:
        print ('score anda sudah habis')
        break
    
   
    
