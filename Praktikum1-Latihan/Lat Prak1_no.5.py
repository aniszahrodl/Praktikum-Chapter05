# input data
a=int(input('Masukkan kode karyawan	:'))
b=str(input('Masukkan nama karyawan	:'))
c=str(input('Masukkan golongan	:'))
d=int(input('Masukkan status (1: menikah, 2: blm)	:'))
if(d==1):
    e=int(input('Masukkan jumlah anak			:'))

#rumus gaji    
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

tunjIstriSuamiA= 10/100*gajiA
tunjIstriSuamiB= 10/100*gajiB
tunjIstriSuamiC= 10/100*gajiC
tunjIstriSuamiD= 10/100*gajiD

# rumus gaji ada anak
tunjAnakA= 5/100*gajiA*e
tunjAnakB= 5/100*gajiB*e
tunjAnakC= 5/100*gajiC*e
tunjAnakD= 5/100*gajiD*e

GajiKotorAnakA = gajiA + tunjIstriSuamiA + tunjAnakA
GajiKotorAnakB = gajiB + tunjIstriSuamiB + tunjAnakB
GajiKotorAnakC = gajiC + tunjIstriSuamiC + tunjAnakC
GajiKotorAnakD = gajiD + tunjIstriSuamiD + tunjAnakD

GajiBersihAnakA = GajiKotorAnakA - potongA
GajiBersihAnakB = GajiKotorAnakB - potongB
GajiBersihAnakC = GajiKotorAnakC - potongC
GajiBersihAnakD= GajiKotorAnakD - potongD



#output 
print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan		        :', b, '(Kode:', a,')')
print('Golongan			:', c)
print('Status Menikah			:', end= ' ')
if(d==1):
    print('Sudah Menikah')
    print('Jumlah Anak			:', e)
elif(d==2):
    print('Belum Menikah')
print('-----------------------------------------------------------')


if(d==1)and(c=='A'):
    print('Gaji Pokok			:  Rp', gajiA)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiA)
    print('Tunjangan anak			: Rp', tunjAnakA)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorAnakA)
    print('Potongan (', potA, '%)		: Rp', potongA)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihAnakA)
if(d==1)and(c=='B'):
    print('Gaji Pokok			:  Rp', gajiB)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiB)
    print('Tunjangan anak			: Rp', tunjAnakB)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorAnakB)
    print('Potongan (', potB, '%)		: Rp', potongB)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihAnakB)
if(d==1)and(c=='C'):
    print('Gaji Pokok			:  Rp', gajiC)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiC)
    print('Tunjangan anak			: Rp', tunjAnakC)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorAnakC)
    print('Potongan (', potC, '%)		: Rp', potongC)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihAnakC)
if(d==1)and(c=='D'):
    print('Gaji Pokok			:  Rp', gajiD)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiD)
    print('Tunjangan anak			: Rp', tunjAnakD)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorAnakD)
    print('Potongan (', potD, '%)		: Rp', potongD)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihAnakD)



#rumus gaji tanpa anak


GajiKotorA = gajiA + tunjIstriSuamiA 
GajiKotorB = gajiB + tunjIstriSuamiB 
GajiKotorC = gajiC + tunjIstriSuamiC 
GajiKotorD = gajiD + tunjIstriSuamiD 

GajiBersihA = GajiKotorA - potongA
GajiBersihB = GajiKotorB - potongB
GajiBersihC = GajiKotorC - potongC
GajiBersihD = GajiKotorA - potongD

#output tanpa anak
if(d==2)and(c=='A'):
    print('Gaji Pokok			:  Rp', gajiA)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiA)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorA)
    print('Potongan (', potA, '%)		: Rp', potongA)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihA)
if(d==2)and(c=='B'):
    print('Gaji Pokok			:  Rp', gajiB)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiB)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorB)
    print('Potongan (', potB, '%)		: Rp', potongB)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihB)
if(d==2)and(c=='C'):
    print('Gaji Pokok			:  Rp', gajiC)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiC)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorC)
    print('Potongan (', potC, '%)		: Rp', potongC)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihC)
if(d==2)and(c=='D'):
    print('Gaji Pokok			:  Rp', gajiD)
    print('Tunjangan Istri/Suami		:  Rp', tunjIstriSuamiD)
    print('----------------------------------------------------------- +')
    print('Gaji Kotor			: Rp', GajiKotorD)
    print('Potongan (', potD, '%)		: Rp', potongD)
    print('----------------------------------------------------------- -')
    print('Gaji Bersih			: Rp',GajiBersihD)


