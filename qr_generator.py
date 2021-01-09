import qrcode
import datetime

ts = datetime.datetime.now().timestamp()

while True:
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(ts)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # img.show('qrcode001.png')
    img.save('asd.png')
