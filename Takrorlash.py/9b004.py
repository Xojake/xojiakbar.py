# """ 1-mashq """

# sonlar = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542]

# print(sorted(sonlar))

# sonlar.sort(reverse=True)
# print(sonlar)

# sonlar.reverse()
# print(sonlar)


# """ 2-mashq """

# mevalar = ["Olma", "O'rik", "Shaftoli", "Apelsin", "Malina", "Xurmo"]

# for meva in mevalar:
#     if meva == "Olma" or meva == "Malina":
#         print(meva.upper())
#     else:
#         print(meva.capitalize())


# """ 3-mashq """


# books = {
#     "kitob1" : "Anor",
#     "kitob2" : "O'tkan kunlar"
# }


# books.update({"kitob3" : "Olma"})
# print(books)

# books["kitob3"] = "Qora tunlar"
# print(books)


# books["kitob3"] = "Treyd"
# print(books)

# books.update({"kitob1" : "Alpomish"})
# print(books)

# del books["kitob1"]
# print(books)

# books.popitem()
# print(books)

# books.pop("kitob2")
# print(books)

# books.clear()


# """ 4-mashq """
# from math import sqrt
# sonlar = list(range(102, 2020))

# for son in sonlar:
#     if 102 <= son <= 1000:
#         print({son**3})
#     elif 1504 <= son <= 2019:
#         print({son-4})
#     elif son%7 == 0:
#         print(f"{sqrt(son)} - shu")
    




# """ 5-mashq """

# foiz = int(input("Imtihondan necha foiz bilan o'tdingiz: "))


# if 0 <= foiz <= 64:
#     print("Siz imtihondan yiqilgansiz! ")
# elif 65 <= foiz <= 85:
#     print("Siz imtihondan o'tgansiz! ")
# elif 86 <= foiz <= 100:
#     print("Siz imtihondan o'tgansiz! ")
#     orin = int(input("Nechinchi o'rinni oldingiz: "))
#     if orin == 1:
#         print("Tabriklayman 100% grant")
#     elif orin == 2:
#         print("Tabriklayman 75% grant")
#     elif orin == 3:
#         print("Tabriklayman 50% grant")
#     elif orin == 4:
#         print("Tabriklayman 25% grant")
#     else:
#         print("Siz grantga yetarli orin olmagansiz: ")
# else:
#     print("Siz xato son kiritdingiz!!!")





