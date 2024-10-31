# """ 1-mashq """

# eng_uzb = {
#     "pear" : "nok",
#     "apple" : "olma",
#     "hand" : "qol",
#     "finger" : "barmoq"
# }


# sorov = input("Sizga qaysi so'zni tarjimasi kerak: ")

# for k, v in eng_uzb.items():
#     if k == sorov:
#         print(v)
#     elif v == sorov:
#         print(k)
# if sorov not in eng_uzb.keys() and sorov not in eng_uzb.values():
#         print("Xato")


# """ 2-mashq """

# menu = {
#     "osh" : 2_000,
#     "qotirma" : 5_000,
#     "shashlik" : 3_000
# }


# print(menu.keys())


# for k, v in menu.items():
#     print(k, v)



# """ 3-mashq """

# ism = input("Ismingizni kiriting: ")

# yosh = int(input("Yoshingizni kiriting: "))

# if 1 <= yosh <= 6:
#     print("Siz bog'cha yoshidasiz! ")
# elif 7 <= yosh <= 17:
#     print("Siz maktab yoshidasiz! ")
# elif 18 <= yosh <= 30:
#     print("Siz universitetda o'qiysiz! ")
# elif 31 <= yosh <= 100:
#     print("Siz maktab o'quvchisi emasssiz! ")
# else:
#     print("Notog'ri son kiritdingiz!")




# """ 4-mashq """


# ism = {
#     "xusanov" : "dovudbek",
#     "abdulaxadov" : "shodiyor",
# }


# sorov = input("Ism yoki familiyangizni kiriting: ")

# for k, v in ism.items():
#     if k == sorov:
#         print(v)
#     elif v == sorov:
#         print(k)
# if sorov not in ism.keys() and sorov not in ism.values():
#         print("Kechirasiz bida bunday ism yoki familiya yo'q! ")
