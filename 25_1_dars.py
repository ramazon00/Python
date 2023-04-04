# INCAPSULATSIYA
# Meros dasturi
from uuid import uuid4

class Avto:
    """Avto klassi"""

    def __init__(self,make,model,rang,yil,narh=0,km=0):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.__narh=narh
        self.__km=km
        self.__id=uuid4()
    def get_narh(self):
        return self.__narh        
    def add_narh(self,narh):
        """Avtomobil kmga yana km qoshish"""
        if narh >=0:
            self.__narh=narh
        else:
              return "Narhni kamaytirib bo'lmaydi"   
    def get_km(self):
        return  self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Avtomobil kmga yana km qoshish"""
        if km >=0:
            self.__km+=km
        else:
              return "Mashina km kamaytirib bo'lmaydi"   
avto1=Avto("GM", "Malibu", "qora", 2022 )


class Avto:
    """Avtomobil klassi"""
  
    __num_avto=0

# Necha marta klass ishlatilgan ekanligini bildiradi
    def __init__(self,make,model,rang,yil,narh=0,km=0):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.__narh=narh
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    def get_narh(self):
        return self.__narh        
    def add_narh(self,narh):
        """Avtomobil kmga yana km qoshish"""
        if narh >=0:
            self.__narh=narh
        else:
              return "Narhni kamaytirib bo'lmaydi"   
    def get_km(self):
        return  self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Avtomobil kmga yana km qoshish"""
        if km >=0:
            self.__km+=km
        else:
              return "Mashina km kamaytirib bo'lmaydi"   
avto1=Avto("GM", "Malibu", "qora", 2022 )

print(avto1.get_num_avto())