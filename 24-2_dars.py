class Shaxs:
    """Shaxslar haqida ma`lumot"""

    def __init__(self,ism,passport,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.passport=passport
        self.tyil=tyil

class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, passport, tyil,idraqam):
        super().__init__(ism, passport,tyil)
        self.idraqam=idraqam
        self.bosqich = 1
        self.ism=ism
        self.passport=passport
        self.tyil=tyil
    

    
class Fan(Talaba):
    def __init__(self, ism, passport, tyil,idraqam,nomi,baho,chorak):    
        super(). __init__(self, ism, passport, tyil)
        self.ism=ism
        self.passport=passport
        self.tyil=tyil
        self.nomi=nomi
        self.baho=baho
        self.chorak=chorak


        def set_baho(self,baho):
            self.baho=baho
        def get_baho(self):
            return self.baho
        def get_age(self,yil):
            "Talaba yoshini qaytuvchi metod"
            return yil - self.tyil
        def get_id(self):        
            return self.idraqam
        def get_manzil(self):
            return self.manzil

talaba1=Talaba("Alijon", "GFA7843873487", 1998, "688676YT")
matematika=Fan("Alijon", "GFA7843873487", 1998, "688676YT","oliy matematika",5,2 )

# print(matematika.set_baho())



