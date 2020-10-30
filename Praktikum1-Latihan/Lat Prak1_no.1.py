a=int(input('Masukkan nilai Bahasa Indonesia:',))
b=int(input('Masukkan nilai Bahasa Matematika:'))
c=int(input('Masukkan nilai Bahasa IPA:'))
d=print('Status Kelulusan:', end= ' ')

if(a < 0) or (b < 0) or (c < 0):
    print(' ')
elif(a > 100) or (b > 100) or (c > 100):
    print(' ')
elif(a < 60) or (b <= 70) or (c < 60):
    print('TIDAK LULUS')
else:
    print('LULUS')
