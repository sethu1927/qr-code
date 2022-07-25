import image
from numpy import source
import qrcode 
qr = qrcode.QRCode(
    version=15,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=5,
)
qr.add_data('source/GF_FD_02_KeyArt_4k.png')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save('D:/NEt/python/qr-code/OUTPUT/newone.png')