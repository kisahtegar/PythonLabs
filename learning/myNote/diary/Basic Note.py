===========================================================
| Created by : Kisah Tegar                                |                                              
| My Diary ONLY                                           |
| Special Thanks : Petanikode                             |
| Date Created: Wednesday, ‎October ‎28, ‎2020, ‏‎10:06:43 AM  |
===========================================================
| My Dream to be a succsessful person :)                  |
=========================================================== 

===========================================================================================================================================
/// 1 /// 
/// Contoh Program ///
        ===================================================================================================================================
 
        // Contoh: Program bio data penduduk desa X

        // membuat variabel beserta isinya (nilainya)
           nama = "Hartono"
           alamat = 'Mataram'
           umur = 19
           tinggi = 170.5
           menikah = False

        // mencetak isi variabel
           print ("Nama : ", nama)
           print ("Alamat : ", alamat)
           print ("Umur : ", umur)
           print ("Tinggi : ", tinggi)
           if(menikah):
               print ("Status: menikah")
           else:
               print ("Status: belum menikah")
 
        ===================================================================================================================================
===========================================================================================================================================
/// 2 ///
/// Contoh Program ///
        ===================================================================================================================================

        // Pembagian
           a = 10
           b = 2
           c = float (a) / float (b)

           print (c)

        ===================================================================================================================================
===========================================================================================================================================
/// 3 ///
/// Contoh Program ///
        ===================================================================================================================================

        // Print
           nama = "Petanikode"
           print("Hello", nama)

        ===================================================================================================================================
===========================================================================================================================================
/// 4 ///
/// Contoh Program ///
        ===================================================================================================================================

        // Fitur formatting
           nama_mu = input("Nama kamu: ")
           nama_dia = input("Nama dia: ")

           print ("{} dengan {} sepertinya pasangan yang serasi :)". format(nama_mu, nama_dia))

        ===================================================================================================================================
===========================================================================================================================================
/// 5 ///
/// Operator Aritmatika ///
        ===================================================================================================================================

          ========================
          | Operator	   | Simbol |
          | Penjumlahan	|   +    |
          | Pengurangan	|   -    |
          | Perkalian	|   *    |
          | Pembagian	|   /    |
          | Sisa Bagi	|   %    |
          | Pemangkatan	|   **   |
          ========================

        // Ambil input untuk mengisi nilai
           a = int(input("Inputkan nilai a: "))
           b = int(input("Inputkan nilai b: "))

        // Menggunakan operator penjumlahan
           c = a + b
           print ("Hasil %d + %d = %d" % (a,b,c))

        // Operator Pengurangan
           c = a - b
           print ("Hasil %d - %d = %d" % (a,b,c))

        // Operator Perkalian
           c = a * b
           print ("Hasil %d x %d = %d" % (a,b,c))

        // Operator Pembagian
           c = a / b
           print ("Hasil %d : %d = %d" % (a,b,c))

        // Operator Sisa Bagi
           c = a % b
           print ("Hasil %d %% %d = %d" % (a,b,c))

        // Operator Pangkat
           c = a ** b
           print ("Hasil %d ^ %d = %d" % (a,b,c))

        ===================================================================================================================================

        // Contoh lainnya:
        // Operasi aritmatika
           a = int(input("Masukan Angka ke-1 : "))
           b = int(input("Masukan Angka ke-2 : "))

        // operasi tambah +
           hasil = a + b
           print(a,'+',b,'=',hasil)

        // operasi pengurangan -
           hasil = a - b
           print(a,'-',b,'=',hasil)

        // operasi perkalian *
           hasil = a * b
           print(a,'*',b,'=',hasil)

        // operasi pembagian /
           hasil = a / b
           print(a,'/',b,'=',hasil)

        // operasi eksponen (pangkat) **
           hasil = a ** b
           print(a,'**',b,'=',hasil)

        // operasi modulus %
           hasil = a % b
           print(a,'%',b,'=',hasil)

        // operasi floor division //
           hasil = a // b
           print(a,'//',b,'=',hasil)
  
      ===================================================================================================================================

        // Contoh program lainnya:

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

        // kurung akan mengambil langkah paling pertama
           hasil = (x + y) * z 
           print('(',x,'+',y,') *',z,'=',hasil)

        ===================================================================================================================================
===========================================================================================================================================
/// 6 ///
/// Operator Penugasan ///
        ===================================================================================================================================

          ======================== 
          | Operator	   | Simbol |
          ========================
          | Pengisian	|   =    |
          | Penjumlahan	|   +=   |
          | Pengurangan	|   -=   |
          | Perkalian	|   *=   |
          | Pembagian	|   /=   |
          | Sisa Bagi	|   %=   |
          | Pemangkatan	|   **=  |
          ======================== 
        // Contoh :
                a += 5
                a = a + 5

        ===================================================================================================================================
 
        // Ambil input untuk mengisi nilai
        // contoh operator penugasan untuk mengisi nilai
           a = int(input("Inputkan nilai a: "))
 
       
        // Coba kita jumlahkan nilai a dengan opertor penugasan
           print ("Nilai a = %d" % a)

        // contoh operator penugasan untuk menjumlahkan
           a += 5

        // Setelah nilai a ditambah 5, coba kita lihat isinya
           print ("Nilai setelah ditambah 5:")
           print ("a = %d" % a)
 
        ===================================================================================================================================
 
        // Operator Lainnya:

        // Ambil input untuk mengisi nilai
           a = int(input("Inputkan nilai a: "))

        // tambahkan dengan 2
           a += 2

        // kurangi 3
           a -= 3

        // kali 10
           a *= 10

        // bagi dengan 4
           a /= 4

        // pangkat 10
           a **= 10

        // Berapakah nilai a sekarang?
           print ("Nilai a adalah %d" % a)

        ===================================================================================================================================
===========================================================================================================================================
/// 7 ///
/// Operator Pembanding, komparasi ///
        ===================================================================================================================================

          ====================================
          | Operator	                 Simbol |
          ====================================
          | Lebih Besar	                >    |
          | Lebih Kecil	                <    |
          | Sama Dengan	                ==   |
          | Tidak Sama dengan	          !=   |
          | Lebih Besar Sama dengan	    >=   |
          | Lebih Kecil Sama dengan	    <=   |
          ====================================
        // Contoh:
                a = 9
                b = 5
                c = a < b
        
        // hasilnya salah, karena (a) lebih besar dari (b)
 
        ===================================================================================================================================
 
        // Contoh coding
           a = int(input("Inputkan nilai a: "))
           b = int(input("Inputkan nilai b: "))

        // apakah a sama dengan b?
           c = a == b
           print ("Apakah %d == %d: %r" % (a,b,c))

        // apakah a < b?
           c = a < b
           print ("Apakah %d < %d: %r" % (a,b,c))

        // apakah a > b?
           c = a > b
           print ("Apakah %d > %d: %r" % (a,b,c))

        // apakah a <= b?
           c = a <= b
           print ("Apakah %d <= %d: %r" % (a,b,c))

        // apakah a >= b?
           c = a >= b
           print ("Apakah %d >= %d: %r" % (a,b,c))

        // apakah a != b?
           c = a != b
           print ("Apakah %d != %d: %r" % (a,b,c))

        ===================================================================================================================================
        
        // Contoh lainnya: 
   
        // operasi komparasi //

        // setiap hasil dari operasi komparasi adalah boolean
        // >,<,>=,<=,==,!=,is,is not
           print()
           a = int(input("Masukan angka ke-1 : "))
           b = int(input("Masukan angka ke-2 : "))

        // lebih besar dari >
           print('\n========== lebih besar dari (>)')
           hasil = a > 3
           print(a,'>',3,'=',hasil)
           hasil = b > 3
           print(b,'>',3,'=',hasil)
           hasil = b > 2
           print(b,'>',2,'=',hasil)

        // kurang dari <
           print('\n========== kurang dari (<)')
           hasil = a < 3
           print(a,'<',3,'=',hasil)
           hasil = b < 3
           print(b,'<',3,'=',hasil)
           hasil = b < 2
           print(b,'<',2,'=',hasil)

        // lebih dari sama dengan >=
           print('\n========== lebih dari sama dengan(>=)')
           hasil = a >= 3
           print(a,'>=',3,'=',hasil)
           hasil = b >= 3
           print(b,'>=',3,'=',hasil)
           hasil = b >= 2
           print(b,'>=',2,'=',hasil)

        // kurang dari sama dengan <=
           print('\n======== kurang dari sama dengan(<=)')
           hasil = a <= 3
           print(a,'<=',3,'=',hasil)
           hasil = b <= 3
           print(b,'<=',3,'=',hasil)
           hasil = b <= 2
           print(b,'<=',2,'=',hasil)

        // sama dengan (==)
           print('\n======== sama dengan(==)')
           hasil = a == 4
           print(a,'==',4,'=',hasil)
           hasil = b == 4
           print(b,'==',4,'=',hasil)

        // tidak sama dengan (!=)
           print('\n======== sama dengan(!=)')
           hasil = a != 4
           print(a,'!=',4,'=',hasil)
           hasil = b != 4
           print(b,'!=',4,'=',hasil)

        ===================================================================================================================================

        // Contoh Komparasi  lainnya dengan is dan is not //

        // Contoh program :
        // is dan is not sebagai komparasi object identity
           print('\n======== object identity(is)')
           x = 5 # ini adalah assignment membuat object
           y = 5
           print('nilai x =',x,',id = ',hex(id(x)))
           print('nilai y =',y,',id = ',hex(id(y)))
           hasil = x is y
           print('x is y =',hasil)
           print()

           x = 5 # ini adalah assignment membuat object
           y = 6
           print('nilai x =',x,',id = ',hex(id(x)))
           print('nilai y =',y,',id = ',hex(id(y)))
           hasil = x is y
           print('x is y =',hasil)

           print('\n======== object identity(is not)')
           x = 5 # ini adalah assignment membuat object
           y = 5
           print('nilai x =',x,',id = ',hex(id(x)))
           print('nilai y =',y,',id = ',hex(id(y)))
           hasil = x is not y
           print('x is not y =',hasil)
           print()

           x = 5 # ini adalah assignment membuat object
           y = 6
           print('nilai x =',x,',id = ',hex(id(x)))
           print('nilai y =',y,',id = ',hex(id(y)))
           hasil = x is not y
           print('x is not y =',hasil)

        ===================================================================================================================================

        // Komparasi dan Logika //

        // membuat gabungan area rentang dari
        // Contoh :
        // ++++++3--------10+++++++
           inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

        // ++++++3-----------------
        // Memeriksa angka kurang dari 3
           isKurangDari = (inputUser < 3)
           print("Kurang dari 3 =", isKurangDari)

        // ---------------10++++++++
        // Memeriksa angka lebih dari 10
           isLebihDari = (inputUser > 10)
           print("Lebih dari 10 =", isLebihDari)

        // ++++++3--------10+++++++
           isCorrect = isKurangDari or isLebihDari
           print("angka yang anda masukan: ", isCorrect)

        ===================================================================================================================================
         
        // Contoh lainnya : 
        // -----3++++++++10--------
        // kasus irisan
           print("\n",10*"=","\n") # hanya pembatas :)
           inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

        // -----3++++++++++++++++++
        // lebih dari 3
           isLebihDari = inputUser > 3
           print("Lebih dari 3 = ",isLebihDari)

        // +++++++++++++++10-------
        // kurang dari 10
           isKurangDari = inputUser < 10
           print("Kurang dari 10 = ",isKurangDari)

        // -----3++++++++10--------
           isCorrect = isKurangDari and isLebihDari
           print("angka yang anda masukan: ", isCorrect)
        
        ===================================================================================================================================
===========================================================================================================================================
/// 8 ///
/// Operator Logika, boolean ///
        ===================================================================================================================================

          =====================================
          | Nama	           Simbol di Python |
          =====================================
          | Logika AND	           and        |
          | Logika OR	           or         |
          | Negasi/kebalikan       not        |
          =====================================

        ===================================================================================================================================

        // Contoh:

           a = True
           b = False

        // Logika AND
           c = a and b
           print ("%r and %r = %r" % (a,b,c))

        // Logika OR
           c = a or b
           print ("%r or %r = %r" % (a,b,c))

        // Logika Not
           c = not a
           print ("not %r  = %r" % (a,c))
  
        ===================================================================================================================================

        // Contoh Lainnya: 
        // operasi logika atau boolean

        // not, or, and, xor

        // not
           print('==== NOT ====')
           a = False
           c = not a
           print('data a =',a)
           print('-------------- NOT')
           print('data c =',c)

        // or (jika salah satu true, maka hasilnya adalah true)
           print('==== OR ====')
           a = False
           b = False
           c = a or b
           print(a,'OR',b,'=',c)
           a = False
           b = True
           c = a or b
           print(a,'OR',b,' =',c)
           a = True
           b = False
           c = a or b
           print(a,' OR',b,'=',c)
           a = True
           b = True
           c = a or b
           print(a,' OR',b,' =',c)

        // and (jika dua buah nilai true, maka hasil true)
           print('==== AND ====')
           a = False
           b = False
           c = a and b
           print(a,'AND',b,'=',c)
           a = False
           b = True
           c = a and b
           print(a,'AND',b,' =',c)
           a = True
           b = False
           c = a and b
           print(a,' AND',b,'=',c)
           a = True
           b = True
           c = a and b
           print(a,' AND',b,' =',c)

        // xor (akan true jika salah satu true, sisanya false)
           print('==== XOR ====')
           a = False
           b = False
           c = a ^ b
           print(a,'XOR',b,'=',c)
           a = False
           b = True
           c = a ^ b
           print(a,'XOR',b,' =',c)
           a = True
           b = False
           c = a ^ b
           print(a,' XOR',b,'=',c)
           a = True
           b = True
           c = a ^ b
           print(a,' XOR',b,' =',c)

        ===================================================================================================================================

        // Contoh program tinggal nginput aje :) :

        // OR (jika salah satu true, maka hasilnya adalah true)
        // AND (jika dua buah nilai true, maka hasil true)

           print('==== OR, AND ====')
           a = str(input("Nilai a [True/False] : "))
           b = str(input("Nilai b [True/False] : "))

           c = a or b
           d = a and b 

           print(a,'NOT',b,'=',c)
           print(a,'AND',b,'=',d)

        ===================================================================================================================================
===========================================================================================================================================
/// 9 ///
/// Operator Bitwise ///
        ===================================================================================================================================

          ============================
          | Nama	            Simbol |
          ============================
          | AND	              &    |   
          | OR	                 |    |
          | XOR	              ^    |
          | Negasi/kebalikan    ~    |
          | Left Shift	        <<   |
          | Right Shift	        >>   |
          ============================

        ===================================================================================================================================
 
        // Konsepnya memang hampir sama dengan opeartor Logika. Namun, 
        // Bitwise digunakan untuk biner.

        a = int(input("Masukan nilai a: "))
        b = int(input("Masukan nilai b: "))

        // Operasi AND
           c = a & b
           print ("a & b = %s" % c)

        // Operasi 
           c = a | b
           print ("a | b = %s" % c)

        // Operasi XOR
           c = a ^ b
           print ("a ^ b = %s" % c)

        // Operasi Not
           c = ~a
           print ("~a = %s" % c)

        // Operasi shift left (tukar posisi biner)
           c = a << b
           print ("a << b = %s" % c)

        // Operasi shift right (tukar posisi biner)
           c = a >> b 
           print ("a >> b = %s" % c)
       
        ===================================================================================================================================
===========================================================================================================================================
/// 10 ///
/// Contoh Program ///
        ===================================================================================================================================

        // Random String
           import random
           myString = 'kisah tegar putra abdi'

           print(myString[random.randrange(0, len(myString))])
        
        // tulisan yang diambil akan acak

        ===================================================================================================================================
===========================================================================================================================================
/// 11 ///
/// Operator Ternary ///
        ===================================================================================================================================
 
        // Operator ternary juga dikenal dengan operator kondisi, karena digunakan untuk membuat 
        // sebuah ekspresi kondisi seperti percabgan IF/ELSE.

           umur = int(input("Berapa umur kamu?"))
           aku = "bocah" if umur < 10 else "dewasa"

           print (aku)

        // Operasi Ternary dengan Tuple and List //

           jomblo = True
           status = "Menikah", "Single" [jomblo]

           print (status)
  
        ===================================================================================================================================
===========================================================================================================================================
/// 12 ///
/// if, elif, else. input ///
        ===================================================================================================================================

        // Contoh: if, elif, else. input

        // Use while True: will loop the program forever.
        // Use == to test for equality.
        // Use .lower() to make it easier to test for answers regardless of case.
        // if/elif/elif/.../else is the correct sequence for testing.

        ===================================================================================================================================

        // hanya 1 kali tidak looping tak terbatas
           def tanya():
               tanya = input("Apakah anda sudah menikah :")

               if tanya == 'yes':
                  print ("status : menikah")
               elif tanya == 'no':
                  print ("status : jomblo")
               else:
                  print ("huh?")
           tanya()

        ===================================================================================================================================

        // Looping tak terbatas
           while True:
               tanya = input("Apakah anda sudah menikah? [yes/no]:"). lower()

               if tanya == 'yes':
                  print ("status : menikah")
               elif tanya == 'no':
                  print ("status : jomblo")
               else:
                  print ("huh?")

        ===================================================================================================================================

        // program untuk mengecek bonus dan diskon

           total_belanja = int(input("Total belanja: Rp "))

        // jumlah yang harus dibayar adalah berapa total belanjaannya
        // tapi kalau dapat diskon akan berkurang
           bayar = total_belanja

        // jika dia belanja di atas 100rb maka berikan bonus dan diskon
           if total_belanja > 100000:
              print("Kamu mendapatkan bonus minuman dingin")
              print("dan diskon 5%")

        // hitung diskonnya
           diskon = total_belanja * 5/100 #5%
           bayar = total_belanja - diskon


        // cetak struk
           print("Total yang harus dibayar: Rp %s" % bayar)
           print("Terima kasih sudah berbelanja")
           print("Datang lagi yaa...")

        ===================================================================================================================================

        // Contoh input nilai grade
           nilai = int(input("Inputkan nilaimu: "))

           if nilai >= 90:
              grade = "A"
           elif nilai >= 80:
              grade = "B+"
           elif nilai >= 70:
              grade = "B"
           elif nilai >= 60:
              grade = "C+"
           elif nilai >= 50:
              grade = "C"
           elif nilai >= 40:
              grade = "D"
           else:
              grade = "E"

           print("Grade: %s" % grade)

        ===================================================================================================================================
        
        // Short Hand If ... Else //
        // If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

        // Contoh :
        // One line if else statement:
           a = 2
           b = 330

           print("A") if a > b else print("B")

        // Output :
           B

        // menyuruh print "A" jika a lebih besar dari b jika lain atau jika tidak print "B"
        // This technique is known as Ternary Operators, or Conditional Expressions.

        // You can also have multiple else statements on the same line:
        // Contoh :
        // One line if else statement, with 3 conditions:
           a = 330
           b = 330
           print("A") if a > b else print("=") if a == b else print("B")

        // Output :
           =
        // simplenya, contoh diatas menyuruh : print "A" jika a lebih besar dari b. jika lain, print "=" jika a sama dengan b. 
        // jika lain, print "B".
        
        #===================================================================================================================================
        
        //  And //
        //  The and keyword is a logical operator, and is used to combine conditional statements:

        // Contoh :
        // Test if a is greater than b, AND if c is greater than a:
           a = 200
           b = 33
           c = 500
           if a > b and c > a:
              print("Both conditions are True")

        // output :
           Both conditions are True
           
        #==================================================================================================================================
        
        // Or //
        // The or keyword is a logical operator, and is used to combine conditional statements:

        // Contoh :
        // Test if a is greater than b, OR if a is greater than c:
           a = 200
           b = 33
           c = 500
           if a > b or a > c:
              print("At least one of the conditions is True")
        
        // Output : 
           At least one of the conditions is True

        #==================================================================================================================================
        
        // Nested If //
        // You can have if statements inside if statements, this is called nested if statements.

        // Contoh :
           x = 41

           if x > 10:
              print("Above ten,")
              if x > 20:
                 print("and also above 20!")
              else:
                 print("but not above 20.")

        // Output :
           Above ten,
           and also above 20!

        #==================================================================================================================================
        
        // The pass Statement //
        // if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

        // Contoh :
           a = 33
           b = 200

           if b > a:
              pass

        // Output : 
           empty / Kosong

        // having an empty if statement like this, would raise an error without the pass statement
        
        ===================================================================================================================================
===========================================================================================================================================
/// 13 ///
/// Perulangan: for, while ///
        ===================================================================================================================================

        // Perulangan for //
        ulang = int(input("input:"))

        // Variabel i berfungsi untuk menampung indeks, dan fungsi range() berfungsi 
        // untuk membuat list dengan range dari 0-10. Fungsi str() berfungsi merubah 
        // tipe data ineger ke string.
           for i in range(ulang):
               print ("Perulangan ke-"+str(i))

        // Contoh dengan senerai (list):
           item = ['kopi', 'nasi', 'teh', 'jeruk']

           for isi in item:
               print (isi)

        ===================================================================================================================================
        
        // contoh perulangan // 

        // loop trough list //
        // contoh :
           thislist = ["apple", "banana", "cherry"]
           for x in thislist:
              print(x)
        
        // output : 
           apple 
           banana
           cherry
         
        // dia melakukan perulangan melalu list ingat list  

        #===================================================================================================================================
        
        // loop trough the index numbers // 
        // contoh : 
           thislist = ["apple", "banana", "cherry"]
           for i in range(len(thislist)):
              print(thislist[i])

        // output : 
           apple
           banana
           cherry

        // dia melakukan perulangan melalui index number pada list contoh diatas
        // lakukanlah pengujian agar bisa membedakan antara trough list dan trough index number   

        #===================================================================================================================================
        
        // loop menggunakan while //
        // Use the len() function to determine the length of the list, 
        // then start at 0 and loop your way through the list items by refering to their indexes.
        // Remember to increase the index by 1 after each iteration.

        // contoh : 
        // Print all items, using a while loop to go through all the index numbers
           thislist = ["apple", "banana", "cherry"]
           i = 0
           while i < len(thislist):
              print(thislist[i])
              i = i + 1 

        // output : 
           apple
           banana
           cherry

        // simplenya, pada kasus diatas dia melakukan perulangan berdasarkan index number dari list tersebut
        // apabila i lebih kecil dari index thislist, dia akan melakukan looping sampai nilainya sama
        // setiap loop akan ditambah 1 / i = i + 1. jika sudah tidak ada lagi akan berhenti loop
        
        #===================================================================================================================================
        
        // The break Statement //
        // With the break statement we can stop the loop even if the while condition is true:
        
        // Contoh:
        // Exit the loop when i is 3:
           i = 1
           while i < 6:
              print(i)
              if i == 3:
                 break
              i += 1

        // Output : 
           1
           2
           3

        // simplenya jika perulangannya sudah sampe 3, hentikan dan menjadikan output diatas.
        
        #===================================================================================================================================
        
        // The continue Statement //
        // With the continue statement we can stop the current iteration, and continue with the next:
        
        // Contoh :
        // Continue to the next iteration if i is 3:
           i = 0
           while i < 6:
              i += 1
              if i == 3:
                 continue
              print(i)

        // Output : 
           1
           2
           4
           5
           6

        // kenapa 3 tidak masuk ke output?. karena jika i sama dengan 3 dia akan lanjut looping lagi tanpa masuk ke print(i).
        
        #===================================================================================================================================
        
        // The else Statement //
        // With the else statement we can run a block of code once when the condition no longer is true:

        // Contoh :
        // Print a message once the condition is false:
           i = 1
           while i < 6:
              print(i)
              i += 1
           else:
              print("i is no longer less than 6")

        // Output :
           1
           2
           3
           4
           5
           i is no longer less than 6
        
        // jika perulangan sudah selesai akan memprint else: atau jika i sudah sama dengan 6 akan di print else: nya.

        ===================================================================================================================================
        
        // Looping using list comprehensive //
        // List Comprehensive offers the shortest syntax for looping through lists:
        // Print all items, using a while loop to go through all the index numbers
        
        // contoh:
           thislist = ["apple", "banana", "cherry"]
           [print(x) for x in thislist] 
           
        // output : 
           apple
           banana
           cherry
        
        // loop ini adalah yang paling pendek untuk melooping dari list
        // dia mengprint semua item menggunakan while loop untuk menelusuri semua nomor index 
        
        // or 

        // Contoh lain Comprehensive //
        // this my favorit list lebih singkat dan cepat
        // contoh:
           thislist = {
              "apple": "wadaw", 
              "banana": "idiw", 
              "cherry": 2003
           }

           [print(x, thislist[x]) for x in thislist]

        // output:
           apple wadaw
           banana idiw
           cherry 2003

        // singkat jelas padat :)

        ===================================================================================================================================

        // list comprehension //
        // List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
        // Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
        // Without list comprehension you will have to write a for statement with a conditional test inside:

        // contoh :
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
           newlist = []

           for x in fruits:
           if "a" in x:
               newlist.append(x)

           print (newlist)

        // output :
           ['apple', 'banana', 'mango']

        // simplenya kita ingin mengisi newlist dengan list fruits. Kita meminta jika variable a ada di list fruits atau kalimatnya ada huruf a
        // maka akan dimasukkan ke newlist sebagai contoh: huruf a ada di kalimat apple, maka apple akan ditambahkan ke newlist
        // kalimat cherry tidak ada huruf a, maka cherry tidak ditambahkan di newlist.
        // kurang lebih seperti itu menurut ku.

        // Dan berikut contoh code comprehension yang sangat singkat
        // contoh :
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
           newlist = [x for x in fruits if "a" in x]

           print (newlist)

        // output :
           ['apple', 'banana', 'mango']
        
        // dengan menggunakan code ini comprehension, akan sangat singkat dan cepat
        // dan kita hanya menulis satu line saja tanpa harus panjang :)
        
        ===================================================================================================================================
        
        // The syntax //
        // ini contoh syntaxnya : 
           newlist = [expression for item in iterable if condition == True]

        // The return value is a new list, leaving the old list unchanged.
        
        ===================================================================================================================================
        
        // condition //
        // The condition is like a filter that accepts only the items that valuates to True.
        
        // contoh :
        // Only accept items that are not "apple":
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

           newlist = [x for x in fruits if x != "apple"]

           print (newlist)
        
        // output :
           ['banana', 'cherry', 'kiwi', 'mango']

        // Kondisi jika x != "apple" akan mengembalikan True untuk semua elemen selain "apple", 
        // membuat daftar baru berisi semua buah kecuali "apple".
        // kondisi jika x == "apple" akan mengembalikan True untuk elemen "apple"
        // maka akan mengprint apple saja.

        // kondisinya opsional dan dapat dihilangkan
        // contoh :
        // tanpa statement if
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

           newlist = [x for x in fruits]

           print (newlist)

        // ini adalah contoh tanpa menggunakan if
        
        ===================================================================================================================================
        
        // iterable //
        // The iterable can be any iterable object, like a list, tuple, set etc.
        // Contoh : 
        // You can use the range() function to create an iterable:
           newlist = [x for x in range(10)]

           print (newlist)
        
        // output :
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        // simplenya x punya jarak sampe 10 nomor index lalu newlist di print dan menghasilkan output tersebut
        // sekarang kita akan buat contoh yang sama tapi beda kondisi menggunakan if
        // contoh: 
           newlist = [x for x in range(10) if x < 5]

           print (newlist)

        // output : 
           [0, 1, 2, 3, 4]
        
        // simplenya sama seperti contoh kasus sebelumnya, tapi dia menggunakan if
        // jika x < 5 maka dia akan mengprint 5 index saja. dan menghasilkan output [0, 1, 2, 3, 4]

        ===================================================================================================================================

        // Expresion //
        // The expression is the current item in the iteration, but it is also the outcome, 
        // which you can manipulate before it ends up like a list item in the new list:
        // contoh:
        // Set the values in the new list to upper case:
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

           newlist = [x.upper() for x in fruits]

           print (newlist)

        // output :
           ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

        // simplenya upper() merubah list fruits menjadi huruf besar semua   
        
        // You can set the outcome to whatever you like:
        // contoh :
        // Set all values in the newlist to 'hello':
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

           newlist = ['fruits' for x in fruits]

           print (newlist)
        
        // output :       
           ['hello', 'hello', 'hello', 'hello', 'hello']
        
        // simplenya, newlist memprint 'hello' sebanyak 5 kali sesuai dengan list fruits
        // mengapa output 'hello' karena ibaratnya index number fruits atau list fruits digantikan
        // namanya jadi'fruits' atau ibaratnya si 'fruits' ini untuk x yang ada di list fruits
        // ribetyak logika kuu :/
        
        // The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
        // contoh:
        // Return "orange" instead of "banana":
           fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

           newlist = [x if x != "banana" else "orange" for x in fruits]

           print (newlist)

        // output :
           ['apple', 'orange', 'cherry', 'kiwi', 'mango']

        // ibaratnya, jika list tidak sama dengan banana abaikan, jika list sama dengan banana akan diganti dengan
        // orange. seperti itu simplenya.

        ===================================================================================================================================
        
        // Sort Lists //
        // List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
        // Contoh ke-1 : 
        // Sort the list alphabetically:
           thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "apple"]

           thislist.sort()

           print(thislist)

        // output : 
           ['apple', 'banana', 'kiwi', 'mango', 'orange', 'pineapple']

        // simplenya, dia menyortir atau mengurutkan thislist yang tadinya kalimatnya tidak berurutan,
        // menjadi berurutan sesuai alphabet a,b,c-z.
        
        // Contoh ke-2 :
        // Sort the list numerically:
           thislist = [100, 50, 65, 82, 23]

           thislist.sort()

           print(thislist)

        // output :
           [23, 50, 65, 82, 100]

        // sama seperti kasus sebelumnya, hanya saja bedanya kasus ini menggunakan angka,
        // dia akan mengurutkan angka dari yang terkecil sampat terbesar.
        
        ===================================================================================================================================
        
        // Sort Descending //
        // To sort descending, use the keyword argument reverse = True :
        
        // Contoh ke-1 :
        // Sort the list descending:
           thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

           thislist.sort(reverse = True)

           print(thislist)

        // output :
           ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

        // Descending = menurun. simplenya dia akan menyortir dari atas ke bawah karena,
        // reverse = True yang artinya kebalikan.
       
        // Contoh ke-2 :
        // Sort the list descending:
           thislist = [23, 50, 65, 82, 100]

           thislist.sort(reverse = True)

           print(thislist)
        
        // output:
           [100, 82, 65, 50, 23]

        // sama seperti study kasus sebelumnya hanya saja ini contoh dengan angka 
        
        ===================================================================================================================================
        
        // Customize sort function //
        // You can also customize you own function by using the keyword argument key = function.
        // The function will return a number that will be used to sort the list (the lowest number first):
        // Contoh : 
           def myfunc(n):
            return abs(n-50)

           thislist = [100, 50, 65, 82, 23]

           thislist.sort(key = myfunc)

           print(thislist)

        // output:
           [50, 65, 23, 82, 100]
        
        // simplenya, abs(n-50) / untuk kasus ini dia menyortir seberapa dekat angka 50 dari semua angka 
        // yang ada di thislist. angka 50 dekat dengan angka 50 yang di list, angka 50 dekat dengan angka 65,
        // angka 50 dekat dengan angka 23, angka 50 dekat dengan angka 82 dan seterusnya....
        // maksudnya dekat adalah jarak hitung dari angka 50 ke angka 62 itu dekat dibandingkan jarak hitung 
        // dari angka 50 ke angka 23.
        // Paham :)

        ===================================================================================================================================

        // Case Insensitive Sort //
        // By default the sort() method is case sensitive, resulting in all capital letters being sorted after lower case letters:
        // Contoh : 
        // Case sensitive sorting can give an unexpected result:
           thislist = ["banana", "Orange", "Kiwi", "cherry"]

           thislist.sort()

           print(thislist)

        // Output : 
           ['Kiwi', 'Orange', 'banana', 'cherry']

        // Sama seperti kasus sebelum-sebelumnya, kalau kita perhatikan thislist memiliki beberapa kalimat yang menggunakan
        // Huruf Kapital atau Besar. simplenya sort() menyortir thislist dari huruf Kapital atau huruf Terbesar dahulu.
        // Simplekan :)
        
        // Jika ingin mengprint dari huruf terkecil gunakan ini:
        // Contoh :
        // Perform a case-insensitive sort of the list:
           thislist = ["banana", "Orange", "Kiwi", "cherry"]

           thislist.sort(key=str.lower)

           print (thislist) 

        // output :
           ['banana', 'cherry', 'Kiwi', 'Orange']
        
        // Simplenya dia akan mengprint dari kalimat dengan huruf depan kecil terlebih dahulu
        // Lalu jika sudah dia akan mengprint dari huruf terbesar secara urut.

        ===================================================================================================================================
        
        // Reverse Order //
        // What if you want to reverse the order of a list, regardless of the alphabet?
        // The reverse() method reverses the current sorting order of the elements.
        
        // Contoh :
        // Reverse the order of the list items:
           thislist = ["banana", "Orange", "Kiwi", "cherry"]

           thislist.reverse()

           print(thislist) 
        
        // output :
           ['cherry', 'Kiwi', 'Orange', 'banana']
        
        // Simplenya, dia akan mengprint secara terbalik, dimulai dari akhir dari thislist sampai ke awal thislist.
        // output akan terprint secara terbalik urutannya.

        ===================================================================================================================================
        
        // Copy a List //
        // You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and 
        // changes made in list1 will automatically also be made in list2.
        // There are ways to make a copy, one way is to use the built-in List method copy().
        
        // Contoh :
        // Make a copy of a list with the copy() method:
           thislist = ["apple", "banana", "cherry"]
           mylist = thislist.copy()
           print(mylist) 

        // Output :
           ['apple', 'banana', 'cherry']

        // Another way to make a copy is to use the built-in method list().
        // Contoh : 
        // Make a copy of a list with the list() method:
           thislist = ["apple", "banana", "cherry"]
           mylist = list(thislist)
           print(mylist)

        // Output :
           ['apple', 'banana', 'cherry']
        
        // Dari kedua kasus tersebut sama saja, simplenya mylist akan mengcopy semua yang ada di thislist

        ===================================================================================================================================
        
        // Join List // 

        // Join Two Lists //
        // There are several ways to join, or concatenate, two or more lists in Python.
        // One of the easiest ways are by using the + operator.
        // Contoh : 
        // Join two list:
           list1 = ["a", "b", "c"]
           list2 = [1, 2, 3]

           list3 = list1 + list2
           print(list3) 

        // output: 
           ['a', 'b', 'c', 1, 2, 3]
        
        // Another way to join two lists are by appending all the items from list2 into list1, one by one:
        // Contoh :
        // Append list2 into list1:
           list1 = ["a", "b" , "c"]
           list2 = [1, 2, 3]

           for x in list2:
           list1.append(x)

           print(list1)
 
        // output: 
           ['a', 'b', 'c', 1, 2, 3]

        // Or you can use the extend() method, which purpose is to add elements from one list to another list:
        // Contoh : 
        // Use the extend() method to add list2 at the end of list1:
           list1 = ["a", "b" , "c"]
           list2 = [1, 2, 3]

           list1.extend(list2)
           print(list1)
         
        // output: 
           ['a', 'b', 'c', 1, 2, 3]

        // simplenya, dari semua study kasus diatas list1 akan bergabung dengan list2
        
        ===================================================================================================================================
        
        // list methods //

            Method	Description
            append()	Adds an element at the end of the list
            clear()	Removes all the elements from the list
            copy()	Returns a copy of the list
            count()	Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()	Removes the element at the specified position
            remove()	Removes the item with the specified value
            reverse()	Reverses the order of the list
            sort()	Sorts the list

        ===================================================================================================================================

        // Perulangan while //
        // looping bisa juga menjadi tidak terbatas
           jawab = 'ya'
           hitung = 0

           while(True):
               hitung += 1
               jawab = input("Ulang lagi tidak? ")
               if jawab == 'tidak':
                   break

           print ("Total perulagan: " + str(hitung))

        ===================================================================================================================================

        // program.me

        // jika digabungkan dengan else untuk menandai ketika salah mengetik
        // proses perhitungan dimulai dari index 0
           hitung = 0
        
           while(True):
               hitung += 1
               jawab = input("Ulang lagi tidak? ")
               if jawab == 'ya':
                   print("Oke")
               elif jawab == 'tidak':
                   break
               else:
                   print("input salah hanya ada jawaban [ya/tidak]")

           print ("Total perulagan: " + str(hitung))

        ===================================================================================================================================
        
        // Nested Loops //
        // A nested loop is a loop inside a loop.

        // The "inner loop" will be executed one time for each iteration of the "outer loop":

        // Contoh :
        // Print each adjective for every fruit:
           adj = ["red", "big", "tasty"]
           fruits = ["apple", "banana", "cherry"]

           for x in adj:
             for y in fruits:
               print(x, y)
        
        // Output :
           red apple
           red banana
           red cherry
           big apple
           big banana
           big cherry
           tasty apple
           tasty banana
           tasty cherry
        
        ===================================================================================================================================
===========================================================================================================================================
/// 14 ///
/// Struktur Data List ///
        ===================================================================================================================================

        // Contoh list
           warna = [] # list kosong.
           warna = ['merah'] # list berjumlah 1.
           warna = ['merah', 'kuning', 'hijau'] # list berjumlah 3 dan bisa ditambah seterusnya.

        // list dapat diisi dengan tipe data apa saja, string, integer, float, double, boolean, object, dan sebagainya.
        // dan bisa mencampur isinya.

           meja = ["buku", 21, True, 34.12]
        
        // Ada empat jenis tipe data pada list meja:
        // 1) "buku" adalah tipe data string;
        // 2) 21 adalah tipe data integer;
        // 3) True adalah tipe data boolean;
        // 4) dan 34.12 adalah tipe data float

        // Kita punya list nama-nama buah
           buah = ["apel", "anggur", "mangga", "jeruk"]

        // Misanya kita ingin mengambil mangga
        // Maka indeknya adalah 2
           print (buah[2])
        
        // Output : Mangga, mengapa bukan anggur?
        // karena indeks selalu diawali dari 0. indeks dari apel adalah 0
  
        ===================================================================================================================================
  
        // Latihan Membuat Program dengan List
        // 1) Buat sebuah list untuk menyimpan kenalanmu
        // 2) Isi list sebanyak 5
        // 3) Tampilkan isi list indeks nomer 3
        // 4) Tampilkan semua teman dengan perulangan
        // 5) Tampilkan panjang list


        // Buat list untuk menampung nama-nama teman
           my_friends = ["Aldio", "Dy", "Agung", "Adi", "Gigih"]

        // Tampilkan isi list my_friends dengan nomer indeks 3
           print ("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3]))

        // Tampilkan semua daftar teman
           print ("Semua teman: ada {} orang".format(len(my_friends)))
           for friend in my_friends:
               print (friend)
        
        // kita menggunakan fungsi len() untuk mengambil panjang list.
  
        ===================================================================================================================================
  
        // Mengganti Nilai List
        // Contoh:
        
        // list mula-mula
           buah = ["jeruk", "apel", "mangga", "duren"]
        
        // mengubah nilai index ke-2
           buah[2] = "kelapa"
        
        // Maka "mangga" akan diganti dengan "kelapa".
           ["jeruk", "apel", "kelapa", "duren"]
  
        ===================================================================================================================================
  
        // Menambahkan Item List
        // 1) prepend(item) menambahkan item dari depan;
        // 2) append(item) menambahkan item dari belakang.
        // 3) insert(index, item) menambahkan item dari indeks tertentu
        
        // Contoh :
        // 1. prepend //
        
        // list mula-mula
           buah = ["jeruk", "apel", "mangga", "duren"]
        
        // Tambahkan anggur
           buah.prepend("anggur")
        
        // Hasilnya "anggur" akan ditambahkan setelah item terakhir.
           ["anggur","jeruk", "apel", "mangga", "duren"]

        ===================================================================================================================================

        // 2. append //

        // list mula-mula
           buah = ["jeruk", "apel", "mangga", "duren"]
        
        // Tambahkan manggis
           buah.append("manggis")
        
        // Hasilnya "manggis" akan ditambahkan setelah item terakhir.
           ["jeruk", "apel", "mangga", "duren", "manggis"]

        ===================================================================================================================================

        // 3. insert //

        // list mula-mula:
           buah = ["jeruk", "apel", "mangga", "duren"]
        
        // Tambahkan manggis
           buah.insert(2, "duren")
        
        // Hasilnya "manggis" akan ditambahkan setelah item terakhir.
           ["jeruk", "apel", "duren", "mangga", "duren"]

        ===================================================================================================================================

        // Membuat Program dengan List //

        // Membuat list kosong untuk menampung hobi
           hobi = []
           stop = False
           i = 0

        // Mengisi hobi
           while(not stop):
           hobi_baru = input("Inputkan hobi yang ke-{}: ".format(i))
           hobi.append(hobi_baru)

        // Increment i
           i += 1
        
           tanya = input("Mau isi lagi? (y/t): ")
           if(tanya == "y"):
                stop = False
           elif(tanya == "t"): 
                stop = True
           else:
                print ("=" * 30) # mengeprint = sebanyak 10
                print("Kamu salah menginput data !")
                print("Perulangan terpaksa dihentikan !")
                print ("=" * 30) # mengeprint = sebanyak 10
                stop = True


        // Cetak Semua Hobi:
           print ("=" * 30) # mengeprint = sebanyak 10
           print ("Kamu memiliki {} hobi".format(len(hobi)))
           for hb in hobi:
                print ("- {}".format(hb))
           print ("=" * 30)

        ===================================================================================================================================

        // Menghapus Item di List //

        // Untuk menghapus salah satu isi dari List, kita bisa menggunakan perintah del.
        // Membuat List
           todo_list = [
               "Balajar Python",
               "Belajar Django",
               "Belajar MongoDB",
               "Belajar Sulap",
               "Belajar Flask"
           ]

        // Misalkan kita ingin menghapus "Belajar Sulap"
        // yang berada di indeks ke-3
           del todo_list[3]

           print (todo_list)

        // Hasilnya, "Belajar Sulap" akan dihapus:
           ['Balajar Python', 'Belajar Django', 'Belajar MongoDB', 'Belajar Flask']

        // Selain menggunakan perintah del, kita juga bisa menggunakan method remove() dengan paramter item yang akan dihapus.
        // mula-mula kita punya list
           a = ["a", "b", "c", "d"]
        
        // kemudian kita hapus b
           a.remove("b")

           print (a)

        // hasilnya
           ["a", "c", "d"]

        ===================================================================================================================================

        // menghapus menggunakan pop() //
        // contoh : 
           thislist = ["apple", "banana", "cherry"]
           thislist.pop(1)
           print(thislist)
        
        // output :
           ['apple', 'cherry'] 

        // pop() menghapus sesuai indeks yang diinputkan   

        ===================================================================================================================================
        
        // menghapus menggunakan del //
        // contoh :
           thislist = ["apple", "banana", "cherry"]
           del thislist[0]
           print(thislist)
        
        // output : 
           ['banana', 'cherry'] 
        
        // del juga bisa menghapus seperti ini
        // contoh :
           thislist = ["apple", "banana", "cherry"]
           del thislist
           print(thislist)

        // output : 
           error

        // akan terjadi error karena del berhasil menghapus thislist yang artinya print tidak bisa mengprint thislist      
          
        ===================================================================================================================================
        
        // Menggunakan clear() //
        // contoh : 
           thislist = ["apple", "banana", "cherry"]
           thislist.clear()
           print(thislist)

        // output :
           []

        // dia akan menghapus list di dalemnya saja dan list menjadi kosong    

        ===================================================================================================================================

        /// Memotong List ///

        // Kita punya list warna
           warna = ["merah", "hijau", "kuning", "biru", "pink", "ungu"]

        // Kita potong dari indeks ke-1 sampai ke-5
           print (warna[1:5])

        // Hasilnya:
           ['hijau', 'kuning', 'biru', 'pink']
 
        ===================================================================================================================================
        
        /// Operasi List ///

        // Penggabungan (+)
        // Perkalian (*)

        // Contoh:
        // Beberapa list lagu
           list_lagu = [
                   "No Women, No Cry",
                   "Dear God"
           ]

        // playlist lagu favorit
           playlist_favorit = [
                   "Break Out",
                   "Now Loading!!!"
           ]

        // Mari kita gabungkan keduanya
           semua_lagu = list_lagu + playlist_favorit

           print (semua_lagu)

        // Hasilnya:
           ['No Women, No Cry', 'Dear God', 'Break Out', 'Now Loading!!!']
 
        ===================================================================================================================================

        // Sedangkan untuk operasi perkalian hanya dapat dilakukan dengan bilangan //

        // Contoh:
        // playlist lagu favorit:
           playlist_favorit = [
                   "Break Out",
                   "Now Loading!!!"
           ]

        // ulangi sebanyak 5x :
           ulangi = 5

           now_playing = playlist_favorit * ulangi

           print (now_playing)

        // Hasilnya:
           ['Break Out', 'Now Loading!!!', 'Break Out', 'Now Loading!!!', 'Break Out', 'Now Loading!!!', 'Break Out', 'Now Loading!!!', 'Break Out', 'Now Loading!!!']
 
        ===================================================================================================================================

        // List Multi  //

        // Contoh:
        // List minuman dengan 2 dimensi:
           list_minuman = [
               ["Kopi", "Susu", "Teh"],
               ["Jus Apel", "Jus Melon", "Jus Jeruk"],
               ["Es Kopi", "Es Campur", "Es Teler"]
           ]

        // Cara mengakses list multidimensi
        // misalkan kita ingin mengambil "es kopi"
           print (list_minuman[2][0])

        // Angka dua 2 pada kode di atas, menujukan indeks list yang akan kita akses. 
        // Kemudian setelah dapat list-nya baru kita ambil isinya.
        // Hasil outputnya:
           "Es Kopi"

        // Bagaimana kalau kita ingin menampilkan semua isi dalam list multi dimensi?
        // Tinggal gunakan perulangan bersarang.
        // List minuman dengan 2 dimensi
           list_minuman = [
               ["Kopi", "Susu", "Teh"],
               ["Jus Apel", "Jus Melon", "Jus Jeruk"],
               ["Es Kopi", "Es Campur", "Es Teler"]
           ]

           for menu in list_minuman:
                   for minuman in menu:
                           print (minuman)

        // Hasilnya :
           1. Kopi
           2. Susu
           3. Teh
           4. Jus Apel
           5. Jus Melon
           6. Jus Jeruk
           7. Es Kopi
           8. Es Campur
           9. Es Teler

        // jika hanya menggunakan 1 penggulangan atau hanya menggunakan
           for menu in list_minuman:
                   print(menu)

        // Hasilnya :
           ["Kopi", "Susu", "Teh"],
           ["Jus Apel", "Jus Melon", "Jus Jeruk"],
           ["Es Kopi", "Es Campur", "Es Teler"]

        ===================================================================================================================================
        
        // Contoh List atau range //

        // mengprint semua list dari urutan apple-orange
           thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
           print(thislist[:4])
        
        // mengprint semua list dari urutan cherry-mango
           thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
           print(thislist[2:])

        // mengprint semua list dari urutan orange-melon
           thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
           print(thislist[-4:-1])

        // menggunakan insert hasilnya : ['apple', 'banana', 'watermelon', 'cherry']
           thislist = ["apple", "banana", "cherry"]
           thislist.insert(2, "watermelon")
           print(thislist)

        // bedanys manggunakan append dan extend pada contoh kasus dibawah ini
        // contoh1: output: ['apple', 'banana', 'cherry', ['mango', 'pineapple', 'papaya']]
           thislist = ["apple", "banana", "cherry"]
           tropical = ["mango", "pineapple", "papaya"]

           thislist.append(tropical)

           print(thislist)

        // contoh2: output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
           thislist = ["apple", "banana", "cherry"]
           tropical = ["mango", "pineapple", "papaya"]

           thislist.extend(tropical)

           print(thislist)

        // menambahkan elements list ke tuple / jadi: ['apple', 'banana', 'cherry', 'kiwi', 'orange']
           thislist = ["apple", "banana", "cherry"]
           thistuple = ("kiwi", "orange")

           thislist.extend(thistuple)

           print(thislist) 

        // menambahkan elements list ke dict / jadi: {'apple', 'papaya', 'cherry', 'mango', 'banana', 'pineapple'}
           thislist = {"apple", "banana", "cherry"}
           tropical = ["mango", "pineapple", "papaya"]

           thislist.update(tropical)

           print(thislist)
   

        ===================================================================================================================================
===========================================================================================================================================
/// 15 ///
/// Tuple ///
        ===================================================================================================================================

        // 1. Membuat Tuple di Python //

        // Tuple biasanya dibuat dengan tanda kurung seperti ini:
           t = (1234, 4321, 'Hello')

        // atau bisa juga tanpa tanda kurung:
           t = 1234, 432, 'World!'
        
        // Kedua-duanya valid.

        // Apabila kita ingin membuat sebuah tuple tanpa isi, kita bisa menuliskannya seperti ini

        ===================================================================================================================================

        // 2. Membuat Tuple Kosong dan Singleton //

        // Membuat Tuple kosong
           kosong = ()

        // Lalu untuk membuat Tuple yang hanya berisi satu (singleton), maka kita harus manambahkan tanda koma di belakangnnya.
        // Contoh:

        // membuat tuple
           satu = ('Isinya',)
           siji = "isinya siji",
        
        // Kenapa harus ditambahkan koma?
        // Karena kalau tidak ditambahkan koma, akan dianggap sebagai string.
           satu = ('isinya') # <-- ini string
           siji = "isinya satu" # <-- ini juga string

        ===================================================================================================================================

        // 3. Mengakses Nilai Tuple //

        // membuat tuple
           nama = ('petani', 'kode', 'linux')

        // mengakses nilai tuple
           print(nama[1])
        
        // Maka hasilnya:
           >>> nama = ('kisah', 'tegar', 'putra')
           >>> print (nama[0])
           kisah
           >>> print (nama[1])
           tegar
           >>> print (nama[2])
        
        // Jika diubah nilainya, maka akan terjadi error:
           >>> nama[0] = 'abdi'
           Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
           TypeError: 'tuple' object does not support item assignment
        
        // Mengapa bisa error? karena tuple bersifat immutable

        ===================================================================================================================================

        // 4. Memotong Tuple //

        // Sama seperti list, di Tuple juga kita bisa melakukan slicing. 
        // Contoh:
        // mula-mula kita punya tuple seperti ini
           web = (123, 'Petani Kode', 'https://www.petanikode.com')

        // lalu kita ingin potong agar ditampilkan
        // dari indeks nomer 1 sampai 2        
           print(web[1:2])

        // Maka hasilnya:
           ('petani kode',)

        ===================================================================================================================================

        // 5. Mengambil Panjang Tuple //
        
        // Untuk mengambil panjang atau jumlah item di dalam Tuple, kita bisa menggunakan fungsi len().
        // Contoh:
        // Membuat Tuple
           hari = ('senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu' )
           print (" Jumlah hari : %d" % len(hari))

        ===================================================================================================================================

        // 6. Tuple Nested //

        // Tuple juga bisa nested, artinya Tuple bisa diisi dengan Tuple.
        // Contoh:

           tuple1 = "aku", "cinta", "kamu"
           tuple2 = "selama", 3, "tahun"
           tuple3 = (tuple1, tuple2) # <- nested tuple
        
        // tuple3 akan berisi nilai dari tuple1 dan tuple2.
        // Hasil:
        
           >>> tuple1 = "aku", "cinta", "kamu"
           >>> tuple2 = "selama", 3, "tahun"
           >>> tuple3 = (tuple1, tuple2)
           >>> tuple3
           (('aku', 'cinta', 'kamu'), ('selama', 3, 'tahun')) 

        // Tuple juga bisa diisi dengan objek apapun seperti list, dictionary, object, dan lain-lain.
        // Contoh:
        
           t = ([1,2,3], {'nama': 'Petanikode', 'rank': 123}, True)
        
        // Tuple t berisi list, dictionary, dan nilai boolean.

        ===================================================================================================================================

        // 7. Sequence Unpacking //

        // Proses pembuatan Tuble bisa kita sebut sebagai packing, sementara untuk mengambil (ekstrak) seluruh isinya disebut unpacking.
        
        // Contoh:
        // mula-mula kita buat tuple seperti ini :
           web = 123, "Petani Kode", "https://www.petanikode.com"

        // lalu di-unpacking
           id_web, nama, url = web

        // maka sekarang tiga variabel tersebut akan bernilai
        // sesuai yang ada di dalam tuple
        // mari kita cetak:
           print(id_web)
           print(nama)
           print(url)
        
        // Hasilnya:
           >>> web = 123, "Petani Kode", "https://www.petanikode.com"
           >>> id_web, nama, url = web # lakukan secara urut sesuai yang anda inginkan
           >>> print(id_web)
           123
           >>> print(nama)
           Petani Kode
           >>> print(url)
           https://www.petanikode.com

        // Dengan melakukan upacking, isi tuple akan di-copy ke variabel. Lalu dengan variabel kita bisa melakukan apapun, 
        // seperti mengubah isinya. Karena variabel bersifat mutable.

        ===================================================================================================================================
        
        // update tuple //

        // Tuples are unchangeable, meaing that you cannot change, add, or remove items once the tuple is created.
        // But there are some workarounds.

        // Change Tuple Values //
        // Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
        // But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
        // Contoh : 
        // Convert the tuple into a list to be able to change it:
           x = ("apple", "banana", "cherry")
           y = list(x)
           y[1] = "kiwi"
           x = tuple(y)

           print(x)

        // output : 
           ("apple", "kiwi", "cherry")

        // y mengcopy list x lalu mengubah banana dengan kiwi, dan x mengcopy tuple y lalu diprint
        
        ===================================================================================================================================
        
        // Add Items //
        // Once a tuple is created, you cannot add items to it.
        // contoh : 
        // You cannot add items to a tuple:
           thistuple = ("apple", "banana", "cherry")
           y = list(thistuple)
           y.append("orange")
           thistuple = tuple(y)

           print (thistuple)
        
        // output : 
           ('apple', 'banana', 'cherry', 'orange')
        
        // simplenya, y = list y mengcopy list yang ada di thistuple lalu ditambahkannya orange menggunakan y.append("orange") 
        // thistuple = tuple(y) thistuple adalah tuple yang sudah dicopy dan ditambahkan dengan orange
        // dan menghasilkan output yang ada diatas agak susah ya jelasinnya :V

        ===================================================================================================================================
        
        // Remove Items
        // You cannot remove items in tuple
        // Tuples are unchangeable, so you cannot remove items from it, but you can use the same 
        // workaround as we used for changing and adding tuple items:
        // Contoh :
        // Convert the tuple into a list, remove "apple", and convert it back into a tuple:
           # asli
           thistuple = ("apple", "banana", "cherry")
           # edit
           y = list(thistuple)
           y.remove("orange")
           thistuples = tuple(y)
           
           # asli 
           print (thistuple)
           # edit
           print (thistuples)

        // Output :
           ('apple', 'banana', 'cherry')
           ('banana', 'cherry') 
        
        // cara ini adalah cara untuk menghapus itemnya ingat tidak tuple tidak bisa dihapus jadi saya
        // membuat perbandingan, saya membuat 2 output yaitu print(thistuple) dan print(thistuples)
        // bedanya bisa dilihat di hasil outputnya itulah fungsi dari copy list pertama.
        // maaf kalo ribet :)

        // Or you can delete the tuple completely:
        // Contoh :
        // The del keyword can delete the tuple completely:
           thistuple = ("apple", "banana", "cherry")
           del thistuple
           print(thistuple) #this will raise an error because the tuple no longer exists

        // output :
           erorr
        // akan terjadi error karena dia menghapus langsung thistuple

        ===================================================================================================================================
        
        // unpack tuple //

        // Unpacking a Tuple //
        // When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
        // Contoh :
        // Packing a tuple:
           fruits = ("apple", "banana", "cherry")
           print(fruits)
        
        // output :
           ('apple', 'banana', 'cherry')

        // But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
        // Contoh :
        // unpacking in a tuple:
           fruits = ("apple", "banana", "cherry")

           (green, yellow, red) = fruits

           print(green)
           print(yellow)
           print(red)

        // output : 
           apple
           banana
           cherry

        // simplenya green, yellow, red dia ibaratnya sama posisinya dengan list fruits
        
        // Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.
        
        // Using Asterix* //
        // If the number of variables is less than the number of values, you can add an * to the variable name 
        // and the values will be assigned to the variable as a list:
        // Contoh : 
        // Assign the rest of the values as a list called "red":
           fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

           (green, yellow, *red) = fruits

           print(green)
           print(yellow)
           print(red)

        // output :
           apple
           banana
           ['cherry', 'strawberry', 'raspberry']

        // If the asterix is added to another variable name than the last, Python will assign values
        // to the variable until the number of values left matches the number of variables left.
        // Contoh : 
        // Add a list of values the "tropic" variable:
           fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

           (green, *tropic, red) = fruits

           print(green)
           print(tropic)
           print(red)
      
        ===================================================================================================================================
        
        // Loop Tuples //
        // Loop Through a Tuple //
        // You can loop through the tuple items by using a for loop.
        // Contoh :
        // Iterate through the items and print the values:
           thistuple = ("apple", "banana", "cherry")
           for x in thistuple:
            print(x) 
      
        // Output :
           apple
           banana
           cherry

        // kasus diatas adalah contoh dari perulangan. 
        
        ===================================================================================================================================
        
        // Loop Through the Index Numbers //
        // You can also loop through the tuple items by referring to their index number.
        // Use the range() and len() functions to create a suitable iterable.
        // Contoh:
        // Print all items by referring to their index number:
           thistuple = ("apple", "banana", "cherry")
           for i in range(len(thistuple)):
             print(thistuple[i])
 
        // output :
           apple
           banana
           cherry

        // Using a While Loop //
        // You can loop through the list items by using a while loop.
        // Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
        // Remember to increase the index by 1 after each iteration.
        // Contoh :
        // Print all items, using a while loop to go through all the index numbers:
           thistuple = ("apple", "banana", "cherry")
           i = 0
           while i < len(thistuple):
             print(thistuple[i])
             i = i + 1
           print("Kamu melakukan ", i, "kali perulangan") 

        // output : 
           apple
           banana
           cherry
           Kamu melakukan  3 kali perulangan

        ===================================================================================================================================
        
        // Tuple Methods //
        // Python has two built-in methods that you can use on tuples.
          
           Method	   Description
           count()	Returns the number of times a specified value occurs in a tuple
           index()	Searches the tuple for a specified value and returns the position of where it was found

        ===================================================================================================================================
===========================================================================================================================================
/// 16 ///
/// Dictionary ///
        ===================================================================================================================================

        // 1. Apa itu Dictionary pada Python? //

        // Dictionary adalah stuktur data yang bentuknya seperti kamus. Ada kata kunci kemudian ada nilaninya. 
        // Kata kunci harus unik, sedangkan nilai boleh diisi denga apa saja.

        // Contoh:
           aku = {
               "nama": "Petani Kode",
               "url:" "https://www.petanikode.com"
           }

        // Pada contoh di atas kita membuat sebuah Dictionary bernama aku dengan isi data nama dan URL. 
        // nama dan url adalah kunci (key) yang akan kita gunakan untuk mengakses nilai di dalamnya.
        // Inilah perbedaanya dibandingkan list dan tuple. Dictionary memiliki kunci berupa teks—bisa juga 
        // angka—sedangkan list dan tuple menggunakan indeks berupa angka saja untuk mengakses nilainya.
        // Dalam bahasa pemrograman lain (seperti PHP), Dictionary juga dikenal dengan sebutan asosiatif array.

        ===================================================================================================================================

        // 2. Membuat Dictionary //

        // Hal yang wajib ada di dalam pembuatan Dictionary adalah:
        //       1. nama dictionary,
        //       2. key,
        //       3. value,
        //       4. buka dan tutupnya menggunakan kurung kurawal.
        // Antara key dan value dipisah dengan titik dua (:) dan apabila terdapat lebih dari satu item, 
        // maka dipisah dengan tanda koma (,).

        // Contoh satu item:
           nama_dict = {
               "key": "value"
           }

        // Contoh tiga item:
           nama_dict = {
               "key1": "value",
               "key2": "value",
               "key3": "value"
           }

        #===================================================================================================================================

        // Isi dari Dictionary dapat berupa:
        //       1. String
        //       2. Integer
        //       3. Objek
        //       4. List
        //       5. Tuple
        //       6. Dictionary
        //       7. dsb.

        // Contoh:
           pak_tani = {
               "nama": "Petani Kode",
               "umur": 22,
               "hobi": ["coding", "membaca", "cocok tanam"],
               "menikah": False,
               "sosmed": {
                   "facebook": "petanikode",
                   "twitter": "@petanikode"
               } 
           }

        // Mari kita lihat isi dari Dictionary di atas:
        //       1. nama berisi string "Petani Kode"
        //       2. umur berisi integer 22
        //       3. hobi berisi list dari string
        //       4. menikah berisi boolean False
        //       5. dan sosmed berisi Dictionary

        #===================================================================================================================================

        // Menggunakan Konstruktor //
        // Selain menggunakan cara di atas, kita juga bisa membaut Dictionary dari constructor dict() dengan parameter key dan value.
        
        // Contoh:
           warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")
        
        // Maka akan menghasilkan dictionary seperti ini:
        // Output :
           {'jeruk': 'orange', 'apel': 'merah', 'pisang': 'kuning'}

        ===================================================================================================================================

        // 3. Mengakses Nilai Item dari Dictionary //
        
        // Contoh :
        // Membuat Dictionary
           pak_tani = {
               "nama": "Petani Kode",
               "umur": 22,
               "hobi": ["coding", "membaca", "cocok tanam"],
               "menikah": False,
               "sosmed": {
                   "facebook": "petanikode",
                   "twitter": "@petanikode"
               } 
           }

        // Mengakses isi dictionary
           print("Nama saya adalah %s" % pak_tani["nama"])
           print("Twitter: %s" % pak_tani["sosmed"]["twitter"])

        // Output :
           Nama saya adalah Petani Kode
           Twitter: @petanikode

        #===================================================================================================================================

        // program.me

           kisah_tegar = {
               "nama": "Kisah Tegar",
               "umur": 22,
               "hobi": ["Coding", "Membaca", "Gaming"],
               "menikah": False,
               "sosmed": {
                   "facebook": "Kisah Tegar",
                   "twitter": "@kisahtegar",
                   "instagram": "@kisahtegarp"
               } 
           }

           ans = True
           while ans:
               question = input("Apa yang anda cari? : ")
    
               if question == 'nama':
                   print("Nama : "+ kisah_tegar["nama"])
               elif question == 'umur':
                   print("Umur : "+ str(kisah_tegar["umur"]))
               elif question == 'hobi':
                   print("Hobinya : ")
               for hb in kisah_tegar["hobi"]:
                   print("- {}". format(hb))
               elif question == 'menikah':
                   if (kisah_tegar["menikah"]):
                       print("Status : Menikah")
                   else:
                       print("Status : Jomblo")
               elif question == 'sosmed':
                   print("Sosmed : ")
                   for sd in kisah_tegar["sosmed"]:
                       print ("- {} : {}". format(sd, kisah_tegar["sosmed"][sd])) 

        #===================================================================================================================================
        
        // Unordered //
        // When we say that dictionaries are ordered, it means that the items does not have a defined order, you cannot 
        // refer to an item by using an index.

        // Changeable //
        // Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

        // Duplicates Not Allowed //
        // Dictionaries cannot have two items with the same key:

        // Contoh :
        // Duplicate values will overwrite existing values:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964, # <---- pertama
               "year": 2020 # <---- akhir
            }
           print(thisdict)

        // Output :
           {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

        // simplenya, items yang diduplikat akan ditimpa dengan item setelahnya atau items yang terakhir
        
        ===================================================================================================================================
        
        // Python - Access Dictionary Items //

        // Accessing Items //
        // You can access the items of a dictionary by referring to its key name, inside square brackets:

        // contoh :
        // Get the value of the "model" key:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           x = thisdict["model"]
           print(x)

        // Output :
           Mustang

        // There is also a method called get() that will give you the same result:
        // Contoh :
        // Get the value of the "model" key:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           x = thisdict.get("model")
           print(x)
           
        // Output :
           Mustang 

        // dari kedua contoh tersebut outputnya akan sama saja 
      
        #===================================================================================================================================
        
        // Get Keys //
        // The keys() method will return a list of all the keys in the dictionary.
        // Contoh : 
        // Get a list of the keys:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           x = thisdict.keys()
           print(x)
           
        // Output :
           dict_keys(['brand', 'model', 'year'])

        // ibaratnya, x = thisdict.keys() method keys() dia akan mengembalikan daftar semua kunci yang ada di thisdict
        // atau di dictionaries.
        // Daftar kunci adalah tampilan kamus, artinya setiap perubahan yang dilakukan pada kamus akan tercermin dalam daftar kunci.
        
        // Contoh : 
        // Add a new item to the original dictionary, and see that the keys list gets updated as well:
           car = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           x = car.keys()

           print(x) #before the change

           car["color"] = "white"

           print(x) #after the change

        // Output :
           dict_keys(['brand', 'model', 'year'])
           dict_keys(['brand', 'model', 'year', 'color'])
        
        #===================================================================================================================================
        
        // Get Values //
        // The values() method will return a list of all the values in the dictionary.

        // Contoh :
        // Get a list of the values:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           x = thisdict.values()

           print(x)
        
        // Output : 
           dict_values(['Ford', 'Mustang', 1964])

        // ibaratnya, x = thisdict.values() dia akan mengeluarkan isi dari kunci pada dict tersebut
        
        // Daftar nilai adalah tampilan kamus, yang berarti bahwa setiap perubahan yang dilakukan 
        // pada kamus akan tercermin dalam daftar nilai.
        // Contoh :
        // Add a new item to the original dictionary, and see that the keys list gets updated as well:
           car = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           x = car.values()

           print(x) #before the change

           car["year"] = 2020

           print(x) #after the change

        // Output : 
           dict_values(['Ford', 'Mustang', 1964])
           dict_values(['Ford', 'Mustang', 2020])
        
        // items yang diduplikat akan ditimpa dengan item setelahnya atau items yang terakhir.
        
        #===================================================================================================================================
        
        // Get Items //
        // The items() method will return each item in a dictionary, as tuples in a list.

        // Contoh : 
        // Get a list of the key:value pairs:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           x = thisdict.items()

           print(x)

        // Output : 
           dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

        // simplenya, x = thisdict.items() akan mengeluarkan semua items yang ada di thisdict.
        
        // The returned list is a view of the items of the dictionary, meaning that any changes done 
        // to the dictionary will be reflected in the items list.
        // Contoh :
        // Add a new item to the original dictionary, and see that the items list gets updated as well:
           car = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           x = car.items()

           print(x) #before the change

           car["year"] = 2020

           print(x) #after the change

        // Output :
           dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
           dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
        
        #===================================================================================================================================
        
        // Python - Change Dictionary Items //

        // Change Values //
        // You can change the value of a specific item by referring to its key name:
        // Contoh :
        // Change the "year" to 2018:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }

           thisdict["year"] = 2018

           print(thisdict)

        // Output : 
           {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

        // cara diatas adalah untuk mengganti nilai pada keys

        ===================================================================================================================================
        
        // Update Dictionary //
        // The update() method will update the dictionary with the items from the given argument.

        // The argument must be a dictionary, or an iterable object with key:value pairs.

        // Contoh :
        // Update the "year" of the car by using the update() method:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           thisdict.update({"year": 2020})

           print(thisdict)

        // Output : 
           {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

        // cara diatas adalah untuk mengupdate thisdict
        
        ===================================================================================================================================
        
        // Python - Add Dictionary Items //
        // Adding Items //
        // Adding an item to the dictionary is done by using a new index key and assigning a value to it:
        // Contoh :
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           thisdict["color"] = "red"
           print(thisdict)

        // Output : 
           {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

        #===================================================================================================================================
        
        // Update Dictionary //
        // The update() method will update the dictionary with the items from a given argument. 
        // If the item does not exist, the item will be added.
        // The argument must be a dictionary, or an iterable object with key:value pairs.
        
        // Contoh :
        // Add a color item to the dictionary by using the update() method:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           thisdict.update({"color": "red"})

           print(thisdict)

        // Output :
           {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

        ===================================================================================================================================

        // Python - Remove Dictionary Items //
        // Removing Items //
        // There are several methods to remove items from a dictionary:
        // Contoh pop() :
        // The pop() method removes the item with the specified key name:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           thisdict.pop("model")
           print(thisdict)

        // Output : 
           {'brand': 'Ford', 'year': 1964}

        // Contoh popitem() :
        // The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           thisdict.popitem()
           print(thisdict)

        // Output : 
           {'brand': 'Ford', 'model': 'Mustang'}

        // Contoh del :
        // The del keyword removes the item with the specified key name:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           del thisdict["model"]
           print(thisdict)
        
        // Output : 
           {'brand': 'Ford', 'year': 1964}

        // Contoh clear() :
        // The clear() method empties the dictionary:
           thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
           }
           thisdict.clear()
           print(thisdict)

        // Output :
           {}

        ===================================================================================================================================
        
        // Python - Loop Dictionaries //

        // Loop Through a Dictionary //
        // You can loop through a dictionary by using a for loop.
        // When looping through a dictionary, the return value are the keys of the dictionary, 
        // but there are methods to return the values as well.

        // Contoh :
        // Print all key names in the dictionary, one by one:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           for x in thisdict:
               print(x)
        
        // Output :
           brand
           model
           year

        // Contoh ke-2 :
        // Print all values in the dictionary, one by one:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           for x in thisdict:
               print(thisdict[x])
        
        // Output :
           Ford
           Mustang
           1964

        // Contoh ke-3 :
        // You can also use the values() method to return values of a dictionary:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           for x in thisdict.values():
               print(x)

        // Output :
           Ford
           Mustang
           1964

        // Contoh ke-3 :
        // You can use the keys() method to return the keys of a dictionary:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           for x in thisdict.keys():
               print(x)

        // Output :
           brand
           model
           year

        // Contoh ke-4 :
        // Loop through both keys and values, by using the items() method:
           thisdict =	{
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           for x, y in thisdict.items():
               print(x, y)

        // Output : 
           brand Ford
           model Mustang
           year 1964

        // atau bisa juga dengan 
           for x in thisdict:
               print(x, thisdict[x])

        // Output sama saja.

        ===================================================================================================================================

        // Python - Copy Dictionaries //
        // Copy a Dictionary //
        // You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
        // and changes made in dict1 will automatically also be made in dict2.
        // There are ways to make a copy, one way is to use the built-in Dictionary method copy().

        // Contoh copy() :
        // Make a copy of a dictionary with the copy() method:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           mydict = thisdict.copy()
           print(mydict)
        
        // Output : 
           {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

        // Another way to make a copy is to use the built-in function dict().
        // Contoh dict() :
        // Make a copy of a dictionary with the dict() function:
           thisdict = {
               "brand": "Ford",
               "model": "Mustang",
               "year": 1964
           }
           mydict = dict(thisdict)
           print(mydict)

        // Output : 
           {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

        ===================================================================================================================================

        // Python - Nested Dictionaries //
        // Nested Dictionaries //
        // A dictionary can contain dictionaries, this is called nested dictionaries.

        // Contoh :
        // Create a dictionary that contain three dictionaries:
           myfamily = {
               "child1" : {
                  "name" : "Emil",
                  "year" : 2004
               },
               "child2" : {
                  "name" : "Tobias",
                  "year" : 2007
               },
               "child3" : {
                  "name" : "Linus",
                  "year" : 2011
               }
            }

            print(myfamily)

        // Output : 
           {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

        // Or, if you want to add three dictionaries intto a new dictionary:
        // Contoh :
        // Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
           child1 = {
               "name" : "Emil",
               "year" : 2004
           }
           child2 = {
               "name" : "Tobias",
               "year" : 2007
           }
           child3 = {
               "name" : "Linus",
               "year" : 2011
           }

           myfamily = {
               "child1" : child1,
               "child2" : child2,
               "child3" : child3
           }

           print(myfamily)

           # Tambahan bila ingin print dalemannya
           for x,y in child1.items():
               print (x,y)

        // Output : 
           {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
           
           # Tambahan
           name Emil
           year 2004 

        ===================================================================================================================================
        
        // Python Dictionary Methods //
        // Dictionary Methods //
        // Python has a set of built-in methods that you can use on dictionaries.

            Method	Description
            clear()	Removes all the elements from the dictionary
            copy()	Returns a copy of the dictionary
            fromkeys()	Returns a dictionary with the specified keys and value
            get()	Returns the value of the specified key
            items()	Returns a list containing a tuple for each key value pair
            keys()	Returns a list containing the dictionary's keys
            pop()	Removes the element with the specified key
            popitem()	Removes the last inserted key-value pair
            setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
            update()	Updates the dictionary with the specified key-value pairs
            values()	Returns a list of all the values in the dictionary
        
        ===================================================================================================================================
===========================================================================================================================================
/// 17 ///
/// Satuan Konversi ///
        ===================================================================================================================================

       // Latihan satuan konversi

         // program konversi celcius ke satuan lain
            print("\nPROGRAM KONVERSI TEMPERATUR\n") # \n digunakan untuk memberikan space atau jarak line atas bawah 

            celcius = float(input('Masukan suhu dalam celcius : '))
            print("suhu adalah",celcius, "Celcius")

            # reamur
            reamur = (4/5) * celcius
            print("suhu dalam reamur adalah ",reamur, "Reamur")

            # fahrenheit
            fahrenheit = ((9/5) * celcius) + 32
            print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

            # Kelvin
            kelvin = celcius + 273
            print("suhu dalam kelvin adalah ",kelvin, "Kelvin")

        ===================================================================================================================================
===========================================================================================================================================
/// 18 ///
/// Buat Login ///
        ===================================================================================================================================
        // login dengan database/dictionary yang sudah saya Inputkan

        // import ini hanya untuk menambahkan waktu tanggal biar cakep hahahaha
           import datetime

        // datetime
           mylistdate = []
           today = datetime.date.today()
           mylistdate.append(today)

        // like dictionary
           database={
              'kisah': 'admin', 
              'tegar': '1806', 
              'putra': '2003'
           }

           def login():
              username = input('Enter Username: ')
              password = input('Enter Password: ')
              if password in database[username]:
                 print("Welcome,", username,". This is a new day : ", mylistdate[0])
            
              else:
                 print ('Invalid code')

        // eksekusi
           login()



        ===================================================================================================================================
===========================================================================================================================================
/// 19 ///
/// fungsi dan prosedur ///
        ===================================================================================================================================

        // Contoh simple tentang fungsi //
        // fungsi pada python disebut dengan def
        // membuat fungsi
           def salam():
               print("hello world")

        // Pemanggilan Fungsi, dapat dilakukan berkali-kali
           salam()
           salam() #jika ditambah 2 maka...
        // Hasilnya jika ada 1 salam() :
           hello world

        // jika terdapat 2 salam() :
           hello world
           hello world

        ===================================================================================================================================

        // fungsi parameter //

        // contoh program parameter
        // saya menambahkan input data
           a = int(input("Masukkan nilai alas: "))
           t = int(input("Masukkan nilai tinggi: "))

        // membuat fungsi dengan parameter
           def luas_segitiga(alas, tinggi):
               luas = (alas * tinggi) / 2
               print("Luas segitiga : %0.2f" % luas) #mengapa ada 0.2 karena saya hanya inggin ada 2 nomor setelah koma atau titik

        // Pemanggilan fungsi
           luas_segitiga(a, t) # masukkan parameternya

        ===================================================================================================================================

        // Fungsi return mengembalikan nilai //
        // return diibaratkan supaya bisa diteruskan atau kita melakukan print saat dipanggil
        // beda dengan tidak memakai return seperti diatas, dia akan langsung melakukan print

        // Contoh program dengan return
        // contoh input data
           sisi = int(input("Masukan Nilai sisi: "))
           vsisi = int(input("Masukan Nilai volume: "))
       
        // fungsi luas persegi
           def luas_persegi(sisi):
               luas = sisi * sisi
               return luas

           print("Luas persegi: %d" % luas_persegi(sisi))

        // fungsi dari Volume persegi
           def volume_persegi(vsisi):
               volume = luas_persegi(sisi) * vsisi
               print ("Volume persegi: %d" % volume)

        // Pemanggilan fungsi atau hasil akhir
           volume_persegi(vsisi)

        ===================================================================================================================================

        // variabel Global dan Lokal //
        // Variabel Global adalah variabel yang bisa diakses dari semua fungsi, 
        // Variabel lokal hanya bisa diakses di dalam fungsi tempat ia berada saja.

        // Contoh program
        // membuat variabel global
            nama = "Kisah Tegar"
            versi = "10.12.0"

           def help():
               // ini variabel lokal
               nama = "Ngoding"
               versi = "1.0.2"
               // mengakses variabel lokal
               print ("Nama: %s" % nama)
               print ("Versi: %s" % versi)


        // mengakses variabel global
           print ("Nama: %s" % nama)
           print ("Versi: %s" % versi)

        // memanggil fungsi help()
           help()

        // Hasilnya:
           Nama: Kisah Tegar
           Versi: 10.12.0
           Nama: Ngoding
           Versi: 1.0.2 

        ===================================================================================================================================

        // fungsi contoh lainnya // 
           def my_function(fname):
               print(fname + " Refsnes")

           my_function("Emil")
           my_function("Tobias")
           my_function("Linus")
        
        // hasilnya: 
           Emil Refsnes
           Tobias Refsnes
           Linus Refsnes

        ===================================================================================================================================

        // fungsi contoh lainnya // 
           def my_function(fname, lname):
               print(fname + " " + lname)

           my_function("Emil", "Refsnes")
         
        // hasilnya:
           Emil Refsnes 

        ===================================================================================================================================
     
        // fungsi contoh lainnya dengan *wargs // 
           def my_function(*kids):
               print("The youngest child is " + kids[2])

           my_function("Emil", "Tobias", "Linus")

        // hasilnya:
           The youngest child is Linus
        
        // mengapa linus karena perhitungan indeks dimulai dari angka 0
        // 0 = Emil, 1 = Tobias, 2 = Linus      

        ===================================================================================================================================

        // fungsi contoh lainnya //
           def my_function(child3, child2, child1):
               print("The youngest child is " + child3)

           my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
           
        // hasilnya: 
           The youngest child is Linus   

        ===================================================================================================================================
        
        // fungsi contoh lainnya demgan **kwargs //
           def my_function(**kid):
               print("His last name is " + kid["lname"])

           my_function(fname = "Tobias", lname = "Refsnes")

        // hasilnya: 
           His last name is Refsnes

        ===================================================================================================================================
        
        // fungsi contoh lainnya //
        x = "awesome"

        def myfunc():
            global x
            x = "fantastic"

        myfunc()

        print("Python is " + x)
        
        // menurut saya ibaratnya kalo make global kita bisa menarik kata fantastic padahal print diluar
        // fungsi. jadi dia tidak ngeprint awesome melainkan mengprint fantastic.
        // bila globalnya di hapus python akan mengprint  awesome.
        // maaf kalo ribet jelasinnya yang ngetik sentolop orangnya :)
        
        ===================================================================================================================================
        
        // Default Parameter Value //
        // The following example shows how to use a default parameter value.
        // If we call the function without argument, it uses the default value:
        // Contoh :
           def my_function(country = "Norway"):
              print("I am from " + country)

           my_function("Sweden")
           my_function("India")
           my_function()
           my_function("Brazil")

        // Output :
           I am from Sweden
           I am from India
           I am from Norway
           I am from Brazil   
        
        // ibaratnya country = "Norway" dia menggantikan my_functiion() yang kosong.

        ===================================================================================================================================
        
        // Recursion //
        // Python also accepts function recursion, which means a defined function can call itself.
        // Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit 
        // of meaning that you can loop through data to reach a result.
        // The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never 
        // terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a 
        // very efficient and mathematically-elegant approach to programming.
        // In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as 
        // the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
        // To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

        // Contoh :
        // Recursion Example
           def tri_recursion(k):
             if(k > 0):
               result = k + tri_recursion(k - 1)
               print(result)
             else:
               result = 0
               return result

           print("Recursion Example Results")
           tri_recursion(6)

        // Output :
           Recursion Example Results
           1
           3
           6
           10
           15
           21

        // cara kerjanya gini //
        // Contoh :
        // function(x)
        // x + function(x-1)

        // function(1)
        // 1 + function(1-1) 
        // 1 + 0 = 1

        // function(2)
        // 2 + function(2-1) 
        // 2 + 1 + function(1-1)
        // 2 + 1 + 0 = 3

        // function(3)
        // 3 + function(3-1)
        // 3 + 2 + function(2-1)
        // 3 + 2 + 1 + function(1-1)
        // 3 + 2 + 1 + 0 = 6

        // function(4)
        // 4 + function(4-1)
        // 4 + 3 + function(3-1)
        // 4 + 3 + 2 + function(2-1)
        // 4 + 3 + 2 + 1 + function(1-1)
        // 4 + 3 + 2 + 1 + 0 = 10

        // dan seterusnya............

        // Jika ingin paham lebih luas lagi kalian bisa uji coba dengan mengubah-ubah script diatas
        
        // Contoh ke-2 :
           def recursion(x):
            if x == 1:
               return 1
            else:
               return(x + recursion(x-1)) 

           x = int(input("input : "))

           print("Nilai faktorial dari {} adalah {}". format(x, recursion(x))) 

        // Output : Output sama seperti diatas tergantung kalian input angkanya berapa.
        
        ===================================================================================================================================
===========================================================================================================================================
/// 20 ///
/// Lambda Expression ///
        ===================================================================================================================================
        // Apa itu Lambda Expression //
        // Lambda expression di Python adalah sebuah ekspresi untuk membuat fungsi.
        // dengan Lambda kita bisa buat fungsi tanpa nama atau dikenal juga dengan
        // anonymous function.
        
        // Syntax :
           lambda arguments : expression

        // contoh kita membat penjumlahan kuadrat seperti ini:
           def suqare_sum(x,y):
               return x**2 + y**2

        // dengan Lambda kita gak perlu pake def dan return. bagkan gak perlu menuliskan namanya.
            lambda x,y: x**2 + y**2
      
        ===================================================================================================================================
        
        // cara menggunakan Lambda Expression //
        // contoh:
           greeting = lambda name: print (f"Hello, {name}")

        // Karena fungsi lambda tidak punya nama, jadi kita butuh variabel untuk menyimpannya.
        // Nanti saat kita mau panggil, kita tinggal tuliskan saja nama variabelnya 
        // seperti ini:
           greeting("mamank garok")
           greeting("tegar")
           greeting("wadidaw")

        // memang sama seperti def tapi bedanya, Lambda khusus untuk fungsi yang 
        // berisi satu ekspresi dan sifat fungsinya akan anonymous.
        
        ===================================================================================================================================
        
        // Anonymous Function di Python //
        // Karena lambda adalah anonymous function, ia akan bebas menggunakan nama apa saja.
        // Dengan kata lain, fungsi lambda bisa disimpan di variabel mana pun.
        // Ini tentunya tidak bisa dilakukan oleh fungsi yang dibuat dengan def.
        // contoh:
           >>> def hello(name):
           ...     print(f"Hello {name}, apa kabar?")
        
        // lalu saya akan input: 
           >>> ucapin = hello(name)

        // nantinya akan muncul error
        // walaupun saya ubah seperti ini:
           >>> ucapin = def hello(name)
        // akan tetap error
        // saya mencoba membuat fungsi hello() dengan def kemudian saya simpan
        // kedalam variable ucapin.
        // mengapa error karena ini bukanlah fungsi anonymous yang boleh diubah-ubah namanya.
        // ============================
        // lalu saya akan mencoba fungsi Lambda
        // contoh: 
           greeting = lambda name: print(f"Hello, {name}")
           sapa = greeting
           greeting("Kisah")
           sapa("Tegar")
         
        // hasilnya:
           Hello, Kisah
           Hello, Tegar

        // dan tidak ada error, karena ini adalah fungsi anonymous atau Lambda
      
        ===================================================================================================================================

        // Eksekusi Lambda Secara Langsung // 
        // Kelebihan fungsi lambda dibandingkan def adalah bisa kita eksekusi langsung.
        // bisa dipakai langsung, tanpa harus memanggil namanya.
        // Contoh:
           (lambda x,y: x**2 + y**2)(4,6) 

        // Tanda kurung yang mengapit fungsi lambda artinya kita akan langsung mengeksekusi fungsi tersebut.
        // Lalu kurung berikutnya akan berisi parameter.
        // Angka 4 dan 6 adalah parameter x dan y yang akan diberikan kepada fungsi Lambda.
        // Mak akita akan langsung mendapatkan hasilnya, yakni: 4**2 + 6**2 = 52.
        // Hasil dari eksekusi ini bisa juga kita simpan ke dalam variabel.
           hasil = (lambda x,y: x**2 + y**2)(4,6)
           print(hasil)
        // Hasilnya:
           52

        ===================================================================================================================================

        // Mengapa Harus Pakai Lambda? //
        // karena Lambda biasanya dibutuhkan saat kita ingin membuat fungsi dalam satu baris.
        // dan dalam kasus tertentu Lambda lebih baik dibandingkan fungsi biasa.
        // Biasanya saat menggunakan fungsi-fungsi seperti filter(), map(), dan reduce() kita akan membutuhkan Lambda.
        // Karena di fungsi-fungsi tersebut membutuhkan parameter fungsi.
        // Contoh:
           bilangan = [10,2,8,7,5,4,3,11,0, 1] 
           filtered_result = map (lambda x: x*x, bilangan)
           print(list(filtered_result))

        // Hasilnya: 
           [100, 4, 64, 49, 25, 16, 9, 121, 0, 1]

        // Pada fungsi map() kita memberikan parameter dengan fungsi lambda.
        // Karena lambda bisa disimpan ke dalam variabel, otmatis dia akan bisa juga jadi parameter.
        // Satu lagi contoh dengan fungsi filter():
           # menentukan bilangan genap
           >>> genap = lambda x: x%2 == 0
           >>> list(filter(genap, range(11))) 
           [0, 2, 4, 6, 8, 10]

        // atau bisa dibuat dalam satu baris:
           >>> list(filter(lambda x: x%2 == 0, range(11)))
           [0, 2, 4, 6, 8, 10]

        // Jadi mengepa harus pakai Lambda?
        // Ya karena kita akan membutuhkannya saat menggunakan fungsi tertentu.

        ===================================================================================================================================
        
        // The expression is executed and the result is returned:
        // Contoh:
        // Add 10 to argument a, and return the result:
           x = lambda a : a + 10
           print(x(5))
        
        // Output : 
           15
        
        #===================================================================================================================================

        // Lambda functions can take any number of arguments:
        // Contoh :
        // Multiply argument a with argument b and return the result:
           x = lambda a, b : a * b
           print(x(5, 6))

        // Output :
           30
        
        #===================================================================================================================================

        // Contoh :
        // Summarize argument a, b, and c and return the result:
           x = lambda a, b, c : a + b + c
           print(x(5, 6, 2))

        // Output :
           13

        ===================================================================================================================================
        
        // Why Use Lambda Functions? //
        // The power of lambda is better shown when you use them as an anonymous function inside another function.
        // Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
           
           def myfunc(n):
               return lambda a : a * n

        // Use that function definition to make a function that always doubles the number you send in:
        // Contoh : 
           def myfunc(n):
               return lambda a : a * n

           mydoubler = myfunc(2)

           print(mydoubler(11))

        // Output :
           22

        // Or, use the same function definition to make both functions, in the same program:
        // Contoh : 
           def myfunc(n):
               return lambda a : a * n

           mydoubler = myfunc(2)
           mytripler = myfunc(3)

           print(mydoubler(11))
           print(mytripler(11))

        // Output :
           22
           33

        // Use lambda functions when an anonymous function is required for a short period of time.

        ===================================================================================================================================
===========================================================================================================================================
/// 21 ///
/// *args and **kwargs ///
        ===================================================================================================================================

        // *args dan **kwargs sebenarnya adalah sebuah variabel. Kadang juga disebut dengan magic variable
        // Variabel ini memiliki kemampuan khusus karena ada tanda bintang (*) di depannya
        // Kalau tidak ada itu maka akan menjadi variabel yang biasa-biasa saja.
        // Jika kita mencoba membuat variabel dengan nama *args dan **kwargs, maka akan terjadi error.
           >>> **nama = "kisah"
             File "<stdin>", line 1
               **nama = "kisah"
                ^
           SyntaxError: invalid syntax
           >>> *nama = "kisah"
             File "<stdin>", line 1
           SyntaxError: starred assignment target must be in a list or tuple       
      
        // mengapa error karena ada simbol bintang (*) di depannya. Sedangkan pada aturan penulisan variabel di Python, 
        // kita tidak dibolehkan menggunakan simbol di depan, kecuali underscore (_).
        // Variabel *args dan **kwargs digunakan sebagai parameter pada fungsi.
        // Contoh:
           # Pembuatan fungsi
           def panggil(*nama):
               print ("daftar orang yang dipanggil:")
               for orang in name:
                   print (orang)
           # Pemanggilan fungsi
           panggil("dian", "deni", "agus")
        
        // Hasilnya: 
           daftar orang yang dipanggil:
           dian
           deni
           agus

        // Catatan: nama *args dan **kwargs bukanlah sesuatu yang baku.
        // Kita juga bisa membuatnya sesuka hati seperti *nama, **nama, *buku, dsb.
        // pada contoh diatas kita bisa memberikan 3 parameter kedalam fungsi panggil().
           panggil("dian", "deni", "agus")

        // Sedangkan pada pembuatanya kita hanya menggunakan satu parameter, yaitu: *nama.
        // Saat kita menambahkan tanda bintang (*) di depan parameter, kita bisa memberikan parameter berapapun yang kita inginkan saat pemanggilan.
        // Waktu yang tepat menggunakan *args dan **kwargs adalah saat kita membuat
        // fungsi dan jumlah parameternya tidak jelas alias tidak pasti (not fixed).
        // biasanya kita membuat seperti ini:
           def colek(nama1, nama2, nama3):
               pass
        // Fungsi tersebut hanya mampu menerima tiga parameter saja.
           colek("eko", "rian," "dwi")

        // coba berikan 1 parameter pasti akan error
           colek("anto")

        // disitulah kita harus menggunakan *args dan **kwargs agar bisa lebih bebas.
        // bisa lebih dari 3 maupun ingin 1 juga bisa
        
        ===================================================================================================================================
        
        // Perbedaan dari *args dan **kwargs //
        // *args menggunakan satu tanda bintang, sedangkan
        // **kwargs menggunakan dua tanda bintang.
        //       
        // * artinya akan membuat parameter menjadi tuple.
        // ** artinya akan membuat parameter menjadi dictionary.
        // Contoh:
           # membuat fungsi dengan parameter *args
           def kirim_sms(*nomer):
               print(nomer)
           
           # membuat fungsi dengan parameter **kwargs
           def tulis_sms(**isi):
               print (isi)

           # Pemanggilan fungsi *args
           kirim_sms(123, 888, 4444)

           # Pemanggilan fungsi **kwargs 
           tulis_sms(tujuan=123, pesan="apa kabar")

        // hasil output:
           (123, 888, 4444)
           {'tujuan': 123, 'pesan': 'apa kabar'}

        // bisa juga seperti ini cara memanggil fungsinya: 
           # siapkan parameternya
           list_nomer = [123, 888, 4444]
           isi_sms = {'tujuan': 4444, 'pesan': 'mau daftar pak'} 

           # pemanggilan fungsi
           kirim_sms(*list_nomer)
           tulis_sms(**isi_sms)

        // Hasil outputnya juga akan sama 

        ===================================================================================================================================
        
        // contoh kasus di dunia nyata // 
        // Salah satu contoh kasus penerapannya di dunia nyata: Fungsi untuk menghitung nilai rata-rata.
        // Karena data yang akan kita hitung nilai rata-ratanya bersifat dinamis,
        // maka kita harus menggunakan *args atau **kwargs.
        // Contoh:
           def rata_rata(*data):
               banyak_data =  len(data)  
               jumlah_data =  sum(data)
               nilai_rata_rata = float(jumlah_data) / float(banyak_data)
               return nilai_rata_rata
           print(rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))

        // fungsi len() adalah fungsi untuk menghitung banyak data yang terdapat dalam tuple atau list.
        // fungsi sum() adalah fungsi untuk menjumlahkan semua data-nya.
        // selanjutnya kita terapkan rumus nilai rata-rata:
           rata_rata = jumlah data / banyak_data
        
        // Hasil Outputnya:
           3.0 

        ===================================================================================================================================
        
        // Contoh menghitung nilai rata-rata dengan input data //
           def nilai_rata_rata():
               n = int(input("Banyaknya Data: "))
               print() #Membuat baris baru

               data = []
               jum = 0

               for i in range(0, n):
                   temp = int(input("Masukkan data ke-%d: " % (i+1)))
                   data.append(temp)
                   jum += data[i]
                   rata2 = jum / n

               print("\nRata-rata  = %0.2f" % rata2)
           nilai_rata_rata() 
      
        // %0.2f fungsinya untuk menampilkan hasil nilai pecahan dengan 2 bilangan desimal / 2 bilangan di belakang koma

        ===================================================================================================================================
===========================================================================================================================================
/// 22 ///
/// Python Numbers ///
        ===================================================================================================================================
        // Example
           x = 1    # int
           y = 2.8  # float
           z = 1j   # complex   

        // Eksekusi: ini akan menampilkan type apa yang dipakai
           print(type(x))
           print(type(y))
           print(type(z))

        ===================================================================================================================================
        
        // int //
        // Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
        // Contoh:
           x = 1
           y = 35656222554887711
           z = -3255522

           print(type(x))
           print(type(y))
           print(type(z))
        
        // output: 
           <class 'int'>
           <class 'int'>
           <class 'int'>
        
        ===================================================================================================================================
        
        // float //
        // Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
           x = 1.10
           y = 1.0
           z = -35.59

           print(type(x))
           print(type(y))
           print(type(z))
        
        // output:
           <class 'float'>
           <class 'float'>
           <class 'float'>
        
        // float can also be scientific numbers with an "e" to indicate the power of 10.
           x = 35e3
           y = 12E4
           z = -87.7e100

           print(type(x))
           print(type(y))
           print(type(z))
        
        // output:
           <class 'float'>
           <class 'float'>
           <class 'float'>

        ===================================================================================================================================
        
        // complex //
        // Complex numbers are written with a "j" as the imaginary part:
           x = 3+5j
           y = 5j
           z = -5j

           print(type(x))
           print(type(y))
           print(type(z))

        // output:
           <class 'complex'>
           <class 'complex'>
           <class 'complex'>

        ===================================================================================================================================
        
        // Type Conversion //
        // You can convert from one type to another with the int(), float(), and complex() methods:
        // Example:
           x = 1    # int
           y = 2.8  # float
           z = 1j   # complex

        // convert from int to float:
           a = float(x)

        // convert from float to int:
           b = int(y)

        // convert from int to complex:
           c = complex(x)

        // lets eksekusi wkwk 
           print(a)
           print(b)
           print(c)

           print(type(a))
           print(type(b))
           print(type(c))

        // output:
           1.0
           2
           (1+0j)
           <class 'float'>
           <class 'int'>
           <class 'complex'>

        // ibaratnya kita bisa ngubah atau convert menjadi beda gitu lah...
        
        ===================================================================================================================================
        
        // Random Number//
        // Import the random module, and display a random number between 1 and 9
        // Example:
           import random
           print(random.randrange(1, 10))
        
        // Output:
           7 # intinya outputnya bakalan random kelakuan ku

        ===================================================================================================================================
===========================================================================================================================================
/// 22 ///
/// Python String  ///
        ===================================================================================================================================

        // Strings are Arrays //
        // Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
        // However, Python does not have a character data type, a single character is simply a string with a length of 1.
        // Square brackets can be used to access elements of the string.
        // Example:
           a = "Hello, World"
           print(a[1])
        
        // output:
           e
        // inget ya setiap ngitung dimulai dari 0. 0 = H lalu 1 = e
        // jadi outputnya e.
        // kalo masih belum paham ibaratnya print(a[1]) dia ngambil huruf yang nomor urutannya 1
        
        ===================================================================================================================================
        
        // Slicing //
        // You can return a range of characters by using the slice syntax.
        // Specify the start index and the end index, separated by a colon, to return a part of the string.
        // Example:
        // Get the characters from position 2 to position 5 (not included):
           b = "Hello, World!"
           print(b[2:5])
           
        // output:
           llo

        // kok bisa gitu?. simplenya dia ngeprint huruf dengan nomor 2, 3, 4 yaitu llo
        // ibaratnya 2 itu awalannya 5 itu akhirnya
        // berarti angkanya 2, 3, 4 = llo kenapa 5 tidak dihitung ? karena di angka akhir print(b[2:5])
        // pusing ya?
      
        ===================================================================================================================================

        // Negative Indexing //
        // Use negative indexes to start the slice from the end of the string:
        // Example:
        // Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
           b = "hello, world"
           print(b[-5:-2])
        
        // output:
           orl 
        
        // kok bisa gitu? hampir sama kek slicing cuma bedanya dia mainnya dari belakang
        // kalo minus dia menghitung dari -1 bukan -0
        // d pada kalimat diatas itu -1 dan seterusnya...
        // contoh:
        // print(b[-5:-2]) dia input angka -5 yaitu w dan -2 yaitu l
        // dari situ terbentuknya kata orl kenapa?
        // -4 = o, -3 = r, -2 = l maka terbentuk kata orl 
        // -5 = w dia tidak terpakai ibaratnya dia batesannya atau angka akhir
        // maaf kalo penjelasan saya ngebingungin kalian
        
        ===================================================================================================================================
        
        // String Methods //
        
        //=================================================================== 
        
        // Example: strip()
        // The strip() method removes any whitespace from the beginning or the end:
           a = " Hello, World "
           printprint(a.strip()) # returns "Hello, World!"

        // output:
           Hello, World

        // simpelnya fungsi strip() buat ngapus spasi awal maupun di akhir.
        
        //=================================================================== 
        
        // Example: lower()
        // The lower() method returns the string in lower case:
           a = "Hello, World!"
           print(a.lower())

        // output:
           hello, world!
        
        // dia ubah tulisannya jadi kecil semua  
        
        //=================================================================== 
        
        // Example: upper()
        // The upper() method returns the string in upper case:
           a = "Hello, World!
           print(a.upper())
        
        // output:
           HELLO, WORLD !
        
        // dia ubah tulisannya jadi BESAR semua

        //=================================================================== 
        
        // Example: replace()
        // The replace() method replaces a string with another string:
           a = "Hello, World!"
           print(a.replace("H", "J"))       
        
        // output:
           Jello, World!
        
        // print(a.replace("H", "J")) H digantikan dengan J
        
        //=================================================================== 
        
        // Example: split()
        // The split() method splits the string into substrings if it finds instances of the separator:
           a = "Hello, World!"
           print(a.split(",")) # returns ['Hello', ' World!']
           
           atau

           a = "Hello, World!"
           b = a.split(",")
           print(b)


        // output:
           ['Hello', ' World!']
        
        // ibaratnya kata yang tadi satu jadi terpecah menjadi beberapa kata
        // jadi kayak list lah dan bisa dilakukan perulangan seru dah
        
        ===================================================================================================================================
        
        // Check String //
        // To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
        // Example: in 
        // Check if the phrase "ain" is present in the following text:
           txt = "The rain in Spain stays mainly in the plain"
           x = "ain" in txt
           print(x)
        
        // output: 
           True 
        
        // contoh diatas melakukan check apakah kalimat ain ada di txt?
        // hasilnya True, karena ada kata ain di txt
        
        //=================================================================== 
        
        // Example: not in
        // Check if the phrase "ain" is NOT present in the following text:
           txt = "The rain in Spain stays mainly in the plain"
           x = "ain" not in txt
           print(x) 
     
        // output:
           False

        // contoh diatas melakukan check apakan ain tidak ada di txt?
        // hasilnya False, karena ada kata ain di txt
        
        ===================================================================================================================================
        
        // String Concatenation //
        // To concatenate, or combine, two strings you can use the + operator.
        // Example: a + b
        // Merge variable a with variable b into variable c:
           a = "Hello"
           b = "World"
           c = a + b
           print(c) 
        
        // output:
           HelloWorld 
        
        //=================================================================== 
        
        // Example: " " 
        // To add a space between them, add a " ":
           a = "Hello"
           b = "World"
           c = a + " " + b
           print(c)

        // output:
           Hello World
        
        ===================================================================================================================================
        
        // String Format //
        // As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
           age = 36
           txt = "My name is John, I am " + age
           print(txt)
        
        // jika di jalankan akan error, mengapa?
        // kita membutuhkan format()
        // saya akan mencoba memperbaiki ulang
           age = 36
           txt = ("My name is John, I am {}". format(age))
           print(txt)

           atau

           age = 36
           txt = "My name is John, and I am {}"
           print(txt.format(age))

        // outputnya:
           My name is John, and I am 36 # sama aja kok yang bawah maupun yang atas
        
        // The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
           quantity = 3
           itemno = 567
           price = 49.95
           myorder = "I want {} pieces of item {} for {} dollars."
           print(myorder.format(quantity, itemno, price))

        // Output:
           I want 3 pieces of item 567 for 49.95 dollars.
        
        // dia akan mengprint sesuai dengan urutan dari atas ke bawah
        // maksudnya dari quantity, itemno, price
        // ada cara lain dengan menggunakan index nomor
        // mari kita liat
        // You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
        // Example:
           quantity = 3
           itemno = 567
           price = 49.95
           myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
           print(myorder.format(quantity, itemno, price))

        // output:
           I want to pay 49.95 dollars for 3 pieces of item 567.
        
        // dengan menggunakan index nomor kita bisa menentukan bagian mana yang ingin
        // diprint terlebih dahulu dengan memakai index nomor
        // Ingat!!! index awal selalu dimulai dari angka 0
        
        ===================================================================================================================================
        
        // Escape Character // 
        // To insert characters that are illegal in a string, use an escape character.
        // An escape character is a backslash \ followed by the character you want to insert.
        // An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
        // Example:
        // You will get an error if you use double quotes inside a string that is surrounded by double quotes:
           txt = "We are the so-called "Vikings" from the north."
           print(txt)

        // disini bila kita akan print akan terjadi error
        // caranya agar kita bisa print kita menggunakan \"
           txt = "We are the so-called \"Vikings\" from the north."
           print(txt)
        
        // output:
           We are the so-called "Vikings" from the north. 

        //=================================================================== 
        
        // \' singgle quote
           txt = 'It\'s alright.'
           print(txt) 

        // output:
           it's alright
 
        //=================================================================== 

        // \\ Backslash
           txt = "This will insert one \\ (backslash)."
           print(txt) 

        // output: 
           This will insert one \ (backslash)
        
        //=================================================================== 
 
        // \n New Line
           txt = "Hello\nWorld!"
           print(txt)
           
        // output:
           Hello
           World!
        
        //=================================================================== 
      
        // \r Carriage Return
           txt = "Hello\rWorld!"
           print(txt) 

        // output:
           Hello
           World!
        
        //=================================================================== 
       
        // \t Tab
           txt = "Hello\tWorld!"
           print(txt) 

        // output:
           Hello  World!
        
        //=================================================================== 
  
        // (\b) Backspace
           #This example erases one character (backspace):
           txt = "Hello \bWorld!"
           print(txt) 
        
        // output:
           HelloWorld!
        
        //=================================================================== 
  
        // (\f) Form Feed
        // output:
        
        // (\ooo) Octal Value
        // tips: 101-132 = A - Z huruf Besar
        // tips: 141-172 = a - z huruf kecil
           #A backslash followed by three integers will result in a octal value:
           txt = "\110\145\154\154\157" 
           print(txt) 
           
        // output:
           Hello
        
        //=================================================================== 
  
        // (\xhh) Hex Value
        // huruf besar
        // tips: 41=A, 42=B, 43=C, 44=D, 45=E, 46=F, 47=G, 48=H, 49=I, 4a=J, 4b=K, 4c=L, 4d=M, 4e=N, 4f=O, 50=P, 51=Q, 
        //       52=R, 53=S, 54=T, 55=U, 56=V, 57=W, 58=X, 59=Y, 5a=Z.
        // huruf kecil
        // tips: 61=a, 62=b, 63=c, 64=d, 65=e, 66=f, 67=g, 68=h, 69=i, 6a=j, 6b=k, 6c=l, 6d=m, 6e=n, 6f=o, 70=p, 71=q, 
        //       72=r, 73=s, 74=t, 75=u, 76=v, 77=w, 78=x, 79=y, 7a=z, 20=space.
           #A backslash followed by an 'x' and a hex number represents a hex value:
           txt = "\x48\x65\x6c\x6c\x6f"
           print(txt) 

        // output:
           Hello

        ===================================================================================================================================
        // String Methods //
        
        // Python has a set of built-in methods that you can use on strings.
        // Note: All string methods returns new values. They do not change the original string.

            Method	            Description
            capitalize()	Converts the first character to upper case
            casefold()	Converts string into lower case
            center()	Returns a centered string
            count()	Returns the number of times a specified value occurs in a string
            encode()	Returns an encoded version of the string
            endswith()	Returns true if the string ends with the specified value
            expandtabs()	Sets the tab size of the string
            find()	Searches the string for a specified value and returns the position of where it was found
            format()	Formats specified values in a string
            format_map()	Formats specified values in a string
            index()	Searches the string for a specified value and returns the position of where it was found
            isalnum()	Returns True if all characters in the string are alphanumeric
            isalpha()	Returns True if all characters in the string are in the alphabet
            isdecimal()	Returns True if all characters in the string are decimals
            isdigit()	Returns True if all characters in the string are digits
            isidentifier()	Returns True if the string is an identifier
            islower()	Returns True if all characters in the string are lower case
            isnumeric()	Returns True if all characters in the string are numeric
            isprintable()	Returns True if all characters in the string are printable
            isspace()	Returns True if all characters in the string are whitespaces
            istitle()	Returns True if the string follows the rules of a title
            isupper()	Returns True if all characters in the string are upper case
            join()	Joins the elements of an iterable to the end of the string
            ljust()	Returns a left justified version of the string
            lower()	Converts a string into lower case
            lstrip()	Returns a left trim version of the string
            maketrans()	Returns a translation table to be used in translations
            partition()	Returns a tuple where the string is parted into three parts
            replace()	Returns a string where a specified value is replaced with a specified value
            rfind()	Searches the string for a specified value and returns the last position of where it was found
            rindex()	Searches the string for a specified value and returns the last position of where it was found
            rjust()	Returns a right justified version of the string
            rpartition()	Returns a tuple where the string is parted into three parts
            rsplit()	Splits the string at the specified separator, and returns a list
            rstrip()	Returns a right trim version of the string
            split()	Splits the string at the specified separator, and returns a list
            splitlines()	Splits the string at line breaks and returns a list
            startswith()	Returns true if the string starts with the specified value
            strip()	Returns a trimmed version of the string
            swapcase()	Swaps cases, lower case becomes upper case and vice versa
            title()	Converts the first character of each word to upper case
            translate()	Returns a translated string
            upper()	Converts a string into upper case
            zfill()	Fills the string with a specified number of 0 values at the beginning        
        
        ===================================================================================================================================
===========================================================================================================================================
/// 23 ///
/// Perbedaan make return atau tidak make ///
        ===================================================================================================================================

        // tidak make return
            def ngitung():
               mtk = int(input("Masukkan Nilai MTK : "))
               bi = int(input("Masukkan Nilai BI : "))
               hasil = ((mtk + bi)/2)
               print(hasil) # <------
               if hasil >= 70:
                  print ("Lulus")
               else:
                  print ("Tidak lulus")
            ngitung()

        // Pakai return
            def ngitung():
               mtk = int(input("Masukkan Nilai MTK : "))
               bi = int(input("Masukkan Nilai BI : "))
               hasil = ((mtk + bi)/2)
               if hasil >= 70:
                  print ("Lulus")
               else:
                  print ("Tidak lulus")
               return hasil # <------
            print(ngitung())


        ===================================================================================================================================
===========================================================================================================================================
/// 24 ///
/// schedule ///
        ===================================================================================================================================

        // Default Scheduler object
           schedule.default_scheduler = <schedule.Scheduler object>
            
        // Default Jobs list
           schedule.jobs = []
            
        // Calls every on the default scheduler instance.
           schedule.every(interval=1)
      
        // Calls run_pending on the default scheduler instance.
           schedule.run_pending()
      
        // Calls run_all on the default scheduler instance.
           schedule.run_all(delay_seconds=0)
        
        // Calls clear on the default scheduler instance.
           schedule.clear(tag=None)
     
        // Calls cancel_job on the default scheduler instance.
           schedule.cancel_job(job)
     
        // Calls next_run on the default scheduler instance.
           schedule.next_run()
     
        // Calls idle_seconds on the default scheduler instance.
           schedule.idle_seconds()
      
         # Schedule Library imported 
         import schedule 
         import time 

         # Functions setup 
         def sudo_placement(): 
            print("Get ready for Sudo Placement at Geeksforgeeks") 

         def good_luck(): 
            print("Good Luck for Test") 

         def work(): 
            print("Study and work hard") 

         def bedtime(): 
            print("It is bed time go rest") 
            
         def geeks(): 
            print("Shaurya says Geeksforgeeks") 

         # Task scheduling 
         # After every 10mins geeks() is called. 
         schedule.every(10).minutes.do(geeks) 

         # After every hour geeks() is called. 
         schedule.every().hour.do(geeks) 

         # Every day at 12am or 00:00 time bedtime() is called. 
         schedule.every().day.at("00:00").do(bedtime) 

         # After every 5 to 10mins in between run work() 
         schedule.every(5).to(10).minutes.do(work) 

         # Every monday good_luck() is called 
         schedule.every().monday.do(good_luck) 

         # Every tuesday at 18:00 sudo_placement() is called 
         schedule.every().tuesday.at("18:00").do(sudo_placement) 

         # Loop so that the scheduling task 
         # keeps on running all time. 
         while True: 

            # Checks whether a scheduled task 
            # is pending to run or not 
            schedule.run_pending() 
            time.sleep(1) 

        ===================================================================================================================================
===========================================================================================================================================
/// 25 ///
/// Program untuk mengetahui karakter yang di inputkan ///
        ===================================================================================================================================

         # FYI
         print ("Program mengetahui karakter")
         print ("[/q untuk keluar]")

         # biar bisa ngulang
         while True:
            
            # pertanyaan
            x = input("\nMasukkan Karakter : ")
            
            # percabangan
            if x == '/q':
               print ("Terimakasih :)")
               break
            elif x.isdigit():
               print ("Anda memasukkan angka yang berdigit :", len(x))
            elif x.isupper():
               print ("Karakter yang diinputkan adalah huruf besar")
            elif x.islower():
               print ("Karakter yang diinputkan adalah huruf kecil")
            else:
               print ("Apa yang anda input ?") 


        ===================================================================================================================================
===========================================================================================================================================
/// 26 ///
/// Program sederhana percabangan dan penjumlahan ///
        ===================================================================================================================================

         # import bahan
         import os
         from prettytable import PrettyTable

         # Membersihkan layar
         os.system("cls")

         # Membuat table menggunakan pretty table
         myTable = PrettyTable(["Jenis", "No", "Judul", "Harga"])
         myTable.add_row(["Horor", "1 \n2 \n3", "Paku Kuntilanak \nSumpah Pocong \nRumah Hantu", "Rp 7500 \nRp 6000 \nRp 4000"])
         myTable.add_row(["---------\nRomantic", "-----\n1 \n2 \n3", "----------------\nI Love You \nNow and Forever \nMy Girl","---------\nRp 5000 \nRp 3000 \nRp 2500"])
         print (myTable)
         print ("============= Program Menghitung =============")

         # eksekusi
         h = int(input("Pilih No Horor : "))
         r = int(input("Pilih No Romantic : "))

         # Memperindah
         print ("\n")
         print ("=" * 20)
         print ("       Judul")
         print ("=" * 20)

         # database horror
         db_horor = {
            1: 7500,
            2: 6000,
            3: 4000
         }

         # database romantic
         db_romantic = {
            1: 5000,
            2: 3000,
            3: 2500
         }

         # 1
         if h == 1 and r == 1:
            print ("- Paku Kuntilanak \n- I Love You")
            print ("\nTotal Harga : Rp", db_horor[1] + db_romantic[1])
         elif h == 1 and r == 2:
            print ("- Paku Kuntilanak \n- Now and Forever")
            print ("\nTotal Harga : Rp", db_horor[1] + db_romantic[2])
         elif h == 1 and r == 3:
            print ("- Paku Kuntilanak \n- My Girl")
            print ("\nTotal Harga : Rp", db_horor[1] + db_romantic[3])

         # 2
         elif h == 2 and r == 1:
            print ("- Sumpah Pocong \n- I Love You")
            print ("\nTotal Harga : Rp", db_horor[2] + db_romantic[1])
         elif h == 2 and r == 2:
            print ("- Sumpah Pocong \n- Now and Forever")
            print ("\nTotal Harga : Rp", db_horor[2] + db_romantic[2])
         elif h == 2 and r == 3:
            print ("- Sumpah Pocong \n- My Girl")
            print ("\nTotal Harga : Rp", db_horor[2] + db_romantic[3])

         #3
         elif h == 3 and r == 1:
            print ("- Rumah Hantu \n- I Love You")
            print ("\nTotal Harga : Rp", db_horor[3] + db_romantic[1])
         elif h == 3 and r == 2:
            print ("- Rumah Hantu \n- Now and Forever")
            print ("\nTotal Harga : Rp", db_horor[3] + db_romantic[2])
         elif h == 3 and r == 3:
            print ("- Rumah Hantu \n- My Girl")
            print ("\nTotal Harga : Rp", db_horor[3] + db_romantic[3])
         
         # Jika salah input   
         else:
            print ("Kamu salah menginput data")


        ===================================================================================================================================
===========================================================================================================================================
/// 27 ///
/// Simple censorship of dirty words ///
        ===================================================================================================================================
        // Using dictionary //
         # database
         db_toxic = {
            "kontol",
            "noob",
            "fuck",
            "fk",
            "dick",
            "sex"
         }
         #loop
         while 1:
            # input data
            chat = input("Chat : ")
            # sensor
            if chat in db_toxic:
               print ("*" * len(chat))
            else:
               print (chat) 

        // not using dictionary //
         while 1:
            chat = input("Chat : ")
            def detact(chat):
               for i in "noob", "shit", "fk":
                     chat = chat.replace(i, "*" * len(chat))
               return chat
            
            print(detact(chat))

        ===================================================================================================================================
===========================================================================================================================================
/// 28 ///
/// Python Sets ///
        ===================================================================================================================================

           myset = {"apple", "banana", "cherry"}

        // Set //
        // Sets are used to store multiple items in a single variable.
        // Set is one of 4 built-in data types in Python used to store collections of data, 
        // the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
        // A set is a collection which is both unordered and unindexed.
        // Sets are written with curly brackets.

        // Contoh : 
        // Create a Set:
           thisset = {"apple", "banana", "cherry"}
           print(thisset) 
        
        // output :
           {'apple', 'banana', 'cherry'}
        // Note: the set list is unordered, meaning: the items will appear in a random order.
        // Refresh this page to see the change in the result.
        // Simplenya, output akan selalu berbeda setiap dieksekusi karena output akan random
        // Catatan: Set tidak berurutan, jadi Anda tidak bisa memastikan di mana urutan item akan muncul.
        
        // Set Items //
        // Set items are unordered, unchangeable, and do not allow duplicate values.

        // Unordered //
        // Unordered means that the items in a set do not have a defined order.
        // Set items can appear in a different order every time you use them, and cannot be refferred to by index or key.

        // Unchangeable //
        // Sets are unchangeable, meaning that we cannot change the items after the set has been created.
        // Once a set is created, you cannot change its items, but you can add new items.

        // Duplicates Not Allowed //
        // Sets cannot have two items with the same value.

        // Contoh:
        // Duplicate values will be ignored:
           thisset = {"apple", "banana", "cherry", "apple"}

           print(thisset)
        
        // output :
           {'apple', 'cherry', 'banana'}

        // simplenya jika ada nilai yang sama dia akan diabaikan.
        
        ===================================================================================================================================
        
        // Set Items - Data Types //
        // Set items can be of any data type:

        // Contoh:
        // String, int and boolean data types:
           set1 = {"apple", "banana", "cherry"}
           set2 = {1, 5, 7, 9, 3}
           set3 = {True, False, False}

           print(set1)
           print(set2)
           print(set3)

        // Output:
           {'banana', 'cherry', 'apple'}
           {1, 3, 5, 7, 9}
           {False, True}

        // A set can contain different data types:

        // Contoh :
        // A set with strings, integers and boolean values:
           set1 = {"abc", 34, True, 40, "male"}

           print(set1)

        // Output:
           {True, 34, 40, 'male', 'abc'}

        ===================================================================================================================================
        
        // The set() Constructor //
        // It is also possible to use the set() constructor to make a set.

        // Contoh:
        // Using the set() constructor to make a set:
           thisset = set(("apple", "banana", "cherry"))

           print (thisset)
           # Note: the set list is unordered, so the result will display the items in a random order.

        // output:
           {'apple', 'cherry', 'banana'}

        ===================================================================================================================================
        
        // Python - Access Set Items //
        // Access Items //
        // You cannot access items in a set by referring to an index or a key.
        // But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

        // Contoh :
        // Loop through the set, and print the values:
           thisset = {"apple", "banana", "cherry"}

           for x in thisset:
             print(x)
           
        // output:
           banana
           apple
           cherry

        // ini adalah contoh perulangan dari set 
        
        // Contoh :
        // Check if "banana" is present in the set:
           thisset = {"apple", "banana", "cherry"}

           print("banana" in thisset)
        
        // Output : 
           True
        
        // Simplenya, apakah banana ada di thisset? jika ada akan terprint True jika tidak ada akan
        // terprint False
        
        // Change Items //
        // Once a set is created, you cannot change its items, but you can add new items.
        
        ===================================================================================================================================
        
        // Python - Add Set Itmes //
        // Add Items
        // Once a set is created, you cannot change its items, but you can add new items.
        // To add one item to a set use the add() method.

        // Contoh :
        // Add an item to a set, using the add() method:
           thisset = {"apple", "banana", "cherry"}

           thisset.add("orange")

           print(thisset)

        // Output :
           {'banana', 'orange', 'apple', 'cherry'}

        // contoh diatas adalah cara untuk menambahkan item pada set.

        #===================================================================================================================================
        
        // Add Sets //
        // To add items from another set into the current set, use the update() method.

        // Contoh:
        // Add elements from tropical and thisset into newset:
           thisset = {"apple", "banana", "cherry"}
           tropical = {"pineapple", "mango", "papaya"}

           thisset.update(tropical)

           print(thisset)

        // output :
           {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

        // contoh diatas adalah cara untuk menambahkan sets tropical kedalam thisset
        
        #===================================================================================================================================
        
        // Add Any Iterable //
        // The object in the update() method does not have be a set, it can be any iterable object (tuples, lists, dictionaries et,).

        // Contoh :
        // Add elements of a list to at set:
           thisset = {"apple", "banana", "cherry"}
           mylist = ["kiwi", "orange"]

           thisset.update(mylist)

           print(thisset)

        // Output : 
           {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

        // Simplenya kita juga bisa menambahkan seperti list, dict, tuple dan lain-lain

        #===================================================================================================================================
        
        // Python - Remove Set Items //

        // Remove Item //
        // To remove an item in a set, use the remove(), or the discard() method.

        // Contoh remove() :
        // Remove "banana" by using the remove() method:
           thisset = {"apple", "banana", "cherry"}

           thisset.remove("banana")

           print(thisset)

        // output : 
           {'cherry', 'apple'}

        // Contoh discard() :
        // Remove "banana" by using the discard() method:
           thisset = {"apple", "banana", "cherry"}

           thisset.discard("banana")

           print(thisset)
        
        // output : 
           {'cherry', 'apple'}

        // Note: If the item to remove does not exist, discard() will NOT raise an error.
        // dari kedua contoh diatas hasilnya sama aja TAPI, jika menggunakan discard() apabila itemnya tidak sama atau tidak ada
        // tidak akan terjadi error. Berbeda dengan remove() jika items yang ingin dihapus beda atau tidak ada dalam set
        // maka akan terjadi error.
        
        // You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that 
        // sets are unordered, so you will not know what item that gets removed.
        // The return value of the pop() method is the removed item.
        
        // Contoh pop() : 
        // Remove the last item by using the pop() method:
           thisset = {"apple", "banana", "cherry"}

           x = thisset.pop()

           print(x) #removed item

           print(thisset) #the set after removal

        // Output : 
           apple
           {'cherry', 'banana'}
        
        // Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
        // simplenya. pop() digunakan untuk menghapus dari item terakhir dan perlu diingat dalam study kasus kali ini
        // kita sedang menggunakan set jadi akan mengacak urutannya dan kita tidak mengetahuinya.
        
        // Contoh clear() :
        // The clear() method empties the set:
           thisset = {"apple", "banana", "cherry"}

           thisset.clear()

           print(thisset)

        // output :
           set()
        
        // simplenya, clear() digunakan untuk menghapus semua set dithisset sehingga outputnya kosong
        
        // Contoh del :
        // The del keyword will delete the set completely:
           thisset = {"apple", "banana", "cherry"}

           del thisset

           print(thisset) #this will raise an error because the set no longer exists

        // Output :
           Error
       
        // Akan terjadi error karena dia menghapus thisset yang artinya thusset tidak ada lagi
        
        #===================================================================================================================================
        
        // join sets //

        // Join Two Sets //
        // There are several ways to join two or more sets in Python.
        // You can use the union() method that returns a new set containing all items from both sets, 
        // or the update() method that inserts all the items from one set into another:
 
        // Contoh union() :
        // The union() method returns a new set with all items from both sets:
           set1 = {"a", "b" , "c"}
           set2 = {1, 2, 3}

           set3 = set1.union(set2)
           print(set3)

        // Output : 
           {3, 'b', 1, 'c', 'a', 2}

        // simplenya, pada kasus diatas dia membuat set baru set3 dengan menambahkan semua items dari kedua set
        
        // Contoh update() :
        // The update() method inserts the items in set2 into set1:
           set1 = {"a", "b" , "c"}
           set2 = {1, 2, 3}

           set1.update(set2)
           print(set1)

        // Output :
           {2, 'c', 'b', 'a', 1, 3}

        // simplenya, set1.update(set2) set2 disisipkan atau ditaruh ke set1
        
        // Note: Both union() and update() will exclude any duplicate items.
        // Catatan: Baik union() dan update() akan mengecualikan item duplikat.
        
        #===================================================================================================================================
        
        // Keep ONLY the Duplicates //

        // The intersection_update() method will keep only the items that are present in both sets.
        // Contoh :
        // Keep the items that exist in both set x, and set y:
           x = {"apple", "banana", "cherry"}
           y = {"google", "microsoft", "apple"}

           x.intersection_update(y)

           print(x)

        // Output :
           {'apple'}

        // Simplenya, x.intersection_update(y) dia akan mengprint items jika items tersebut ada dikedua set x dan set y
        // contoh diatas terdapat apple di set x dan set y maka dia akan diprint.

        // The intersection() method will return a new set, that only contains the items that are present in both sets.
        // Contoh :
        // Return a set that contains the items that exist in both set x, and set y:
           x = {"apple", "banana", "cherry"}
           y = {"google", "microsoft", "apple"}

           z = x.intersection_update(y)

           print(z)
           
        // Output :
           {'apple'}
        
        // sama seperti kasus sebelumnya cuma, z = x.intersection_update(y) dia membuat simplenya set baru

        #===================================================================================================================================
        
        // Keep All, But NOT the Duplicates //
        // The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

        // Contoh :
        // Keep the items that are not present in both sets:
           x = {"apple", "banana", "cherry"}
           y = {"google", "microsoft", "apple"}

           x.symmetric_difference_update(y)

           print(x)

        // output :
           {'google', 'banana', 'microsoft', 'cherry'}

        // simplenya, x.symmetric_difference_update(y) dia akan mengeluarkan output hanya item yang tidak sama di kedua set x dan set y,
        // apple terdapat dikedua set x dan set y, jadi yang diprint adalah selain items apple, yang menghasilkan output diatas.
        // 

        #===================================================================================================================================
        
        // Python - Set Methods // 
        // Set Methods //
        // Python has a set of built-in methods that you can use on sets.
           
            Method	               Description

            add()	                  Adds an element to the set
            clear()	               Removes all the elements from the set
            copy()	               Returns a copy of the set
            difference()	         Returns a set containing the difference between two or more sets
            difference_update()	   Removes the items in this set that are also included in another, specified set
            discard()	            Remove the specified item
            intersection()	         Returns a set, that is the intersection of two other sets
            intersection_update()	Removes the items in this set that are not present in other, specified set(s)
            isdisjoint()	         Returns whether two sets have a intersection or not
            issubset()	            Returns whether another set contains this set or not
            issuperset()	         Returns whether this set contains another set or not
            pop()	                  Removes an element from the set
            remove()	               Removes the specified element
            symmetric_difference()	Returns a set with the symmetric differences of two sets
            symmetric_difference_update()	inserts the symmetric differences from this set and another
            union()	               Return a set containing the union of sets
            update()	               Update the set with the union of this set and others
        
        ===================================================================================================================================
===========================================================================================================================================
/// 29 ///
/// Python Classes, OOP and Objects ///
        ===================================================================================================================================

        // Python Classes / Objects //
        // Python is an object oriented programming language.
        // Almost everything in Python is an object, with its properties and methods.
        // A Class is like an object constructor, or a "blueprint" for creating objects.
        
        ===================================================================================================================================
        
        // Create a Class //
        // To create a class, use the keyword class:
        // Contoh : 
        // Create a class named MyClass, with a property named x:
           class MyClass:
               x = 5

           print(MyClass) 

        // Output : 
           <class '__main__.MyClass'>

        #===================================================================================================================================
        
        // Create Object //
        // Now we can use the class named MyClass to create objects:
        // Contoh :
        // Create an object named p1, and print the value of x:
           class MyClass:
              x = 5

           p1 = MyClass()
           print(p1.x)

        // Output : 
           5

        ===================================================================================================================================
        
        // The __init__() Function //
        // Contoh di atas adalah kelas dan objek dalam bentuk yang paling sederhana, dan tidak terlalu berguna dalam aplikasi kehidupan nyata.
        // Untuk memahami arti dari kelas kita harus memahami fungsi built-in __init __ ().
        // Semua kelas memiliki fungsi yang disebut __init __ (), yang selalu dijalankan saat kelas sedang dimulai.
        // Gunakan fungsi __init __ () untuk menetapkan nilai ke properti objek, atau operasi lain yang perlu dilakukan saat objek sedang dibuat:
        // Contoh :
        // Create a class named Person, use the __init__() function to assign values for name and age:
           class Person:
              def __init__(self, name, age):
                  self.name = name
                  self.age = age

           p1 = Person("John", 36)

           print(p1.name)
           print(p1.age)

        // Output : 
           John
           36

        // Note: The __init__() function is called automatically every time the class is being used to create a new object.
        
        ===================================================================================================================================
        
        // Object Methods //
        // Objects can also contain methods. Methods in objects are functions that belong to the object.
        // Let us create a method in the Person class:
        // Contoh :
        // Insert a function that prints a greeting, and execute it on the p1 object:
           class Person:
           def __init__(self, name, age):
               self.name = name
               self.age = age

           def myfunc(self):
               print("Hello my name is " + self.name)

           p1 = Person("John", 36)
           p1.myfunc()
        
        // Output :
           Hello my name is John

        #===================================================================================================================================
        
        // Contoh lain dengan input() :
           class orang:
           def __init__(self, nama, pacar):
               self.nama = nama
               self.pacar = pacar

           def myfunc(self):
               print ("Welcome {} and {}". format(self.nama, self.pacar))
           
           # Input
           x = input("Nama Kamu : ")
           y = input("Pacar Kamu : ")

           p1 = orang(x, y)
           p1.myfunc()    

        // Output : sesuai dengan yang kalian input
        
        // Note: The self parameter is a reference to the current instance of the class, and is used to access variables 
        // that belong to the class.
        
        ===================================================================================================================================
        
        // The self Parameter //
        // The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        // It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
        // Contoh :
        // Use the words mysillyobject and abc instead of self:
           class Person:
           def __init__(mysillyobject, name, age):
               mysillyobject.name = name
               mysillyobject.age = age

           def myfunc(abc):
               print("Hello my name is " + abc.name)

           p1 = Person("John", 36)
           p1.myfunc()

        // Output :
           Hello my name is John
           
        // Kita gak harus make self untuk memanggilnya.

        ===================================================================================================================================

        // Modify Object Properties //
        // You can modify properties on objects like this:
        // Contoh :
        // Set the age of p1 to 40:
           class Person:
              def __init__(self, name, age):
                  self.name = name
                  self.age = age

              def myfunc(self):
                  print("Hello my name is {} and my age {}". format(self.name, self.age))

           p1 = Person("John", 36)
           p1.age = 40 # <----
           p1.myfunc()

        // Output : 
           Hello my name is John and my age 40

        ===================================================================================================================================
        
        // Delete Object Properties //
        // You can delete properties on objects by using the del keyword:
        // Contoh :
        // Delete the age property from the p1 object:
           class Person:
              def __init__(self, name, age):
                  self.name = name
                  self.age = age

              def myfunc(self):
                  print("Hello my name is {}". format(self.name))
                  print("My age {}". format(self.age))

           p1 = Person("John", 36)
           del p1.age
           p1.myfunc()

        // Output : 
           Hello my name is John
           AttributeError: 'Person' object has no attribute 'age'

        // pada kasus diatas dia hanya bisa menggelurkan output nama, karena age telah dihapus.
        
        ===================================================================================================================================
        
        // The pass Statement //
        // class definitions cannot be empty, but if you for some reason have a class definition with no content, 
        // put in the pass statement to avoid getting an error.
        // Contoh :
           class Person:
             pass

        // Output : 
           Empty / kosong

        // having an empty class definition like this, would raise an error without the pass statement

        ===================================================================================================================================
===========================================================================================================================================
/// 30 ///
/// Python Inheritance ///
        ===================================================================================================================================

        // Python Inheritance //
        // Inheritance allows us to define a class that inherits all the methods and properties from another class.
        // Parent class is the class being inherited from, also called base class.
        // Child class is the class that inherits from another class, also called derived class.

        ===================================================================================================================================
        
        // Create a Parent Class //
        // Any class can be a parent class, so the syntax is the same as creating any other class:
        // Contoh : 
        // Create a class named Parent, with firstname and lastname properties, and a printname method:
           class Parent:
               def __init__(self, fname, lname):
                  self.firstname = fname
                  self.lastname = lname

               def printname(self):
                  print(self.firstname, self.lastname)

           #Use the Person class to create an object, and then execute the printname method:
           x = Parent("John", "Doe")
           x.printname()

        // Output : 
           John Doe

        ===================================================================================================================================
        
        // Create a Child Class //
        // To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
        // Contoh :
        // Create a class named Child, which will inherit the properties and methods from the Parent class:
           class Child(Parent):
              pass

        // Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

        // Now the Child class has the same properties and methods as the Parent class.
        // Contoh :
        // Use the Child class to create an object, and then execute the printname method:
           class Parent:
             def __init__(self, fname, lname):
               self.firstname = fname
               self.lastname = lname

             def printname(self):
               print(self.firstname, self.lastname)

           class Child(Person): # <--- 
             pass

           x = Child("Kisah", "Tegar") # <---
           x.printname()

        // Output :
           Kisah Tegar

        ===================================================================================================================================
        
        // Add the __init__() Function //
        // Sejauh ini kita telah membuat kelas anak yang mewarisi properti dan metode dari induknya.
        // kita ingin menambahkan fungsi __init__() ke kelas anak (bukan kata kunci pass).

        #===================================================================================================================================
        // Note: Fungsi __init__() dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.
        #===================================================================================================================================

        // Contoh :
        // Add the __init__() function to the Child class:
           class Child(Person):
             def __init__(self, fname, lname):
               #add properties etc.

        // Saat Anda menambahkan fungsi __init__(), kelas anak tidak akan lagi mewarisi fungsi __init__() induknya.
        #===================================================================================================================================
        // Note: Fungsi __init__() anak menggantikan pewarisan fungsi __init__() induk.
        #===================================================================================================================================

        // Untuk mempertahankan warisan fungsi __init__ () induk, tambahkan panggilan ke fungsi __init__() induk:
        
        // Contoh : 
           class Parent:
               def __init__(self, fname, lname):
                  self.firstname = fname
                  self.lastname = lname

               def printname(self):
                  print(self.firstname, self.lastname)

           class Child(Person):                            # <---
               def __init__(self, fname, lname):           # <---
                  Person.__init__(self, fname, lname)      # <---

           x = Child("Mike", "Olsen")
           x.printname()

        // Output : 
           Mike Olsen

        // Sekarang kita telah berhasil menambahkan fungsi __init__(), dan mempertahankan warisan dari kelas induk, 
        // dan kita siap untuk menambahkan fungsionalitas dalam fungsi __init__().
        
        ===================================================================================================================================

        // Use the super() Function //
        // Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
        // Contoh :
           class Parent:
             def __init__(self, fname, lname):
               self.firstname = fname
               self.lastname = lname

             def printname(self):
               print(self.firstname, self.lastname)

           class Child(Person):
             def __init__(self, fname, lname):
               super().__init__(fname, lname)

           x = Child("Mike", "Olsen")
           x.printname()

        // Output : 
           Mike Olsen

        // Dengan menggunakan fungsi super (), Anda tidak harus menggunakan nama elemen induk, 
        // itu akan secara otomatis mewarisi metode dan properti dari induknya.

        // Add Properties //
        // Contoh :
        // Add a property called graduationyear to the Student class:
           class Parent:
             def __init__(self, fname, lname):
               self.firstname = fname
               self.lastname = lname

             def printname(self):
               print(self.firstname, self.lastname)

           class Child(Parent):
             def __init__(self, fname, lname):
               super().__init__(fname, lname)
               self.graduationyear = 2019 # <---

           x = Child("Mike", "Olsen")
           x.printname()
           print(x.graduationyear)
        
        // Output : 
           Mike Olsen
           2019

        // Pada contoh di bawah, tahun 2019 harus berupa variabel, dan diteruskan ke kelas Siswa saat membuat objek siswa. 
        // Untuk melakukannya, tambahkan parameter lain dalam fungsi __init__ ():
        // Contoh : 
        // Add a year parameter, and pass the correct year when creating objects:
           class Parent:
             def __init__(self, fname, lname):
               self.firstname = fname
               self.lastname = lname

             def printname(self):
               print(self.firstname, self.lastname)

           class Child(Parent):
             def __init__(self, fname, lname, year): # <---
               super().__init__(fname, lname)
               self.graduationyear = year            # <---

           x = Child("Mike", "Olsen", 2019)
           x.printname()
           print(x.graduationyear)

        // Output :
           Mike Olsen
           2019
  
        // 
        ===================================================================================================================================
===========================================================================================================================================
/// 31 ///
/// Python Iterators ///
        ===================================================================================================================================

        // Python Iterators //
        // An iterator is an object that contains a countable number of values.
        // An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
        // Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

        // Iterator vs Iterable //
        // Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
        // All these objects have a iter() method which is used to get an iterator:

        // Contoh :
        // Return an iterator from a tuple, and print each value:
           mytuple = ("apple", "banana", "cherry")
           myit = iter(mytuple)

           print(next(myit))
           print(next(myit))
           print(next(myit))

        // Output :
           apple
           banana 
           cherry

        // Even strings are iterable objects, and can return an iterator: //
        // Contoh :
        // Strings are also iterable objects, containing a sequence of characters:
           mystr = "banana"
           myit = iter(mystr)

           print(next(myit))
           print(next(myit))
           print(next(myit))
           print(next(myit))
           print(next(myit))
           print(next(myit))

        // Output :
           b
           a
           n
           a
           n
           a

        ===================================================================================================================================
        
        // Looping Through an Iterator //
        // We can also use a for loop to iterate through an iterable object:
        // Contoh :
        // Iterate the values of a tuple:
           mytuple = ("apple", "banana", "cherry")

           for x in mytuple:
             print(x)

        // Output :
           apple
           banana
           cherry

        #===================================================================================================================================
        
        // Contoh :
        // Iterate the characters of a string:
           mystr = "banana"

           for x in mystr:
             print(x)

        // Output :
           b
           a
           n
           a
           n
           a
           
        // The for loop actually creates an iterator object and executes the next() method for each loop.

        ===================================================================================================================================
        
        // Create an Iterator //
        // To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
        // As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
        // The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
        // The __next__() method also allows you to do operations, and must return the next item in the sequence.

        // Contoh :
        // Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
           class mynumber:
               def __iter__(self):
                  self.a = 1
                  return self

               def __next__(self):
                  x = self.a
                  self.a +=1
                  return x

           myclass = mynumber()
           myiter = iter(myclass)

           print(next(myiter))
           print(next(myiter))
           print(next(myiter))
           print(next(myiter))
           print(next(myiter))

        // Output :
           1
           2
           3
           4
           5

        ===================================================================================================================================
        
        // StopIteration //
        // The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
        // To prevent the iteration to go on forever, we can use the StopIteration statement.
        // In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

        // Contoh :
        // Stop after 20 iterations:
           class mynumber:
               def __iter__(self):
                  self.a = 1
                  return self

               def __next__(self):
                  if self.a <= 20:
                       x = self.a
                       self.a +=1
                       return x
                  else:
                       raise StopIteration

           myclass = mynumber()
           myiter = iter(myclass)

           for x in myclass:
              print (x)
        
        // Output :
           1
           2
           3
           4
           5
           6
           7
           8
           9
           10
           11
           12
           13
           14
           15
           16
           17
           18
           19
           20

        ===================================================================================================================================
===========================================================================================================================================
/// 32 ///
/// Python Scope ///
        ===================================================================================================================================
        // A variable is only available from inside the region it is created. This is called scope.

        ===================================================================================================================================
        
        // Local Scope //
        // A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
        // Contoh :
        // A variable created inside a function is available inside that function:
           def myfunc():
              x = 300
              print(x)

           myfunc()

        // Output :
           300

        ===================================================================================================================================
        
        // Function Inside Function //
        // As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
        // Contoh :
        // The local variable can be accessed from a function within the function:
           def myfunc():
             x = 300
             def myinnerfunc():
               print(x)
             myinnerfunc()

           myfunc()

        // Output :
           300

        ===================================================================================================================================
        
        // Global Scope //
        // A variable created in the main body of the Python code is a global variable and belongs to the global scope.
        // Global variables are available from within any scope, global and local.
        // Contoh :
        // A variable created outside of a function is global and can be used by anyone:
           x = 300

           def myfunc():
             print(x)

           myfunc()

           print(x)

        // Output :
           300
           300

        ===================================================================================================================================

        // Naming Variables //
        // If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
        // Contoh :
        // The function will print the local x, and then the code will print the global x:
           x = 300

           def myfunc():
             x = 200
             print(x)

           myfunc()

           print(x)

        // Output :
           200
           300

        ===================================================================================================================================

        // Global Keyword //
        // If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
        // The global keyword makes the variable global.

        // Contoh :
        // If you use the global keyword, the variable belongs to the global scope:
           def myfunc():
             global x
             x = 300

           myfunc()

           print(x)

        // Output :
           300

        // Also, use the global keyword if you want to make a change to a global variable inside a function.
        // Contoh :
        // To change the value of a global variable inside a function, refer to the variable by using the global keyword:
           x = 300

           def myfunc():
             global x
             x = 200

           myfunc()

           print(x)

        // Output :
           200

        ===================================================================================================================================
===========================================================================================================================================
/// 33 ///
/// Python Modules ///
        ===================================================================================================================================

        // What is a Module? //
        // Consider a module to be the same as a code library.
        // A file containing a set of functions you want to include in your application.

        ===================================================================================================================================

        // Create a Module //
        // To create a module just save the code you want in a file with the file extension .py:

        // Contoh :
        // Save this code in a file named mymodule.py
           def greeting(name):
             print("Hello, " + name)

        #===================================================================================================================================
 
        // Use a Module //
        // Now we can use the module we just created, by using the import statement:
        // Contoh :
        // Import the module named mymodule, and call the greeting function:
           import mymodule

           mymodule.greeting("Jonathan")

        // Output :
           Hello Jonathan 

        // Note: When using a function from a module, use the syntax: module_name.function_name.

        ===================================================================================================================================

        // Variables in Module
        // The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
        // Contoh :
        // Save this code in the file mymodule.py
           person1 = {
               "name": "John",
               "age": 36,
               "country": "Norway"
           }

        // Contoh :
        // Import the module named mymodule, and access the person1 dictionary:
           import mymodule

           a = mymodule.person1["age"]
           print(a)

        // Output :
           36

        ===================================================================================================================================

        // Naming a Module //
        // You can name the module file whatever you like, but it must have the file extension .py

        ===================================================================================================================================

        // Re-naming a Module //
        // You can create an alias when you import a module, by using the as keyword:

        // Contoh :
        // Create an alias for mymodule called mx:
           import mymodule as mx

           a = mx.person1["age"]
           print(a)

        // mymodule sebagai mx

        ===================================================================================================================================

        // Built-in Modules //
        // There are several built-in modules in Python, which you can import whenever you like.

        // Contoh :
        // Import and use the platform module:
           import platform

           x = platform.system()
           print(x)

        // Output :
           windows #karena saya sedang menggunakan windows

        ===================================================================================================================================

        // Using the dir() Function //
        // There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

        // Contoh :
        // List all the defined names belonging to the platform module:
           import platform

           x = dir(platform)
           print(x)

        // Output :
           ['_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages',
           'architecture', 'collections', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']
        
        // beda computer beda output biasanya
        #===================================================================================================================================
        // Note: The dir() function can be used on all modules, also the ones you create yourself.
        #===================================================================================================================================

        ===================================================================================================================================

        // Import From Module //
        // You can choose to import only parts from a module, by using the from keyword.
        // Contoh :
        // The module named mymodule has one function and one dictionary:
           def greeting(name):
             print("Hello, " + name)

           person1 = {
             "name": "John",
             "age": 36,
             "country": "Norway"
           }

        // Contoh :
        // Import only the person1 dictionary from the module:
           from mymodule import person1

           print (person1["age"])

        // Output : 
           36

        ===================================================================================================================================
===========================================================================================================================================
/// 36 ///
/// datetime ///
        ===================================================================================================================================

        // Python Dates //
        // A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
        // Contoh:
        // Import the datetime module and display the current date:
           import datetime

           x = datetime.datetime.now()
           print(x)

        // Output :
           2020-11-26 13:24:24.601609

        ===================================================================================================================================

        // Date Output //
        // When we execute the code from the example above the result will be:
        // 2020-11-26 09:44:10.198611
        // The date contains year, month, day, hour, minute, second, and microsecond.
        // The datetime module has many methods to return information about the date object.
        // Here are a few examples, you will learn more about them later in this chapter:
        // Contoh:
        // Return the year and name of weekday:
           import datetime

           x = datetime.datetime.now()

           print(x.year)
           print(x.strftime("%A"))

        // Output :
           2020
           Thursday

        // Creating Date Objects //
        // To create a date, we can use the datetime() class (constructor) of the datetime module.
        // The datetime() class requires three parameters to create a date: year, month, day.
        // Contoh :
        // Create a date object:
           import datetime

           x = datetime.datetime(2020, 5, 17)

           print(x)

        // Output :
           2020-05-17 00:00:00

        // The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
        // but they are optional, and has a default value of 0, (None for timezone). 

        ===================================================================================================================================

        // The strftime() Method //
        // The datetime object has a method for formatting date objects into readable strings.
        // The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
        // Contoh :
        // Display the name of the month:
           import datetime

           x = datetime.datetime(2018, 6, 1)

           print(x.strftime("%B"))

        // Output :
           June

            A reference of all the legal format codes:

            Directive	Description	                                                          Example	
            %a	         Weekday, short version	                                                Wed	
            %A	         Weekday, full version	                                             Wednesday	
            %w	         Weekday as a number 0-6, 0 is Sunday	                                  3	
            %d	         Day of month 01-31	                                                   31	
            %b	         Month name, short version	                                             Dec	
            %B	         Month name, full version	                                          December	
            %m	         Month as a number 01-12	                                                12	
            %y	         Year, short version, without century	                                 18	
            %Y	         Year, full version	                                                  2018	
            %H	         Hour 00-23	                                                            17	
            %I	         Hour 00-12	                                                            05	
            %p	         AM/PM	                                                                  PM	
            %M	         Minute 00-59	                                                         41	
            %S	         Second 00-59	                                                         08	
            %f	         Microsecond 000000-999999	                                           548513	
            %z	         UTC offset	                                                          +0100	
            %Z	         Timezone	                                                               CST	
            %j	         Day number of year 001-366	                                             365	
            %U	         Week number of year, Sunday as the first day of week, 00-53	            52	
            %W	         Week number of year, Monday as the first day of week, 00-53	            52	
            %c	         Local version of date and time	                              Mon Dec 31 17:41:00 2018	
            %x	         Local version of date	                                             12/31/18	
            %X	         Local version of time	                                             17:41:00	
            %%	         A % character	                                                         %	

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
/// Python Math ///
        ===================================================================================================================================

        // Python has a set of built-in math functions, including an extensive math module, 
        // that allows you to perform mathematical tasks on numbers.

        // Built-in Math Functions //
        // The min() and max() functions can be used to find the lowest or highest value in an iterable:
        // Example :
           x = min(5, 10, 25)
           y = max(5, 10, 25)

           print(x)
           print(y)

        // Output : 
           5
           25

        // angka minimal x = 5 dan angka maximal y = 25
        
        #===================================================================================================================================

        // The abs() function returns the absolute (positive) value of the specified number: //
        // Example :
           x = abs(-7.25)

           print(x)

        // Output :
           7.25

        // abs() mengubah negatif menjadi positif pada contoh diatas.

        #===================================================================================================================================

        // The pow(x, y) function returns the value of x to the power of y (xy) //
        // Example :
        // Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
           x = pow(4, 3)

           print(x)

        // Output :
           64

        // simplenya pow() 4 pangkat 3 hasilnya 64 
        
        ===================================================================================================================================

        // The Math Module //
        // Python has also a built-in module called math, which extends the list of mathematical functions.
        // To use it, you must import the math module:
           import math

        // When you have imported the math module, you can start using methods and constants of the module.
        // The math.sqrt() method for example, returns the square root of a number:
        // Example :
           import math

           x = math.sqrt(64)

           print(x)

        // Output :
           8.0

        // The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method 
        // rounds a number downwards to its nearest integer, and returns the result:
        // Example :
           #Import math library
           import math

           #Round a number upward to its nearest integer
           x = math.ceil(1.4)

           #Round a number downward to its nearest integer
           y = math.floor(1.4)

           print(x)
           print(y)

        // Output : 
           2
           1
        
        // The math.pi constant, returns the value of PI (3.14...):
        // Example :
           import math

           x = math.pi

           print(x)

        // Output :
           3.141592653589793


        ===================================================================================================================================
===========================================================================================================================================
/// 35 ///
/// Door Game ///
        ===================================================================================================================================

        import random
        import os

        def doorgame():
            life = 5
            while life > 0:
               os.system("cls")
               door = random.randint(1,5)
               print("=====================================================================")
               print("|                            Door: {}                               |". format(door))
               print("|                            Life: {}                               |". format(life))
               print("=====================================================================")
               life -= 1
               # Guess
               guess = int(input("| Dari ke-{} pintu yang ada, pilih pintu yang menurut kamu benar: ". format(door)))
               print("=====================================================================")
               # Check guess
               if guess != door:
                     if life > 0:
                        input("==> Pilihan Kamu salah. Coba Lagi...")
                        continue
                     else:
                        print("==> Kamu kehilangan semua nyawa. Pintu yang benar adalah pintu ke-{}". format(str(door)))
                        print("=============================")
                        print("| Terimakasih sudah bermain |\n| Sampai jumpa kembali      |")
                        print("=============================")
                        print("=====================================================================")
                        break
               else:
                     print("==> kamu berhasil melewati pintu ke-{}".format(str(door)))
               # Ask play again or no?
               print("==> Apakah kamu ingin melanjutkan game lagi?")
               lagi = input("==> Iya atau Tidak [y/n]: ")
               if lagi == "y":
                     print("==> Game dilanjutkan dan nyawa dipenuhkan")
                     life = 5
               elif lagi == "n":
                     print("==> Game berakhir")
                     life = 0
               else:
                     print("==> Kamu salah input")
                     life = 0
            else:
               print("=============================")
               print("| Terimakasih sudah bermain |\n| Sampai jumpa kembali      |")
               print("=============================")
               print("=====================================================================")
        # Eksekusi
        doorgame()

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================
/// 34 ///
///  ///
        ===================================================================================================================================

        // 

        ===================================================================================================================================
===========================================================================================================================================