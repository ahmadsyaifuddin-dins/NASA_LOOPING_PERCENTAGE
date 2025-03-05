#KREDIT AHMAD SYAIFUDDIN
#Looping ini menggunakan Persentase ketika Berjalan menuju suatu nilai yg di inputkan User


import random
import os
import time
os.system('cls')

# Daftar kode yang bernilai True
kodes_benar = [10, 25, 50, 100, 110, 1000, 1114, 56999, 75000]

# Meminta pengguna memasukkan kode
kode_pengguna = int(input("Masukkan kode : "))

if kode_pengguna in kodes_benar:
    for i in range(1, kode_pengguna + 1):
        os.system('cls')
        progress = (i / kode_pengguna) * 100
        print("Process {:.0f}%".format(progress))
        time.sleep(0.7) 
        print()
    print("NASA HACKED")
else:
    for i in range(1, kode_pengguna + 1):
        os.system('cls')
        progress = (i / kode_pengguna) * 100
        print("Process {:.0f}%".format(progress))
        time.sleep(0.7) 
        print()
    print("HACKING FAILED")
