import qrcode
import datetime
import time

while True:
    ts = datetime.datetime.now()
    print(ts)
    with open('qr_code_text.txt', mode="w") as f:
        f.write("QR: " + str(ts))
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(ts)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')
    time.sleep(0.1)
