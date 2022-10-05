# For fb,wesbite,youtube video,link,even sentence,paytm qrcode etc using python
# Ist process -- directly genrate qr
# 2nd process - Border size,width, colors change ( how to change basic properties ) 
import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=WL&index=13")#qrcode generate
img.save("youtube_link.png")# QR code save as youtube_link.png (black and white)
#


