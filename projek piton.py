class main():
    def menu():
        print("\t**********************************************")
        print("\t|            W E L C O M E   T O             |")
        print("\t|                 M TIX                      |")
        print("\t**********************************************")
        print("\t|              !!NOW SHOWING!!               |")
        print("\t| 1. KUNTILANAK LONCAT                       |")
        print("\t| 2. POCONG NGESOT                           |")
        print("\t| 3. BALING-BALING BAMBU                     |")
        print("\t| 4. TERMINATOR                              |")
        print("\t| 5. EXIT APPLICATION                        |")
        print("\t**********************************************")

    def seat():
        print("\t-------------------------------------------")
        print("\t|                SCREEN                   |")
        print("\t| A1  A2  A3  A4  A5  A6  A7  A8  A9  A10 |")
        print("\t| B1  B2  B3  B4  B5  B6  B7  B8  B9  B10 |")
        print("\t| C1  C2  C3  C4  C5  C6  C7  C8  C9  C10 |")
        print("\t| D1  D2  D3  D4  D5  D6  D7  D8  D9  D10 |")
        print("\t| E1  E2  E3  E4  E5  E6  E7  E8  E9  E10 |")
        print("\t-------------------------------------------")


class film():
    def milih1():
        print("")
        print(film1)
        try:
            amount = int(input("\t Jumlah tiket : "))
            harga_tiket = 50000
            fee = 50000 * amount
        except ValueError:
            print("!!!PLEASE ENTER THE CORRECT AMOUNT!!!")
            film.milih1()
        kursi = []
        i = 0
        while (i != amount):
            i = i + 1
            main.seat()
            kursi_baru = input("Choose Your Seat {} : ".format(i))
            kursi.append(kursi_baru)
            print("------------------------------")
            print("         M-TIX RECEIPT        ")
            print("-" * 10)
            print("Your Movie: KUNTILANAK NGESOT ")
            print("Your Have {} Seat : ".format(len(kursi)))
            for st in kursi:
                print("-{} ".format(st))
            print("Pay : Rp ", fee)
        choose = input("Back To Menu?(Y/N):")
        if choose == "Y" or choose == "y":
            film.mainapp()
        elif choose == "N" or choose == "n":
            print("THANK YOU FOR USING OUR SERVICE")
            exit()
        else:
            print("your input is not valid")
            film.mainapp()

    def milih2():
        print("")
        print(film2)
        try:
            amount = int(input("\t Jumlah tiket : "))
            harga_tiket = 50000
            fee = 50000 * amount
        except ValueError:
            print("!!!PLEASE ENTER THE CORRECT AMOUNT!!!")
            film.milih2()
        kursi = []
        i = 0
        while i != amount:
            i = i + 1
            main.seat()
            kursi_baru = input("Choose Your Seat {} : ".format(i))
            kursi.append(kursi_baru)
            print("----------------------------")
            print("        M-TIX RECEIPT       ")
            print("-" * 20)
            print("Your Movie: POCONG LONCAT   ")
            print("Your Have {} Seat : ".format(len(kursi)))
            for st in kursi:
                print("-{} ".format(st))
            print("Pay : Rp ", fee)
        choose = input("Back To Menu?(Y/N):")
        if choose == "Y" or choose == "y":
            film.mainapp()
        elif choose == "N" or choose == "n":
            print("THANK YOU FOR USING OUR SERVICE")
            exit()
        else:
            print("your input is not valid")
            film.mainapp()

    def milih3():
        print("")
        print(film3)
        try:
            amount = int(input("\t Jumlah tiket : "))
            harga_tiket = 50000
            fee = 50000 * amount
        except ValueError:
            print("!!!PLEASE ENTER THE CORRECT AMOUNT!!!")
            film.milih3()
        kursi = []
        i = 0
        while i != amount:
            i = i + 1
            main.seat()
            kursi_baru = input("Choose Your Seat {} : ".format(i))
            kursi.append(kursi_baru)
            print("-------------------------------")
            print("         M-TIX RECEIPT         ")
            print("-" * 20)
            print("Your Movie: BALING-BALING BAMBU")
            print("Your Have {} Seat : ".format(len(kursi)))
            for st in kursi:
                print("-{} ".format(st))
            print("Pay : Rp ", fee)
        choose = input("Back To Menu?(Y/N):")
        if choose == "Y" or choose == "y":
            film.mainapp()
        elif choose == "N" or choose == "n":
            print("THANK YOU FOR USING OUR SERVICE")
            exit()
        else:
            print("your input is not valid")
            film.mainapp()

    def milih4():
        print("")
        print(film4)
        try:
            amount = int(input("\t Jumlah tiket : "))
            harga_tiket = 50000
            fee = 50000 * amount
        except ValueError:
            print("!!!PLEASE ENTER THE CORRECT AMOUNT!!!")
            film.milih4()
        i = 0
        kursi = []
        while i != amount:
            i = i + 1
            main.seat()
            kursi_baru = input("Choose Your Seat {} : ".format(i))
            kursi.append(kursi_baru)
            print("----------------------------")
            print("        M-TIX RECEIPT       ")
            print("-" * 20)
            print("Your Movie: Terminator")
            print("Your Have {} Seat : ".format(len(kursi)))
            for st in kursi:
                print("-{} ".format(st))
            print("Pay : Rp ", fee)

        choose = input("Back To Menu?(Y/N):")
        if choose == "Y" or choose == "y":
            film.mainapp()
        elif choose == "N" or choose == "n":
            print("THANK YOU FOR USING OUR SERVICE")
            exit()
        else:
            print("Your input is not valid")
            film.mainapp()

    def mainapp():
        # Main Program
        film1 = "\t          |  KUNTILANAK LONCAT |"
        film2 = "\t          |    POCONG NGESOT   |"
        film3 = "\t          | BALING-BALING BAMBU|"
        film4 = "\t          |     TERMINATOR     |"
        main.menu()
        try:
            pilih = int(input("\t Choose Your Movie: "))
        except ValueError:
            print("!!!PLEASE ENTER THE CORRECT NUMBER!!!")
            film.mainapp()
        if pilih == 1:
            film.milih1()
        elif pilih == 2:
            film.milih2()
        elif pilih == 3:
            film.milih3()
        elif pilih == 4:
            film.milih4()
        elif pilih == 5:
            exit()
        else:
            print("\t Your Choose Is Not Valid!!")
            print("\t!!!!PLEASE ENTER THE CORRECT NUMBER!!!!")
            film.mainapp()


# Main Program
film1 = "\t          |  KUNTILANAK LONCAT |"
film2 = "\t          |    POCONG NGESOT   |"
film3 = "\t          | BALING-BALING BAMBU|"
film4 = "\t          |     TERMINATOR     |"
main.menu()
try:
    pilih = int(input("\t Choose Your Movie: "))
except ValueError:
    print("!!!PLEASE ENTER THE CORRECT NUMBER!!!")
    film.mainapp()
if pilih == 1:
    film.milih1()
elif pilih == 2:
    film.milih2()
elif pilih == 3:
    film.milih3()
elif pilih == 4:
    film.milih4()
elif pilih == 5:
    exit()
else:
    print("\t!!!!YOUR CHOOSE IS NOT VALID!!!!")
    print("\t!!!!PLEASE ENTER THE CORRECT NUMBER!!!!")
    film.mainapp()

