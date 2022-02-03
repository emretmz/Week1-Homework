
user_weight=int(input("Kilonuz:"))
user_height=int(input("Boyunuz (cm):"))

index=user_weight/((user_height/100)**2)
print(f"index Yuzdesi: {index}")

if index<25:
    print("Normal")
elif 25<index<30:
    print("Fazla kilolu")
elif 30<index<40:
    print("Fazla Kilolu")
else :
    print("Obez")