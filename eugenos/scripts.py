from cgitb import text
from PIL import Image

# background = Image.open("1.png")
# foreground = Image.open("2.png")

# background.paste(foreground, (0, 0), foreground)
# # background.show()
# background.save('finall.png')

    #import necessary packages 
 
import os 

 
     
# import os
image_dir="C:/Users/jalis/Desktop/fiverr/eugenos/image/"
text_dir="C:/Users/jalis/Desktop/fiverr/eugenos/text/"
output_dir="C:/Users/jalis/Desktop/fiverr/eugenos/output/"

for img,text in zip(os.listdir(image_dir),os.listdir(text_dir)):
    if img.endswith(".png") and text.endswith(".png"):

        # print(img.split('.')[0])
        background = Image.open(image_dir+img)
        foreground = Image.open(text_dir+text)
        background.paste(foreground, (0, 0), foreground)
        new_img_name=img.split('.')[0]+text.split('.')[0]+'.png'
        background.save(output_dir+new_img_name)



