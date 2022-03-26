from PIL import Image

background = Image.open("1.png")
foreground = Image.open("2.png")

background.paste(foreground, (0, 0), foreground)
# background.show()
background.save('finall.png')
