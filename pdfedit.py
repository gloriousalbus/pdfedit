from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import os
import sys
poppler_path = r"C:\pdfedit-main\poppler-21.03.0\Library\bin"

# if you want to edit all pdfs together, use 'python pdfedit.py a' or 'all', else 'python pdfedit.py certificatename.py'
def getcertificatenames():
	certificates = list()
	if len(sys.argv) == 2:
		if sys.argv[1] == 'a' or sys.argv[1] == 'all':
			for file in os.listdir("./"):
				if file.split('.')[-1] == 'pdf':
					certificates.append(file)
		else:
			try:
				splitname = sys.argv[1].split('.')
				if len(splitname) >= 2:
					if splitname[-1] == 'pdf':
						print("pdf")
						certificates.append(sys.argv[1])
			except:
				certificates.append('certificate.pdf')
	else:
		certificates.append('certificate.pdf')
	return certificates

certificates = getcertificatenames()
print(f"Number of pdfs found: {len(certificates)}")
image_file = 'out.jpg'

# make 'edited' directory as destination
if not os.path.exists('edited'):
    os.makedirs('edited')

#open the flag image using PIL module 
with Image.open('flag.jpg') as flag:
	
	for certificate in certificates:
		print(certificate, end="\t")

		#obtain a jpg image from the pdf
		images = convert_from_path(certificate, poppler_path = poppler_path)
		images[0].save(image_file, 'JPEG')

		#open the converted image using PIL module 
		with Image.open(image_file) as img:
			
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

			#display result, only if amending one certificate
			if len(certificates) == 1:
				img.show()

			#remove temporary file
			os.remove(image_file)
			
			# savename is filename_edited
			savename = os.path.splitext(certificate)[0]

			#save result as pdf
			img.save(f'./edited/{savename}_edited.pdf', 'PDF' ,resolution=100.0)
			
			print("Done")


