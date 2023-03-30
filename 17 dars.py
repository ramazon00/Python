



# def toliq_ism_yasa(ism, familya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism}, {familya}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")

# def toliq_ism_yasa(ism, familya, otasini_ismi = ""):
#     """toliq ism qaytaruvchi funksiya"""
#     if otasini_ismi:
#         toliq_ism = f"{ism} {familya} {otasini_ismi}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()
    


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov", "boburvich")
# print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompanya, model, rangi, karopka, yili, narhi=None):
#     avto ={
#         "kompany":kompanya,
#         "model":model,
#         "color":rangi,
#         "avtomat":karopka,
#         "year":yili,
#         "price":narhi,
#       }  
#     return avto

# avto1 = avto_info("GM", "malibu", "sariq", "avtomat", 2022)
# avtolar = [avto1]
# print("onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["price"]:
#         narx = f'{avto["price"]}$'
#     else:
#         narx = "nomalum"
#     print(f"{avto['color']} {avto['model']}. narhi: {narx}")
    


# def oraliq(min, max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=qadam
#     return sonlar
# print(oraliq(1,21,2))

# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto={
#         "kompaniya" : kompaniya,
#         "model": model,
#         "rang" : rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto

# print("Saytimizdagi avtolar ro`yhatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("Quyidagi ma`lumotlarni kiriting", end = "")
#     kompaniya=input("Ishlab chiqaruvchi:")
#     model=input("Modeli:")
#     rangi=input("Rangi:")
#     korobka=input("Korobkasi:")
#     yili=input("Ishlab chiqarilgan yili:")
#     narhi=input("Narhi:")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili,narhi))

#     d=input("Yana kiritishni istaysizmi:  (yes/no)")
#     if d== "no":
#         break
# for avto in avtolar:
#     if avto["narh"]:
#         narh = f"{avto['narh']}$"
#     else:
#         narh="Nomalum"
        
        
#     e = (f"Salonimizdagi avtolar ro`yhati: "f"Kompaniyasi {avto['kompaniya']}, Modeli {avto['model']}, Rangi {avto['rang']} ,Korobkasi {avto['korobka']},Yili {avto['yil']},Narhi {avto['narh']}")  
#     print(e.title())

# def talaba_bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism = ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholar[ism]= int(baho)
#     return baholar
# baho= talaba_bahola(["ali","vali","xasan","xusan"])
# print(baho)

























