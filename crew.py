defuser = "Crew" 
defkey = "CrewWas"

while (True):
    print("Hesabınız varmı? (var/yok)")
    cevap = input( )
    if (cevap == "var"):
        user = input("E-posta :")
        key = input("Şifre :")
        
        if (defuser == user) and (key == defkey):
            print("Hesaba başarılı bir şekilde erişim sağlandı.")
            break
        elif (defuser != user) and (key == defkey):
            print("Bu mail adresi sistemde kayıtlı değil.")
            print("G-mail adresinizi değiştirmek istermisiniz? (evet/hayır)")
            cevapa = input( )
            if (cevapa == "evet"):
                print("Lütfen bekleyin...")
                degisuser = input("G-mail adresi belirtin. :")
                print("Lütfen bekleyin...")
                defuser = degisuser
                print("Başarılı bir şekilde sistemdeki mail adresiniz değişti yeni mail adresi " + degisuser)
        elif (defuser == user) and (key != defkey):
            print("Girdiğiniz şifre sistemde kayıtlı değil.")
            print("şifrenizi değiştirmek istermisiniz? (evet/hayır)")
            cevapb = input( )
            if (cevapb == "evet"):
                    print("Lütfen bekleyin...")
                    yenikey = input("Yeni şifrenizi girin :")
                    print("Lütfen bekleyin...")
                    defkey = yenikey
                    print("Başarıyla sistemdeki şifreniz değişti " + yenikey)
                    
    elif (cevap == "yok"):
        yeniusr = input("Bir G-mail belirtiniz.")
        defuser = yeniusr
        yeniusrkey = input("Bir şifre belirtiniz. (8 Karakterli)")
        defkey = yeniusrkey
        print("Sisteme başarılı bir şekilde kayıt oldunuz.")
        print('Mail :' + yeniusr)
        print('Şifre :' + yeniusrkey)
    else:
        print("Sisteme giriş yapamadınız.")
