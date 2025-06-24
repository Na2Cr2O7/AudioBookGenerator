from PIL import Image   
from sys import argv 

img=[]
for x in argv[1:]:   
    img.append( Image.open(x)   )

concatenated_image_vertical = Image.new("RGB", (max(*[i.width for i in img]), sum([i.height for i in img])))
y_offset = 0
for i in img:
    concatenated_image_vertical.paste(i, (0, y_offset)) 
    y_offset += i.height
concatenated_image_vertical.save("concatenated_image_vertical.jpg")