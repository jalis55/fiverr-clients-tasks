class Rectangle:
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width

    def Perimeter(self):
        return 2*(self.length+self.width)
    def Area(self):
        return self.length * self.width

    def display(self):
        print(f"Length is {self.length}")
        print(f"Width is {self.width}")
        print(f"Perimeter of Rectange is {self.Perimeter()}")
        print(f"Area of Rectange is {self.Area()}")

class Parallelepiped(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def Volumne(self):
        return self.length * self.width * self.height




rec=Rectangle(7,5)

rec.display()

paral=Parallelepiped(7,5,2)

print(f"The Voulume of Parallelepiped is {paral.Volumne()}")