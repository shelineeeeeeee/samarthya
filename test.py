class car:
    def __init__(self,brand,colour,hp):
        self.brand=brand
        self.colour = colour
        self.hp=hp
    def myfunc(self):
        print(f"brand of my car is {self.brand} and colour is {self.colour} and hp {self.hp}")
    def __str__(self):
        return "Brand:"+ self.brand+ ",colour:" + str(self.colour) +",hp:" +str(self.hp)
p1=car ("bmw","white",360)
p1.myfunc()
print(p1)


























