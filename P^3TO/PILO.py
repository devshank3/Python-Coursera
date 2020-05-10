
import PIL
from PIL import Image
import inspect
print("PIL version used in this assignment is ** " + str(PIL.__version__)+" **\n")
data_path = "msi_recruitment.gif"
image = Image.open(data_path)
print("This is image object output : \n"+ str(image)+"\n")
print("This is the type of image : +\n" + str(type(image))+"\n")
image.show()
image.save("msi_recruitment.png")
image  = Image.open("msi_recruitment.png")
print("Fulldescription of object contained : \n"+ str(inspect.getmro(type(image)))+"\n")
from PIL import ImageFilter

image = image.convert("RGB")
image.show()
print("Fulldescription of object contained : \n"+ str(inspect.getmro(type(image)))+"\n")

Blurred_image = image.filter(ImageFilter.BLUR)
Blurred_image.show()

print("{}x{}".format(image.width,image.height))

img1 = image.crop((50,0,185,140))

img1.show()

from PIL import ImageDraw

drawing_object = ImageDraw.Draw(image)

drawing_object.rectangle((50,0,185,140), fill= None, outline="yellow")
image.show()

