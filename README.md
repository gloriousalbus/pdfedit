## Steps to run:
1. Download this code by clicking the green coloured download code button above and clicking download zip, and unzip it to your required location.
2. Copy your certificates to this location. If you want to edit just one pdf,  pass the name of the certificate as an argument. For multiple pdfs at once, pass 'a' or 'all' as argument. If you don't want to use arguments, ensure the name of the file is "certificate.pdf".
3. Install python from https://www.python.org/downloads/ (I ran it using version 3.9, it should work normally on any other version as well)
4. Install pdf2image and PIL modules using `pip install -r requirements.txt`.
5. pdf2image requires poppler as described [here](https://github.com/Belval/pdf2image).
   Once installed, set the path of poppler in the poppler_path variable in pdfedit.py.
5. Install PIL module using `pip install `. 
6. Run the code from commandline using `python pdfedit.py` with a subsequent argument as described in step 2. 

The result should look like below:
![result image](https://raw.githubusercontent.com/gloriousalbus/pdfedit/main/res.jpg)
