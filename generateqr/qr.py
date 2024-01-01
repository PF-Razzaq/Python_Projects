import qrcode as qr

img = qr.make('https://github.com/PF-Razzaq/Python_Crud/tree/master/Crud')

img.save('github.png')