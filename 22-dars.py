# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self,ism,familiya,tyil,tel):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.tel=tel
#     def get_f_name(self):
#         return f"Toliq ismim {self.ism} {self.familiya}"
#     def get_tel(self):
#         return self.tel
#     def tanishtir(self):
#         print(f"""Ismim {self.ism}, Familiyam {self.familiya}, {self.tyil}-yil tug'ilganman,{self.tel}""")

# talaba1=Talaba("Alijon","Aliyev",2002,989909798)
# talaba2=Talaba("Xusan","Umarov",2000,999909789)

# print(talaba1.ism)
# print(talaba1.familiya)
# talaba2.tanishtir()

# talaba2=Talaba("Olim","Hakimov",1999,899942020)
# talaba2.tanishtir()
# talaba3=Talaba("Husan","Akbarov",1998,909870998)


# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"Toliq ismim {self.ism} {self.familiya}"
#     def get_age(self,yil):
#         "Talaba yoshini qaytaradi"
#         return yil - self.tyil
#     def tanishtir(self):
#         print(f"""Ismim {self.ism}, Familiyam {self.familiya}, {self.tyil}-yil tug'ilganman""")


# talaba1=Talaba("Olim","Hakimov",1999)
# print(talaba1.get_fullname())
# print(talaba1.get_age(2022))

class Avto:
    """Avto nomli klass yaratamiz"""
    def __init__(self,kompaniyasi,modeli,km,dtraqami):
        """Avtonig xususiyatlari"""
        self.kompaniyasi=kompaniyasi
        self.modeli=modeli
        self.km=km
        self.dtraqami=dtraqami
    def get_name(self):
        return f"Kompaniyasi {self.kompaniyasi}"
    def get_lastname(self):    
        return f"Modeli {self.modeli}"
    def get_km(self):
        return f"Yurgan yo'li {self.km}"
    def get_tel(self):
        return f"Davlat raqami {self.dtraqami}"

avto1=Avto("GM","Malibu",27000,899)





















