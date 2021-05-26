## Steps to run:
1. Download this code by clicking the green coloured download code button above and clicking download zip, and unzip it to your required location.
2. Copy your certificate to this location. Make sure the name of the file is "certificate.pdf". You can also edit the code to accept any other file name. 
3. Install python from https://www.python.org/downloads/ (I ran it using version 3.9, it should work normally on version 2 as well)
4. Install pdf2image module using `pip install pdf2image`. It requires poppler as described [here](https://github.com/Belval/pdf2image).
   Once installed, set the path of poppler in the poppler_path variable in pdfedit.py.
4. Install PIL module using `pip install pillow`. 
5. Run the code from commandline using `python pdfedit.py`. 

The result should look like below:
![result image](https://raw.githubusercontent.com/gloriousalbus/pdfedit/main/res.jpg)
