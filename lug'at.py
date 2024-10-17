# # buyumlar = {
# #     "ism" : "ali",
# #     "familiya" : "valiyev",
# #     "yosh" : 15,
# #     "o'quvchi" : True,
# #     "manzil" : {
# #         "yashash_joyi" : "Oromgoh",
# #         "o'qisah_joyi" : "Do'stlida"
# #     }

# # }


# # print(buyumlar)



# taomlar = {
#     "sali" : "osh",
#     "g'ani" : "qotirma",
#     "vali" : "shashlik",
#     "dandonali" : "taomlar"
# }

# # print({taomlar["g'ani"].title()})

# # taomlar["dav_dava"] = "sarimsoq piyoz"
# # taomlar["wotik"] = input("Wotikning taomi: ")

# # taomlar.update({"alw" : "Lag'mon"})
# # print(taomlar)








# """ Qiymatni o'chirish """

# del taomlar["sali"]
# print(taomlar)

# taomlar.pop("vali")
# print(taomlar)

# taomlar.popitem()

# print(taomlar)

# """ Ro'yxatni tozalash """

# taomlar.clear()

# print(taomlar)








# ota_ona = {
#     "ota" : {
#         "ism" : "Sali",
#         "familiya" : "Valiyev",
#         "yosh" : 43,
#         "kasb" : True 
#     },

#     "ona" : {
#         "ism" : "Salima",
#         "familiya" : "Valiyeva",
#         "yosh" : 40,
#         "kasb" : "Uy bekasi"
#     }
    
# }


# for key, value in ota_ona.items():
#     print(f"{key} - {value}")






# fanlar = {
#     "fan1" : "Ona-Tili",
#     "fan2" : "Rus-Tili",
#     "fan3" : "O'zbek-tili",
#     "fan4" : "Ingiliz-tili"
# }


# fanlar["fan5"] = "Qozoq-Tili"
# fanlar.update({"fan6" : "Nemis-Tili"})

# print(fanlar)


# fanlar["fan1"] = "Turkman-Tili"

# fanlar.update({"fan2" : "Qirg'iz-Tili🤣"})
# print(fanlar)




# fanlar.pop("fan1")
# fanlar.popitem()
# del fanlar["fan4"]

# fanlar.clear()

# print(fanlar)










# """ Get metodi """

# ismlar = {
#     "ali" : "Sali",
#     "g'ani" : "Qani"
# }

# print(f"salom {ismlar["sali"]}")
# print(f"salom {ismlar.get("sali")}")











# ombor = {
#     "asal" : 4_000,
#     "bexi" : 3_000,
#     "non" : 3_000,
#     "tuz" : 1_000,
#     "banan" : 8_000 
# }


# print("Assalomu aleykum do'konimizga xush kelibsiz! ")


# for k, v in ombor.items():
#     print(f"{k} - {v}")


# bor = []
# yoq = []

# nechtaligi = int(input("Nechta narsa harid qilmoqchisiz: "))
# for x in range(nechtaligi):
#     x = input(f"{x+1} - chi mahsulot nomini kiriting: ")
#     if x in ombor:
#         bor.append(x)
#     elif x not in ombor:
#         yoq.append(x)

# print(f"Bizda quyidagi mahsulotlar yoq: ",end=" ")

# if yoq:
#     for y in yoq:
#         if y[-1]:
#             print(f"{y}", end=". ")
#         elif y[0]:
#             print(f"{y}", end= ", ")
#         else:
#             print(end=", ")

# print(f"\nBizda quyidagi mahsulotlar bor: ",end=" ")
# if bor:
#     for b in bor:
#         if b[-1]:
#             print(f"{b}", end=". ")
#         elif b[0]:
#             print(f"{b}", end= ", ")
#         else:
#             print(f"{b}", end=", ")














bor = []
yoq = []

menu = {
    "osh" : 4_000,
    "salat" : 3_000,
    "kabob" : 3_000,
    "shashlik" : 1_000,
    "qotirma" : 8_000 
}


print("Assalomu aleykum restoranimizga xush kelibsiz! ")


for k, v in menu.items():
    print(f"{k} - {v}")



nechtaligi = int(input("Nechta narsa xariq qilmoqchisiz: "))


for s in range(nechtaligi):
    s = input(f"{s+1} - chi ovqat nomini kiriting: ")
    if s in menu:
        bor.append(s)
    elif s not in menu:
        yoq.append(s)


print(f"Bizda quyidagi ovqatlar bor ular: ", end=" ")
if bor:
  for a in bor:
       if a [-1]:
           print(f"{a}", end=". ")
       elif a [0]:
            print(f"{a}", end=", ")
       else:
            print(f"{a}", end=", ")

print(f"Bizda quyidagi ovqatlar yoq ular: ", end=" ")

if yoq:
   for b in bor:
       if b [-1]:
        print(f"{b}", end=". ")
       elif b [0]:
        print(f"{b}", end=", ")
       else:
        print(f"{b}", end=", ")







