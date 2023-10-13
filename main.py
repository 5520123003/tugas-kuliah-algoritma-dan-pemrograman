# membuat program
import os
import time
print(F"{'MEMBUAT TUGAS':^50} ")
print(F"{'ALGORITMA DAN PEMROGRAMAN':^50} ")

print(50*'=')

while True:   # while loop-------------------------------------
    User = "clone"
    Sandi = "ze123"
    waktu = time.time()

    print(50 * '-')
    Username = input(f"{'[+] Masukkan Username ':^10}: ")
    Password = str(input(f"{'[+] Masukkan password ':^10}: "))
    print(50 * '-')

# 1. kondisi pertama menggunakan (if)
    #-------------------------------------------------
    if Username + Password == User + Sandi:
        print("TERIMAKASI ANDA TELAH LOGIN !!")
        print('\n\n')

        so = input("Tekan Enter untuk Masuk kehalaman Selanjutnya   ")
        print(50*'-')
        if so == "Enter":
            continue

        print(f"\n{'SELAMAT DATANG':^50}")
        print(f"{'DIDUNIA TIPU-TIPU':^50}")
        print(50 * '=')
        print("             today",waktu)
        print(50*'-')

        print('\n')
        ej = input()
        if ej == "Enter":
            print('\n')
            print(f"{'loading...':^40}")
        while True:

            print("                   .===.                ")
            print("                   |   |                ")
            print("                   |---|                ")
            print("                   |   |                ")
            print("                   |---|                ")
            print("           __  __  |   |                ")
            print("          /--|/--\ |---| ---            ")
            print("         /   |    ||   ||----\          ")
            print("        /|---|----||   ||\    \         ")
            print("       / |   |    ||   || |---|\        ")
            print("        \(   )(   )|   |  (   ) ||      ")
            print('\n')
            is_done = input("apakah sudah selesai ? (y/n) ")
            dj = input()
            if is_done or dj== 'y':
                break

            elif is_done == 'n':
                print("login Kembali...")


            print(50 * '-')


# 2. kondisi kedua menggunakan (elif)
    elif Username or Password == User and Sandi:
        print("Mohon Maaf Username dan password yang anda masukkan salah ")
        print('\n')
        is_done = input("apakah ingin coba lagi ? (y/n) ")
        if is_done == 'n':
            break


# 3. kemudian yang ketiga kondisi menggunakan (else)
    else:
        print("\n Selamat Mencoba Kembali!!")
        is_done = input("apakah ingin coba lagi ? (y/n) ")
        if is_done == "n":
            break


print(50*'-')
print(f"{'Program Selesai....':^20}")























































