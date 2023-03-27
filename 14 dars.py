# # -*- coding: utf-8 -*-
# """
# Created on Fri Oct 28 14:36:03 2022

# @author: IT CENTER YANGIYER
# """

# # python_words = {
# #     "integer": "butun son,"
# #     "float": "o`nlik son",
# #     "boolean": "mantiqiy qiymat",
# #     "for": "biror amalni qayta-qayta bajarish "
# #     }

# # davlatlar = {
# #     'o`zbekiston': 'toshkent',
# #     'aqsh': 'washington d.c.',
# #     'rossiya': 'moskova',
# #     'tojikiston': 'dushanbe',
# #     'qirgiziston': 'bishkek',
# #     'qozoqiston': 'nursultan',
# #     'malayziya': 'kuala-lumpur',
# #     'singapur': 'singapur',
# #     'italya': 'rim'
# #     }

# # country = input('Qaysi davlatning poytaxtini bilishni istaysizmi?:').lover()
               
# # capital = davlatlar.get(country)
# # if capital == None:
# #     print("kechirasiz, bizda bu haqida malumot yo`q")
# # else:
# #     print(f"{country.upper()}ning poytaxti {capital.title()}")

              
# # menu = {
# #     'osh': 20000,
# #     'lag`mon': 22000,
# #     'non': 4000,
# #     'choy': 5000,
# #     'shashlik': 12000,
# #     'somsa': 6000,
# #     'tabaka': 15000,
# # }
# # narh = 0
# # narhlar = []
# # print('3 ta taom buyurtma bering.')
# # buyurtmalar = []
# # for n in range(3):
# #     buyurtmalar.append(input(f'{n+1}-taom:').lower())
    
# # for buyurtma in buyurtmalar:
# #     if buyurtma in menu:
# #         narh = narh + menu[buyurtma]
# #         narhlar.append(menu[buyurtma])
# #         print(f'{buyurtma.title()} {menu[buyurtma]} so`m')
# #     else:
# #         print(f'Kechirasiz, bizda {buyurtma} yo`q.')
# # print(f'jami: {narh}')
# # print(f'jami: {sum(narhlar)}')
# print("dostingizni ismini kiriting")
# dostlar = {}
# ishora = True
# n = 1
# while ishora:
#     ism = input(f"{n} - dostingizni ismini kiriting: ")
#     yosh = int(input(f"{ism.title()} ning yoshini kiriting: "))
#     dostlar[ism] = yosh
#     n+=1
#     javob = input("yana malumot qoshasizmi? (ha/yoq) ")
#     if javob != "ha":
#         ishora = False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ["lacetti","nexia","toyota","nexia","audi","malibu" ]
# car = "lacetti"
# car2 = "malibu"
# while car in cars:
#     cars.remove(car)
# print(cars
      
talabalar = ["hasan","husan","olim","botir"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning bahosini kiriting ")
    print(f"{talaba.title()} baholandi")     
    baholangan_talabalar[talaba] = int(baho)
      
      
      



