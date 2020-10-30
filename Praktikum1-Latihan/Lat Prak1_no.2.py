a=int(input('Masukkan nilai Bahasa Indonesia:'))
b=int(input('Masukkan nilai Bahasa Matematika:'))
c=int(input('Masukkan nilai Bahasa IPA:'))

if(a < 0) or (b < 0) or (c < 0):
    print('Maaf input yang anda masukkan tidak valid')
elif(a > 100) or (b > 100) or (c > 100):
    print('Maaf input yang anda masukkan tidak valid')
elif(a < 60) or (b <= 70) or (c < 60):
    print('Status Kelulusan: TIDAK LULUS')
else:
    print('Status Kelulusan: LULUS')
