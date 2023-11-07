import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://egojsdev.netlify.app"
data2 = "https://linkedin.com/in/godwinego"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")

# for data 2
qr.add_data(data2)
qr.make(fit=True)
img2 = qr.make_image(fill="black", back_color="white")
img.save("data2.jpg")