import os
from PIL import Image
import os, sys

img = Image.open('static/cat.jpg')
print(img.size)
img = img.crop((300,0,1024,682))
img = img.resize((80, 80))
img.save('cat.jpg')
img.show()

sys.exit()
folder = "nav/images"
for png in os.listdir(folder):
    image = Image.open(os.path.join(folder, png))
    image = image.resize((16,16))
    image.save(os.path.join(folder, "%s_1.png" % os.path.splitext(png)[0]))