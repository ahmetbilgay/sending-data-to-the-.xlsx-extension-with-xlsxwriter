import xlsxwriter

#add variable(optional)
isim = str(input("Adınızı Giriniz : "))
firma = str(input("Firma Adınızı Giriniz : "))
adres = str(input("Adresinizi Giriniz : "))
urun = str(input("Ürününüzün Adını Giriniz : "))
adet = int(input("Ürününüzün Adetini Giriniz : "))
birimFiyat = int(input("Ürününüzün Birim Fiyatını Giriniz : "))
tarih = str(input("Tarihi Giriniz : "))

#xlsxwriter 
excelfilename = xlsxwriter.Workbook("excel.xlsx")
excelsheetname = excelfilename.add_worksheet("sheet")


excelsheetname.write("A1",isim)
excelsheetname.write("B1",firma)
excelsheetname.write("C1",adres)
excelsheetname.write("D1",firma)
excelsheetname.write("E1",urun)
excelsheetname.write("F1",adet)

excelfilename.close()