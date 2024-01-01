import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://github.com/PF-Razzaq/Python_Crud/tree/master/Crud")
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='gray')
img.save('githubsite.png')
