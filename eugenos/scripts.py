import os 
from PIL import Image
import time
t=time.time()

image_dir="C:/Users/jalis/Desktop/fiverr/eugenos/image/"
text_dir="C:/Users/jalis/Desktop/fiverr/eugenos/text/"
output_dir="C:/Users/jalis/Desktop/fiverr/eugenos/output/"
print("processing",end=" ")
for img,text in zip(os.listdir(image_dir),os.listdir(text_dir)):
    print("#",end=" ")
    if img.endswith(".png") and text.endswith(".png"):

        background = Image.open(image_dir+img)
        foreground = Image.open(text_dir+text)
        background.paste(foreground, (0, 0), foreground)
        new_img_name=img.split('.')[0]+text.split('.')[0]+'.png'
        background.save(output_dir+new_img_name)

print("\nThis is done")

print(time.time()-t)