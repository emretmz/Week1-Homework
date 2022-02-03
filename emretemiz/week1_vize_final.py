

user_name=input("Kullanici adi:")
user_surname=input("Kullanici Soyadi:")
user_num=int(input("Okul numarasi:"))
user_visa=int(input("Vize notu:"))
user_final=int(input("Final notu:"))

ort=(user_final/100)*60+(user_visa/100)*40
if ort<50:
    print(f"Kaldiniz! Notunuz {ort}")
else:
    print(f"Gectiniz.Notunuz {ort}")