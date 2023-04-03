class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"Ism familiyam {self.ism} {self.familiya} {self.tyil}- yil tug'ilganman. {self.bosqich}-bosqichda o'qiyman"
    def set_bosqich(self,bosqich):
        """Talaba kursini yangilovchi me'tod"""
        self.bosqich = bosqich
    def update_bosqich(self):
        """Talaba kursini 1taga ko'paytirish"""
        self.bosqich += 1

# talaba1=Talaba("Olim","Hakimov",1999)
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())


class Fan():
    """Fan nomli klass yaratamiz"""

    def __init__(self,nomi):
        """Fanning xususiyatlari"""
        self.nomi=nomi
        self.talabalar_soni = 0
        self.talabalar=[]
    def add_students(self, talaba):
        """Talabalar qo'shish"""        
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def get_name(self):
        return self.nomi
    def get_talabalar(self):
        return self.talabalar
    def get_students(self):
        return [x.get_info() for x in self.talabalar]
    


matematika=Fan("Oliy matematika")

talaba1=Talaba("Olim","Hakimov",1999)
talaba2=Talaba("Alijon","Aliyev",2002)
talaba3=Talaba("Xusan","Umarov",2000)

talaba1.update_bosqich()
talaba2.update_bosqich()
talaba3.update_bosqich()

matematika.add_students(talaba1)
matematika.add_students(talaba2)
matematika.add_students(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)

talabalar_list=matematika.get_students()
# print(talabalar_list)




def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('_') is False]

print(see_methods(Talaba))
print(see_methods(talaba1))

print(talaba1.__dict__)

print(talaba1.__dict__.keys())
print(talaba1.__dict__.values())

















































