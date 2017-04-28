kisiler = {

            "Burak Çayır":{
                "ad":"Burak",
                "soyad":"Çayır",
                "yaş":"21",
                "memleket":"Çankırı",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Sistem Mühendisi",
                "Tecrübe":"5 Yıl",
                "Uzmanlık":"Sistem Yöneticiliği , Sistem Programlama"
            },
            "Sinan Sarıkaya":{
                "ad":"Sinan",
                "soyad":"Sarıkaya",
                "yaş":"22",
                "memleket":"Çankırı",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Proje Yöneticisi",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Proje Geliştirme"
            },
            "Sedat Kızılçınar":{
                "ad":"Sedat",
                "soyad":"Kızılçınar",
                "yaş":"22",
                "memleket":"Batman",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Murat Yıldız":{
                "ad":"Murat",
                "soyad":"Yıldız",
                "yaş":"22",
                "memleket":"Yozgat",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Sistem Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Sistem Yönetimi Süpervizörü"
            },
            "Ramin Karimkhani":{
                "ad":"Ramin",
                "soyad":"Karimkhani",
                "yaş":"22",
                "memleket":"Kırşehir",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Ali Ağdeniz":{
                "ad":"Ali",
                "soyad":"Ağdeniz",
                "yaş":"21",
                "memleket":"İstanbul",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Ramazan Uysal":{
                "ad":"Ramazan",
                "soyad":"Uysal",
                "yaş":"22",
                "memleket":"Aydın",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Onur Ekkazan":{
                "ad":"Onur",
                "soyad":"Ekkazan",
                "yaş":"22",
                "memleket":"Tekirdağ",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Atilla Şahin":{
                "ad":"Atilla",
                "soyad":"Şahin",
                "yaş":"22",
                "memleket":"Ankara",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            },
            "Furkan Yaylaçeşme":{
                "ad":"Furkan",
                "soyad":"Yaylaçeşme",
                "yaş":"22",
                "memleket":"İstanbul",
                "Mezun Olduğu Üni.":"Gazi Üniversitesi",
                "Meslek":"Kıdemli Siber Güvenlik Uzmanı",
                "Tecrübe":"7 Yıl",
                "Uzmanlık":"Siber Güvenlik Süpervizörü"
            }

           }

print("Veritabanındaki kişiler aşağıda listelenmiştir.\n")
for i in kisiler:
    print(kisiler[i]["ad"] +" "+ kisiler[i]["soyad"])
print()  #boşluk bırakma amacı ile
def kisi_bul(*args,**kwargs):
    for ad in args:
        if ad in kwargs:
            print(str (list ( (kisiler[ad].values() )  ) ).strip("[]"))
        else:
            print("{} kişisi veritabanında bulunmamakta".format(ad))


def kisi_bul2(*args,**kwargs):
    for ad in args:
        if ad in kwargs:
            liste = list( (kisiler[ad].values()) )
            for el in liste:
                print(el[:5],end=' ')
            print()
            # print(str (list ( (kisiler[ad].values() )  ) ).strip("[]"))
        else:
            print("{} kişisi veritabanında bulunmamakta".format(ad))

def belli_bilgileri_getir(ad,*args,**kwargs):
    for bilgi in args:
        if ad in kwargs:
            try:
                print(kisiler[ad][bilgi])
            except KeyError:
                print("{} bilgisi veritabanında bulunmamakta".format(bilgi))

def kisileri_arat(*args):   #kullanıcıya arayüz amacıyla yazıldı
    kisi_sayisi = int(input("kaç kişi gireceksiniz ? : "))
    kisi_listesi = []
    for i in range(kisi_sayisi):
        yeni_kisi = input("{}. kişiyi giriniz : ".format(i+1))
        kisi_listesi.append(yeni_kisi)
    secim = int(input("Bilgileri Nasıl Görüntülemek istersiniz ? (Normal Mod :1 , Kısaltılmış Mod :2) :"))
    if secim == 1:
        kisi_bul(*kisi_listesi, **kisiler)
    else:
        kisi_bul2(*kisi_listesi, **kisiler)

def belli_bilgiler(*args):
    kim = input("Kimin bilgilerini görmek istiyorsunuz ? :")
    bilgi_sayisi = int(input("kaç bilgi görmek istiyorsunuz ? : "))
    bilgi_listesi = []
    for i in range(bilgi_sayisi):
        yeni_bilgi = input("{}. bilgiyi giriniz : ".format(i+1))
        bilgi_listesi.append(yeni_bilgi)
    belli_bilgileri_getir(kim,*bilgi_listesi,**kisiler)

def kisi_bilgilerini_degistir():
    kisi_ismi = input("Bilgisini değiştireceğiniz kişinin Adını giriniz : ")
    print(list(kisiler[kisi_ismi].items()))
    print("\nKişinin nitelikleri : ")
    print(list(kisiler[kisi_ismi].keys()))
    degistir = input("Kişinin hangi bilgisini değiştirmek istiyorsunuz ? : ")
    kisiler[kisi_ismi][degistir] = input("{} bilgisini girin : ".format(degistir))
    print(list(kisiler[kisi_ismi].items()))


islem_sec = int(input("Ne yapmak istiyorsunuz ? (1.Bilgileri Görüntülemek , 2.Bilgileri Değiştirmek) : "))
if islem_sec==1:
    islem_sec_2 = int(input("Ne yapmak istiyorsunuz ? (1.Tüm bilgiler , 2.Seçeceğim bilgiler) : "))
    if islem_sec_2==1:
        kisileri_arat()
    else:
        belli_bilgiler()
else:
    kisi_bilgilerini_degistir()