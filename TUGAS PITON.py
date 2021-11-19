class main():
    def menu():
        print("\t************************************************************")
        print("\t|                  W E L C O M E   T O                     |")
        print("\t|                  T O K O   R E T A I L                   |")
        print("\t************************************************************")
        print("\t|              !! O U R   P R O D U C T S!!                |")
        print("\t| 1. Sabun Cuci Piring                                     |")
        print("\t| 2. Margarin                                              |")
        print("\t| 3. Beras                                                 |")
        print("\t| 4. Minyak Goreng                                         |")
        print("\t| 5. EXIT APPLICATION                                      |")
        print("\t************************************************************")

    def lobby():

        main.menu()
        pilih = input("\t Choose Your Item: ")
        pilih2 = int(input("\t How much item you want to buy : "))
        i = 0
        while i != pilih2 :
            if pilih == 1:
                barang.barang1()
            elif pilih == 2 :
                barang.barang2()
            elif pilih == 3:
                barang.barang3()
            elif pilih == 4:
                barang.barang4()
            elif pilih == 5:
                exit()
            else:
                print("\t!!!!YOUR CHOOSE IS NOT VALID!!!!")
                print("\t!!!!PLEASE ENTER THE CORRECT NUMBER!!!!")
                main.lobby()


class barang () :
    def barang1(sabun= 2500) :
        kuantitas =int(input("Quantity :"))
        payment1 = kuantitas * sabun
        print("----------------------------")
        print("        TOKO RECEIPT       ")
        print("-" * 25)
        print("Your Item : Sabun ")
        print(" Quantity : ",kuantitas)
        print("Your Have {} item : ".format(len(item)))
        for it in item:
            print("-{} ".format(it))
            print(payment1)




    def barang2(margarin = 8500) :
        kuantitas =int(input("Quantity :"))
        payment2 = kuantitas * margarin
        print("----------------------------")
        print("        TOKO RECEIPT       ")
        print("-" * 25)
        print("Your Item : Margarin ")
        print(" Quantity : ",kuantitas)
        print("Your Have {} item : ".format(len(item)))
        for it in item:
            print("-{} ".format(it))
        b = payment2
        return b


    def barang3(beras = 20000) :
        kuantitas =int(input("Quantity :"))
        payment3 = kuantitas * beras
        print("----------------------------")
        print("        TOKO RECEIPT       ")
        print("-" * 25)
        print("Your Item : Beras ")
        print(" Quantity : ",kuantitas)
        print("Your Have {} item : ".format(len(item)))
        for it in item:
            print("-{} ".format(it))
        d=payment3
        return d


    def barang4(minyak = 18000) :
        kuantitas =int(input("Quantity :"))
        payment4 = kuantitas * minyak
        print("----------------------------")
        print("        TOKO RECEIPT       ")
        print("-" * 25)
        print("Your Item : Minyak ")
        print(" Quantity : ",kuantitas)
        print("Your Have {} item : ".format(len(item)))
        for it in item:
            print("-{} ".format(it))
        e = payment4
        return e


    def kalkulasi (a,b,d,e) :
        barang.barang1(a)
        barang.barang2(b)
        barang.barang3(d)
        barang.barang4(e)
        c = a + b + d + e
        return c



# main program

    pilih2 = int(input("\t How much item you want to buy : "))
    i=0
    item = []
    while i != pilih2 :
        i = i + 1
        main.menu()
        item_baru = input("\t Choose Your Item -{}: ")
        item.append(item_baru)
        if item_baru == 1 :
            barang.barang1()


        elif item_baru == 2 :
            barang.barang2()

        elif item_baru == 3:
            barang.barang3()

        elif item_baru == 4:
            barang.barang4()

        elif item_baru == 5:
            exit()
        else:
            print("\t!!!!YOUR CHOOSE IS NOT VALID!!!!")
            print("\t!!!!PLEASE ENTER THE CORRECT NUMBER!!!!")
            main.lobby()


