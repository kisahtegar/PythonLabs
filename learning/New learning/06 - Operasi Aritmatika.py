print("Berikut  hasil dari Outputnya :")
print()
print("1) x ** y * (z + x) / y - y % z // x = ?")
print("2) x + y * z = ?")
print("3) (x + y) * z = ?")
print()

print("Silahkan masukkan angka !")
x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))
z = int(input("Masukan Nilai Z : "))

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)