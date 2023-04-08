# # 1
# from uuid import uuid4
# class Teacher:
#     __num_teacher=0
    
#     def __init__(self,ism,familiya,ochistva,mutaxasislik,bitirgan_universiteti,telefon,email):
#         self.ism = ism
#         self.familiya = familiya
#         self.ochistva = ochistva
#         self.__mutaxasislik = mutaxasislik
#         self.bititrgan_universiteti = bitirgan_universiteti
#         self.telefon = telefon
#         self.email = email
#         self.__id=uuid4()
#         Teacher.__num_teacher+=1

#     @classmethod
#     def get_num_teacher(cls):
#         return cls.__num_teacher


#     def get_full_name(self):
#         return f"Ismi {self.ism} , Familiyasi {self.familiya} , Sharifi {self.ochistva}"
#     def get_phone(self):
#         return self.telefon
#     def get_email(self):
#         return self.email
#     def get_study(self):
#         return self.bitirgan_universiteti
#     def get_mutaxasislik(self):
#         return self.__mutaxasislik
#     def get_info(self):    
#         return f"Ismi {self.ism} , Familiyasi {self.familiya} , Sharifi {self.ochistva},Mutaxasisligi {self.__mutaxasislik},Bitirgan universiteti {self.bititrgan_universiteti},Telefon raqami : {self.telefon}, Email: {self.email} "

# teacher1 = Teacher("Aziz","Aliyev","Akmalovich","Matematika","Uzbekistan Milliy universiteti",998999076564,"aziz@gmail.com")
# teacher2 = Teacher("Ali","Azizov","Akmalovich","Ona tili","Samarqand Milliy universiteti",998999076564,"aziz@gmail.com")
# teacher3 = Teacher("Akmal","Aliyev","Azizovich","Doktor","Guliston Milliy universiteti",998999076564,"aziz@gmail.com")


# # 2

# class Avto:

#     __num_avto=0    

#     def __init__(self,model,kompaniya,rang,yil,km = 0):
#         self.model = model
#         self.km = km
#         self.kompaniya = kompaniya
#         self.rang = rang
#         self.yil = yil
#         Avto.__num_avto+=1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
#     def get_model(self):
#         return self.model
#     def get_rang(self):
#         return self.rang
#     def get_kompaniya(self):
#         return self.kompaniya
#     def get_yil(self):
#         return self.yil
#     def update_km(self,c):
#          self.a+=c
#          return self.c
#     def set_km(self,r):
#          self.b = r
#          return self.r

# avto1 = Avto("Tracker", "GM","Qora",2022)
# avto2 = Avto("Malibu", "GM","Oq",2023)


# # 3

# import json

# talaba = {
#     'ism' : 'Azizbek ',
#     'yosh' : 20,
#     'oila' : True,
#     'farzandlar' : ("Bobour","Akmal","Akbar"),
#     'mashina' : True
# }

# t_json = json.dumps(talaba)
# print(t_json)

# with open("t_json" , "w") as f:
#     json.dump(talaba, f)


# filename = "t_json"
# with open(filename) as f:
#     talaba = json.load(f)
# print(talaba)
# print(type(talaba))

# #4

# def talaba_info(maktab,sinf,xona,qator,yil):
#     """..."""
#     talaba={
#         "maktab" : maktab,
#         "sinf": sinf,
#         "xona" : xona,
#         "qator": qator,
#         "yil": yil,

#     }
#     return talaba

# def talaba_kirit():
#     """..."""
#     talabalar=[]
#     while True:
#         print("\nQuyidagi ma`lumotlarni kiriting", end = "")
#         maktab = input("Maktab:")
#         sinf=input("Sinf:")
#         xona=input("Xona:")
#         qator=input("Qator:")
#         yil=input("Tug'ilgan yili:")

#         talabalar.append(talaba_info(maktab, sinf, xona, qator, yil))

#         d = input("Kiritshni istaysizm?")
#         if d== "no":
#             break
#     return talabalar

# sonlar = [1,7,4,8,4]
# for a in sonlar:
#     print(f"{a} * 8")

# # 5
# #  Dunder - bu tagida ikkita chiziqchali metodlar 
# # Misol:uuid4()
# #     __num_avto=0    

# #     def __init__(self,model,kompaniya,rang,yil,km = 0):
# #         self.model = model
# #         self.km = km
# #         self.kompaniya = kompaniya
# #         self.rang = rang
# #         self.yil = yil
# #         Avto.__num_avto+=1


# # 6
# from pprint import pprint
# import requests

# page = "https://kundalik.com/userfeed"
# a = requests.get(page)
# pprint(a)