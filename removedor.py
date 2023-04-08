from rembg import remove
from PIL import Image

img = Image.open('example.jpg')
#removendo fundo
img_sem_fundo = remove (img)

#salvando
img_sem_fundo.save('imgsf.png')