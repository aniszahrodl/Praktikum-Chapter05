from random import randint
total=0
while True:
    bil=randint(0,10)
    total= total + 1
    print(bil)
    if bil == 5:
        break    
print('Jumlah perulangan:', total)

