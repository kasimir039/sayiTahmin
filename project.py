import random

randNumber = random.randint(1,100)

count = 0

while True:
    number = int(input("1 ile 100 arasında sayı giriniz: Çıkmak için 0 tuşuna basınız\n"))
    count += 1
    
    if count == 10:  
        print(f"Hakkınız doldu! tahmin edilemeyen sayı: {randNumber}")
        break      

    if number == 0:
        print("Çıkış başarılı")
        break
    elif number < randNumber:
        print("Daha büyük bir sayı giriniz: ")
    elif number > randNumber:
        print("Daha küçük bir sayı giriniz: ")
    else:
        print(f"Tebrikler sayıyı {count} kerede doğru tahmin ettiniz: {randNumber}")



    




