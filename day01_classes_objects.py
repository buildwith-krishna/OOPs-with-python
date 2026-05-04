class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def call(self):
        print("\n<<- Calling Fucntion ->>")
        print(f"{self.brand} is calling")
        print(f"Model is : {self.model}")

class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os
        
    def browse(self):
        print("\n<<- Browsing Function ->>")
        print(f"Browsing on {self.brand} | OS : {self.os}")

class BasicPhone(Phone):      
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    def text(self):
        print("\n<<- Texting Function ->>")
        print(f"Texting from {self.brand}")

class Camera():
    def __init__(self, camera, MP):
        self.camera = camera
        self.MP = MP

    def taking_pics(self):
        print("\n<<- Camera Function ->>")
        print(f"Taking pictures from {self.camera}")
        print(f"Camera's MegaPixels are : {self.MP}")

brand = input("Enter brand name: ").strip()
model = input("Enter model: ").strip()
os  = input("Enter OS: ").strip()
camera = input("Enter camera name: ").strip()
MP = int(input("Enter camera's MegaPixels: ").strip())


p = Phone(brand, model)
p.call()

a = SmartPhone(brand, model, os)
a.browse()

b = BasicPhone(brand, model)
b.text()

c = Camera(camera, MP)
c.taking_pics()
