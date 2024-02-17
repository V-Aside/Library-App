class Library:
    def __init__(self, kitapAdi=None, yazarAdi=None, yayinTarihi=None, sayfaSayisi=None, kategori=None, barkod=None):
        file = open("Books.txt","a+", encoding="UTF-8")
        self.kitapAdi = kitapAdi
        self.yazarAdi = yazarAdi
        self.yayinTarihi = yayinTarihi
        self.sayfaSayisi = sayfaSayisi
        self.kategori = kategori
        self.barkod = barkod
        self.file = file

    def listele(self): # Kütüphane içerisindeki ögeleri listeler.
        self.file.seek(0)
        #Dosya içeriğinin boş olup olmadığını kontrol eder. Boşsa kullanıca bildirir.
        if len(self.file.read()) != 0:
            self.file.seek(0)
            #Dosya içeriğini satırlara göre ayırır ve her bir satıra ulaşır.
            for satir in self.file.read().splitlines():
                #Satır içeriğini virgüle göre ayırır.
                icerik = satir.split(",")
                #İçeriğin başı ve sonundaki boşluk karakterlerini siler ve ekrana yazdırır.
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\n")
        else:
            print("Kitaplıkta Kayıtlı Kitap Bulunmamakta.")

    def ismeGoreFiltre(self, kitapAdi): # İsme göre filtreler
        self.file.seek(0)
        # Boş bir liste oluşturur.
        kitapListesi = []
        for satir in self.file.read().splitlines():
            icerik = satir.split(",")
            if kitapAdi.title().strip() == icerik[0].strip():
                # Aranan değer ile eşleşen içeriği listeye ekler ve ekrana yazdırır.
                kitapListesi.append(icerik)
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\nYayınlanma Tarihi: {icerik[2].strip()}\nSayfa Sayısı: {icerik[3].strip()}\nKategori: {icerik[4].strip()}\nBarkod: {icerik[5].strip()}\n")
        
        else:
            # Oluşturulan liste boş ise kullanıcının aradığı değer ile eşleşen içerik olmadığı anlamına gelir.
            if len(kitapListesi) == 0:
                print("Aradığınız İsme Sahip Bir Kitap Bulunmuyor.")

    def yazaraGoreFiltre(self, yazarAdi): # Yazara göre filtreler
        self.file.seek(0)
        kitapListesi = []
        for satir in self.file.read().splitlines():
            icerik = satir.split(",")
            if yazarAdi.title().strip() == icerik[1].strip():
                kitapListesi.append(icerik)
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\nYayınlanma Tarihi: {icerik[2].strip()}\nSayfa Sayısı: {icerik[3].strip()}\nKategori: {icerik[4].strip()}\nBarkod: {icerik[5].strip()}\n")
        else:
            if len(kitapListesi) == 0:
                print("Aradığınız Yazara Ait Bir Kitap Bulunmuyor.")

    def tariheGoreFiltre(self, yayinTarihi): # Yayın tarihine göre filtreler
        self.file.seek(0)
        kitapListesi = []
        for satir in self.file.read().splitlines():
            icerik = satir.split(",")
            if yayinTarihi.title().strip() == icerik[2].strip():
                kitapListesi.append(icerik)
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\nYayınlanma Tarihi: {icerik[2].strip()}\nSayfa Sayısı: {icerik[3].strip()}\nKategori: {icerik[4].strip()}\nBarkod: {icerik[5].strip()}\n")
        else:
            if len(kitapListesi) == 0:
                print("Aradığınız Yayın Tarihine Sahip Bir Kitap Bulunmuyor.")

    def sayfaSayisinaGoreFiltre(self, sayfaSayisi): # Sayfa sayısına göre filtreler
        self.file.seek(0)
        kitapListesi = []
        for satir in self.file.read().splitlines():
            icerik = satir.split(",")
            if sayfaSayisi.title().strip() == icerik[3].strip():
                kitapListesi.append(icerik)
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\nYayınlanma Tarihi: {icerik[2].strip()}\nSayfa Sayısı: {icerik[3].strip()}\nKategori: {icerik[4].strip()}\nBarkod: {icerik[5].strip()}\n")
        else:
            if len(kitapListesi) == 0:
                print("Aradığınız Sayfa Sayısına Sahip Bir Kitap Bulunmuyor.")

    def kategoriyeGoreFiltre(self, kategori): # Kategoriye göre filtreler
        self.file.seek(0)
        kitapListesi = []
        for satir in self.file.read().splitlines():
            icerik = satir.split(",")
            if kategori.title().strip() == icerik[4].strip():
                kitapListesi.append(icerik)
                print(f"Kitap Adı: {icerik[0].strip()}\nYazar Adı: {icerik[1].strip()}\nYayınlanma Tarihi: {icerik[2].strip()}\nSayfa Sayısı: {icerik[3].strip()}\nKategori: {icerik[4].strip()}\nBarkod: {icerik[5].strip()}\n")
        else:
            if len(kitapListesi) == 0:
                print("Aradığınız Kategoride Bir Kitap Bulunmuyor.")

    def ekle(self, barkod): # Kütüphaneye kitap ekler.
        # Geçici bir kontrol listesi oluşturulur.
        kontrolListesi = []
        self.file.seek(0)
        for satir in self.file.read().splitlines():
            self.file.seek(0)
            # Girilen barkod numarasına ait kayıtlı bir kitap olup olmadığı kontrol edilir.
            if barkod == satir.split(",")[5].strip():
                # Girilen barkod numarasına ait kayıtlı bir kitap varsa o kitaba ait bilgiler geçici listeye kaydedilir.
                kontrolListesi.append(satir)
                # Girilen barkod numarasına ait kayıtlı bir kitap bulunduğunda güncelleme yapılmak istenip istenmediği sorulur.
                while True:
                    guncellemeIstek = input("Bu ürün daha önce kütüphaneye eklenmiş. Güncelleme yapmak ister misiniz? (e/h): ").lower()
                    if guncellemeIstek == "e":
                        self.guncelle(barkod)
                        break
                    elif guncellemeIstek == "h":
                        break
                    else:
                        print("Lütfen Geçerli Bir Değer Girin.")
        else:
            if len(kontrolListesi) == 0:
                while True:
                    self.kitapAdi = input("Kitap Adı: ").strip().title()
                    if self.kitapAdi != "":
                        break
                    else:
                        print(50*"-")
                        print("Kitap Adı Boş Bırakılamaz!")
                        print(50*"-")
                self.yazarAdi = input("Yazar Adı: ").strip().title() # Opsiyonel
                self.yayinTarihi = input("Yayın Tarihi: ").strip().title() # Opsiyonel
                self.sayfaSayisi = input("Sayfa Sayısı: ").strip().title() # Opsiyonel
                self.kategori = input("Kategori: ").strip().title() # Opsiyonel
                if self.yazarAdi == "": # Yazar adı belirtilmediyse varsayılan değer atanır.
                    self.yazarAdi = None
                if self.yayinTarihi == "": # Yayın tarihi belirtilmediyse varsayılan değer atanır.
                    self.yayinTarihi = None
                if self.sayfaSayisi == "": # Sayfa sayısı belirtilmediyse varsayılan değer atanır.
                    self.sayfaSayisi = None
                if self.kategori == "": # Kategori belirtilmediyse varsayılan değer atanır.
                    self.kategori = None
                # Toplanan bilgiler dosyaya işlenir.
                self.file.write(f"{self.kitapAdi}, {self.yazarAdi}, {self.yayinTarihi}, {self.sayfaSayisi}, {self.kategori}, {barkod}\n")
                print(50*"-")
                print("Kitap kütüphaneye eklenmiştir.")

    def guncelle(self,barkod): # Kütüphaneye daha önce eklenmiş kitabın içeriğini günceller.
        self.file.seek(0)
        icerikListesi = [satir for satir in self.file.read().splitlines()]
        for icerik in icerikListesi:
            icerikler = icerik.split(",")
            if barkod == icerikler[5].strip():
                self.kitapAdi = input(f"Kitap Adı (Eski Bilgi: {icerikler[0]}): ").strip().title()
                self.yazarAdi = input(f"Yazar Adı (Eski Bilgi: {icerikler[1]}): ").strip().title()
                self.yayinTarihi = input(f"Yayın Tarihi (Eski Bilgi: {icerikler[2]}): ").strip().title()
                self.sayfaSayisi = input(f"Sayfa Sayısı (Eski Bilgi: {icerikler[3]}): ").strip().title()
                self.kategori = input(f"Kategori (Eski Bilgi: {icerikler[4]}): ").strip().title()
                icerikListesi.remove(icerik)
                open("Books.txt","w").close()
                for yeni_icerikler in icerikListesi:
                    self.file.write(f"{yeni_icerikler}\n")
                self.file.write(f"{self.kitapAdi}, {self.yazarAdi}, {self.yayinTarihi}, {self.sayfaSayisi}, {self.kategori}, {barkod}\n")
                break
        else:
            print(50*"-")
            print("Girdiğiniz Barkoda Sahip Bir Ürün Bulunmamaktadır.")

    def kaldır(self, silinecek_kitap): # Kütüphane içerisinden ismi belirtilen ögeyi kaldırır.
        self.file.seek(0)
        # Boş bir liste oluşturulur, dosya içerisindeki her satır ayrıştırılır ve bu listenin içerisine aktarılır.
        kitaplar = [kitap for kitap in self.file.read().splitlines()]
        # Daha önce içeriği aktardığımız liste içerisindeki ögeler ayrıştırılır ve silmek istenen kitabın isim bilgisi ile aynı olan kitap bulunur.
        for kitap_kontrol in kitaplar:
            if kitap_kontrol.split(",")[0].strip().title() == silinecek_kitap:
                # Kitap bulunduktan sonra listeden o kitaba ait bilgiler silinir ve dosya temizlendikten sonra listede kalan ögeler dosya içerisine tekrardan yazılır.
                kitaplar.remove(kitap_kontrol)
                open("Books.txt","w",encoding="UTF-8").close()                
                for yeni_icerik in kitaplar:
                    self.file.write(f"{yeni_icerik}\n")
                print("Kitap Kütüphaneden Kaldırıldı.")
                break
        # Eğer kullanıcın belirttiği isme ait bir kitap bulunamazsa uyarı verir.
        else:
            print("-"*50)
            print("Bu İsme Sahip Bir Kitap Bulunmamaktadır.")

    def __del__(self):
        self.file.close()
        
while True: # Arayüz

    # Kullanıcı Karşılanır.
    print("Hoş Geldiniz".center(20,"-"),"\n1- Kitapları Listele\n2- Filtreleme Seçenekleri\n3- Kitap Ekle\n4- Kitap Güncelle\n5- Kitap Sil\n6- Programı Kapat")
    try:
        print(50*"-")
        # Kullanıcının girdiğini değer "int" formatına dönüştürülür. Dönüştürülemezse kullanıcıya hatalı bilgi girdiği belirtilir.
        secim = int(input("Seçiminiz: ".rjust(28)))
        print(50*"-")
        # Kullanıcının istenen formatta değer girmesine rağmen herhangi bir komutu çalıştırmıyorsa kullanıcıya hata mesajı gösterilir.
        if secim != 1 and secim != 2 and secim != 3 and secim != 4 and secim != 5 and secim != 6: 
            raise ValueError
        else:
            # Kullanıcı geçerli bir değer girdiği zaman ilgili class'a ait obje oluşturulur.
            lib = Library()
        
        if secim == 1: # Kitapları Listele
            lib.listele()
            print(50*"-")

        elif secim == 2: # Filtreleme Seçenekleri
            while True:
                print("1- İsme Göre Filtrele\n2- Yazara Göre Filtrele\n3- Yayın Tarihine Göre Filtrele\n4- Sayfa Sayısına Göre Filtrele\n5- Kategoriye Göre Filtrele\n6- Seçimi İptal Et")
                try:
                    print(50*"-")
                    # Kullanıcının girdiğini değer "int" formatına dönüştürülür. Dönüştürülemezse kullanıcıya hatalı bilgi girdiği belirtilir.
                    filtreSecim = int(input("Lütfen Filtreleme Şeklini Seçiniz: ".rjust(40)))
                    print(50*"-")
                    # Kullanıcının istenen formatta değer girmesine rağmen herhangi bir komutu çalıştırmıyorsa kullanıcıya hata mesajı gösterilir.
                    if filtreSecim != 1 and filtreSecim != 2 and filtreSecim != 3 and filtreSecim != 4 and filtreSecim != 5 and filtreSecim != 6:
                        raise ValueError
                    else:
                        if filtreSecim == 1: # Kitap İsmine Göre
                            while True:
                                filtre = input("Aradığınız Kitabın Adını Girin: ")
                                if filtre.strip() != "":
                                    break
                            print(50*"-") 
                            lib.ismeGoreFiltre(filtre)
                            break

                        elif filtreSecim == 2: # Yazar İsmine Göre
                            while True:
                                filtre = input("Aradığınız Kitabın Yazarının Adını Girin: ")
                                if filtre.strip() != "":
                                    break
                            print(50*"-") 
                            lib.yazaraGoreFiltre(filtre)
                            break

                        elif filtreSecim == 3: # Yayın Tarihine Göre
                            while True:
                                filtre= input("Aradığınız Kitabın Yayın Tarihini Girin: ")
                                if filtre.strip() != "":
                                    break
                            print(50*"-")
                            lib.tariheGoreFiltre(filtre)
                            break

                        elif filtreSecim == 4: # Sayfa Sayısına Göre
                            while True:
                                filtre = input("Aradığınız Kitabın Sayfa Sayısını Girin: ")
                                if filtre.strip() != "":
                                    break
                            print(50*"-")
                            lib.sayfaSayisinaGoreFiltre(filtre)
                            break

                        elif filtreSecim == 5: # Kategoriye Göre
                            while True:
                                filtre = input("Aradığınız Kitabın Kategorisini Girin: ")
                                if filtre.strip() != "":
                                    break
                            print(50*"-")            
                            lib.kategoriyeGoreFiltre(filtre)
                            break
                        
                        else: # Seçim İptali
                            print("Bir Üst Menüye Aktarılıyor.".center(50))
                            break
                
                except ValueError:
                    print(50*"-")
                    print("Lütfen Geçerli Bir Değer Girin.")
                    print(50*"-")
            print(50*"-")

        elif secim == 3: # Kitap Ekle
            while True: # Kullanıcıdan kitap adı ister ve eğer kitap adı boş geçilmişse kullanıcı geçerli bir kitap adı girene kadar kullanıcıya sorar.
                barkod = input("Barkod Kodunu Giriniz (HER KOD KİTABA ÖZGÜDÜR): ")
                if barkod.strip() != "": # Geçerli bir kitap adı girildikten sonra opsiyonel bilgiler istenir.
                    break
                else:
                    print(50*"-")
                    print("Barkod Kodu Boş Bırakılamaz!".center(50))
                    print(50*"-")
            lib.ekle(barkod)
            print(50*"-")

        elif secim == 4:
            while True: # Kullanıcıdan kitap adı ister ve eğer kitap adı boş geçilmişse kullanıcı geçerli bir kitap adı girene kadar kullanıcıya sorar.
                barkod = input("Güncellemek İstediğiniz Kitabın Barkod Kodunu Giriniz: ")
                if barkod.strip() != "": # Geçerli bir kitap adı girildikten sonra opsiyonel bilgiler istenir.
                    break
                else:
                    print(50*"-")
                    print("Barkod Kodu Boş Bırakılamaz!".center(50))
                    print(50*"-")
            lib.guncelle(barkod)
            print(50*"-")

        elif secim == 5:
            while True:
                silinecek_kitap = input("Lütfen Silmek İstediğiniz Kitabın Adını Girin: ").title().strip()
                if silinecek_kitap != "":
                    break
                else:
                    print(50*"-")
                    print("Kitap Adı Boş Bırakılamaz!")
                    print(50*"-")        
            lib.kaldır(silinecek_kitap)
            print(50*"-")

        else:
            del lib
            print("Programdan Kapatılıyor...")
            print(50*"-")
            break

    except ValueError:
        print(50*"-")
        print("Lütfen Geçerli Bir Değer Girin.")
        print(50*"-")
