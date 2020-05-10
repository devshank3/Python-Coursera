import PIL
from PIL import Image
import inspect
dir_path = "msi_recruitment.gif"

image = Image.open(dir_path)

print("Fulldescription of object contained : \n"+ str(inspect.getmro(type(image)))+"\n")

image = image.convert("RGB")

print("Fulldescription of object contained : \n"+ str(inspect.getmro(type(image)))+"\n")
#image.show()

from PIL import ImageEnhance

e = ImageEnhance.Brightness(image)

images = []

for i in range(0,10):
    images.append(e.enhance(i/10))

for i in range(0,10):
    print(images[i])
    #images[i].show() 

first_image = images[0]

contactsheet = Image.new(first_image.mode,  (first_image.width,10*first_image.height))

#contactsheet.show()


print("Fulldescription of object contained : \n"+ str(inspect.getmro(type(contactsheet)))+"\n")
print(contactsheet)

cur_location = 0

for i in images:
    contactsheet.paste(i,(0,cur_location))
    cur_location = cur_location+450

#contactsheet.show()

contactsheet = contactsheet.resize((160,900))
#contactsheet.show()

grid = Image.new("RGB",(first_image.width*3,first_image.height*3))

x = 0
y= 0 

for img in images[1:]:
    grid.paste(img,(x,y))
    if x+first_image.width == grid.width:
        x=0
        y= y+first_image.height
    else:
        x = x+first_image.width

grid = grid.resize((int(grid.width/2),int(grid.height/2)))
grid.show()
