import qrcode 
from PIL import Image # for formatting qr code image

# qrcode se data le rhe h and usme changes kr rhe h 
# QRCode is function to read PIL file that is used to change functionalities of qrcode and removing errors of qrcode
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,
border=10,)
qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=WL&index=13")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("youtube_Link2.png")