class Manzil:
    """Manzilni saqlash uchun klass"""
    
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        """..."""
        info = f" {self.viloyat} viloyati , {self.tuman} tumani "
        info += f"{self.kocha} kochasi, {self.uy}-uy "
        return info
talaba_manzil=Manzil(12, "Tinchlik", "Boyovut", "Sirdaryo")
# talaba1=Talaba("Alijon", "GFA7843873487", 1998, "688676YT",talaba_manzil)
print(talaba_manzil.get_manzil())
