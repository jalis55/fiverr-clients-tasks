import os 
from PIL import Image

path=os.path.dirname(__file__)

img_folder_name='image'
text_folder_name='text'
output_folder='output'

image_dir=os.path.join(path, img_folder_name)
text_dir=os.path.join(path,text_folder_name)
output_dir=os.path.join(path,output_folder)


print("processing",end=" ")
for img,text in zip(os.listdir(image_dir),os.listdir(text_dir)):

    print("#",end=" ")
    if img.endswith(".png") and text.endswith(".png"):
        background=Image.open(os.path.join(image_dir,img))
        foreground=Image.open(os.path.join(text_dir,text))
        background.paste(foreground, (0, 0), foreground)
        new_img_name=img.split('.')[0]+'_'+text.split('.')[0]+'.png'
        background.save(os.path.join(output_dir,new_img_name))

print("\nThis is done")


