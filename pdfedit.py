from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import os

poppler_path = r"E:\user\Release-21.03.0\poppler-21.03.0\Library\bin"
certificate_file = 'certificate.pdf'
image_file = 'out.jpg'

#obtain a jpg image from the pdf
images = convert_from_path(certificate_file, poppler_path = poppler_path)
images[0].save(image_file, 'JPEG')

#open the converted image anf the flag image using PIL module 
img = Image.open(image_file)
flag = Image.open('flag.jpg')

#load the pixel map of the certificate
pixels = img.load()

#replacement colour
colour = (232,236,239)

#colour over with background colour
for i in range(0, 950):
	for j in range(1616, 1950):
		if i not in range(837, 886) or j not in range(1606, 1656):
			img.putpixel((i,j), colour)

#insert flag
img.paste(flag, (180, 1616))

#display result
img.show()

#remove temporary file
os.remove(image_file)

#save result as pdf
img.save('certificate_edited.pdf', 'PDF' ,resolution=100.0)
