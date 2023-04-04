class Shaxs:
    """Shaxslar haqida ma`lumot"""

    def __init__(self,ism,passport,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        """Shaxs haqida ma`lumot"""
        info = f"Ismim {self.ism} "
        info+=f"Pasport raqamim {self.passport} {self.tyil}-yili tug'ilganman"
        return info
    def get_age(self,yil):
        "Shaxs yoshini qaytuvchi metod"
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, passport, tyil,idraqam,manzil):
        super().__init__(ism, passport, tyil)
        self.ism=ism
        self.passport=passport
        self.tyil=tyil     
        self.idraqam=idraqam
        self.bosqich = 1
        self.manzil=manzil
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Shaxs haqida ma`lumot"""
        info = f"Ismim {self.ism} ."
        info+=f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam} "
        return info


class Manzil:
    """Manzilni saqlash uchun klass"""
    
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        """..."""
        info = f" {self.viloyat} viloyati ,  {self.tuman} tumani "
        info += f"{self.kocha} kochasi, {self.uy}-uy "
        return info
# talaba_manzil=Manzil(12, "Tinchlik", "Boyovut", "Sirdaryo")
# talaba1=Talaba("Alijon", "GFA7843873487", 1998, "688676YT",talaba_manzil)
































