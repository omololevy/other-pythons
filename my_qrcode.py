import io
import qrcode


qr = qrcode.QRcode()
qr.add_data("I love levy")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

