sozluk={"apple":"elma", "banana":"muz","LOL" : "komik bir şeye verilen cevap"}

anahtarkelime=input("bana sormak istediğin kelime nedir? ")

if anahtarkelime in sozluk.keys():
    
    print("yazdığınız kelimenin anlamı: ",sozluk[anahtarkelime])
else:
    print("bulamadım")
