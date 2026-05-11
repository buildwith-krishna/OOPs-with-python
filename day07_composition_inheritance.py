class Camera():
    def __str__(self):
        return "Camera!"

    def pics(self):
	    return "Took a pic!"
			
class Phone():
	def __init__(self):
		self.camera = Camera()

	def __str__(self):
	    return f"Phone with camera : {self.camera}"
			
	def pics(self):
		self.camera.pics()

			
c = Camera()
p = Phone()
print(c.pics())
print(p)

