defuser = "Creza"
defkey = "Creza was here"

while (True):
    print("Hesabınız varmı (v/y)?")
    cevap = input( )
    if (cevap == "v"):
        user = input("E-posta :")
        key = input("Şifrenizi girin :")
        
        if (defuser == user) and (key == defkey):
            print("👍 Giriş başarılı.")
            break
        elif (defuser != user) and (key == defkey):
            print("Hatalı kullanıcı adı.")
            print("Kullanıcı adınızı değiştirmek istermisiniz(e/h)")
            cevapa = input( )
            if (cevapa == "e"):
                degisuser = input("Yeni kullanıcı adınızı girin :")
                defuser = degisuser
                print("Başarılı!")
        elif (defuser == user) and (key != defkey):
            print("Hatalı şifre.")
            print("Şifrenizi değiştirmek istermisimiz(E/H")
            cevapb = input( )
            if (cevapb == "e"):
                    print("Lütfen bekleyin...")
                    yenikey = input("Yeni şifrenizi girin :")
                    print("Lütfen bekleyin...")
                    defkey = yenikey
                    print("Başarılı.")
                    
    elif (cevap == "y"):
        yeniusr = input("Kullanıcı adı belirleyiniz :")
        defuser = yeniusr
        yeniusrkey = input("Şifre belirleyiniz :")
        defkey = yeniusrkey
        print("Hesabınız başarıyla oluşturuldu!")
        
    else:
        print("Hatalı giriş.")
