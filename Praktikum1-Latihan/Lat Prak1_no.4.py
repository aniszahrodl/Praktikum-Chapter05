gajiA= 10000000	
gajiB= 8500000	
gajiC= 7000000	
gajiD= 5500000	

potA= 2.5
potB= 2.0
potC= 1.5
potD= 1.0

potongA= gajiA*potA/100
potongB= gajiB*potB/100
potongC= gajiA*potC/100
potongD= gajiA*potD/100

a=int(input('Masukkan kode karyawan	:'))
b=str(input('Masukkan nama karyawan	:'))
c=str(input('Masukkan golongan	:'))

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan		        :', b, '(Kode:', a,')')
print('Golongan			:', c)
print('-----------------------------------------------------------')

if(c=='A'):
    print('Gaji Pokok			: Rp', gajiA)
    print('Potongan (', potA, '%)		: Rp', potongA)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp', gajiA - potongA)
if(c=='B'):
    print('Gaji Pokok			: Rp', gajiB)
    print('Potongan (', potB, '%)		: Rp', potongB)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp', gajiB - potongB)
if(c=='C'):
    print('Gaji Pokok			: Rp', gajiC)
    print('Potongan (', potC, '%)		: Rp', potongC)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp', gajiC - potongC)
if(c=='D'):
    print('Gaji Pokok			: Rp', gajiD)
    print('Potongan (', potD, '%)		: Rp', potongD)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp', gajiD - potongD)

