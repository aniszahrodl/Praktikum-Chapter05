
a= int(input('Masukkan Nilai Bahasa Indonesia:'))
b= int(input('Masukkan Nilai Matematika:'))
c= int(input('Masukkan Nilai IPA:'))

TidakLulus= (a<60) or (b<=70) or (c<60)

TidakValid= (a<0) or (b<0) or (c<0)
TidakValid2=(a>100) or (b>100) or (c>100)

if(TidakValid)or(TidakValid2):
    print('Maaf input yang anda masukkan tidak valid')
    print('Sebab:')
    if(a<0):
        print('- Nilai Bahasa Indonesia kurang dari 0')
    elif(a>100):
        print('- Nilai Bahasa Indonesia lebih dari 100')
    if(b<0):
        print('- Nilai Matematika kurang dari 0')
    elif(b>100):
        print('- Nilai Matematika lebih dari 100')
    if(c<0):
        print('- Nilai IPA kurang dari 0')
    elif(c>100):
        print('- Nilai IPA lebih dari 100')
elif(TidakLulus):
    print('Status Kelulusan: Tidak LULUS')
    print('Sebab:')
    if(a<60):
        print('- Nilai Bahasa Indonesia kurang dari 60')
    if(b<=70):
        print('- Nilai Matematika kurang dari atau sama dengan 70')
    if(c<60):
        print('- Nilai IPA kurang dari 60')
else:
    print('Status Kelulusan: LULUS')
   

