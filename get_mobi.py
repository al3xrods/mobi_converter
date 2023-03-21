import os
import glob
import shutil
import time
import os

path = "C:\\Downloads\\"
moveto = "C:\\Documents\\Calibre Books\\"

files = os.listdir(path)
try:
    for f in files:
        if f.endswith('.epub'):
            scr = path + '\\' +f
            dest = moveto + '\\'+f
            os.replace(scr, dest)

    print('Epub Files Transfered Succesfully.')
except:
    print('Epub Files not found.')
        
#================================================= 
# Calibre Book Conversion
os.system('start "" "' + r"C:\Program Files\Calibre2\calibre.exe" + '"') #Open Calibre
time.sleep(10)
input = str(input('Transfer Books? (Y/N) ')).lower()

books_path = "C:\\Users\\97254\\Downloads\\New Folder"
files_path = list(glob.glob(books_path+"\**\*", recursive=True))

if input == 'y':
    try:
        for file in files_path: # get all files in 'New Folder'.
            if file.endswith('.mobi'): # Check file extension.
                shutil.move(file, path) # move all .azw3 files to Downloads folder.
        print('Converted books tranfered.')
        time.sleep(2)
        os.system("taskkill /f /im calibre.exe") # Terminate Calibre
        time.sleep(1)
        
    except:
        print('Files Not Found.')
        
shutil.rmtree(books_path)
