import sqlite3 as sql


baglanti = sql.connect("ogr.db")

def baglan(): 
 komut="CREATE TABLE IF NOT EXISTS ogrenci(id PRIMARY KEY AUTOINCREMENT,ad TEXT)"
 baglanti.execute(komut)
 baglanti.commit()

def ogrEkle(ad):
 baglanti.execute("INSERT OR REPLACE INTO ogrenci VALUES(null,?);",(ad,))
 baglanti.commit()
 print("Öğrenci Eklendi")

def scnk():
    print("1.Öğrenci Listesi Getir")
    print("2.Öğrenci Ekle")    
    cevap = input("Seçim: ")
    if cevap == 1:
     liste= baglanti.execute("SELECT * FROM kab")

     print("|[ID]|[  AD  ]|")

     for veri in liste:         
        print(
            "|",veri[0],
            "|",veri[1],
            "|"
            )
     scnk()
    elif cevap == 2:        
        isim = input("Öğrenci Adını Giriniz: ")
        ogrEkle(isim)
        scnk()




