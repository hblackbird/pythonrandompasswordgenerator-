import string,random,sys
def sifreolusturucu():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "abcdefghijklmnopqrstuvwxyz1234567890"
    c = "abcdefghijklmnopqrstuvwxyz1234567890!#@.,$'"
    d = "1234567890"
    e = "1234567890'!#@.,$"
    sayi = input("Parolanın içerisinde sayı olsun mu? [E/H]").upper()
    harf = input("Parolanın içerisinde harf olsun mu? [E/H]").upper()
    ozel = input("Parolanın içerisinde ozel karakter olsun mu? [E/H]").upper()
    uzunluk1 = int(input("Parola minimum kac karakter uzunlukta olacak ?"))
    uzunluk_2 = int(input("Parola maximum kac karakter uzunlukta olacak ?"))
    uzunluk = random.randint(uzunluk1,uzunluk_2)
    if sayi == "E"  and harf == "E" and ozel == "E":
        if uzunluk <=43:
            p = "".join(random.sample(c,uzunluk))
            print("Sifreniz :", p)
        elif uzunluk >43:
            print("Uzunluk sinirini astiniz !")
    elif sayi == "E" and harf == "E" and ozel == "H":
        if uzunluk <=36:
            p = "".join(random.sample(b, uzunluk))
            print("Sifreniz :", p)
        elif uzunluk >36:
            print("Uzunluk sinirini astiniz !")
    elif sayi == "E" and harf == "H" and ozel == "H":
        if uzunluk <= 10:
            p = "".join(random.sample(d, uzunluk))
            print("Sifreniz :", p)
        elif uzunluk >10:
            print("Bu uzunlukta sadece sayi sifresi uretemezsiniz!")
    elif sayi == "H" and harf == "E" and ozel == "H":
        if uzunluk <=26:
            p = "".join(random.sample(a, uzunluk))
            print("Sifreniz :", p)
        elif uzunluk >26:
            print("Uzunluk sinirini astiniz !")
    elif sayi == "E" and harf == "H" and ozel == "E":
        if uzunluk <=17:
            p = "".join(random.sample(e, uzunluk))
            print("Sifreniz :", p)
        elif uzunluk >17:
            print("Uzunluk sinirini astiniz !")
    elif sayi == "H" and harf == "H" and ozel == "H":
        print("Yazılacak bir şey kalmadı :)")
    else :
        print("Bir şeyler yanlış oldu sanki")


sifreolusturucu()