import xlsxwriter

isim = str(input("Adınızı Giriniz : "))
firma = str(input("Firma Adınızı Giriniz : "))
adres = str(input("Adresinizi Giriniz : "))
urun = str(input("Ürününüzün Adını Giriniz : "))
adet = int(input("Ürününüzün Adetini Giriniz : "))
birimFiyat = int(input("Ürününüzün Birim Fiyatını Giriniz : "))
tarih = str(input("Tarihi Giriniz : "))


exceldosyaadi = xlsxwriter.Workbook("excelsayfam.xlsx")
excelsayfaadi = exceldosyaadi.add_worksheet("orneksayfa")


excelsayfaadi.write("A1",isim)
excelsayfaadi.write("B1",firma)
excelsayfaadi.write("C1",adres)
excelsayfaadi.write("D1",firma)
excelsayfaadi.write("E1",urun)
excelsayfaadi.write("F1",adet)

exceldosyaadi.close()