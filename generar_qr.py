import qrcode

# Sustituye esta URL por la de tu GitHub Pages
url = "https://github.com/danaliz1808-droid/biorreactor-simulador.git"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("simulador_qr.png")

print("✅ Código QR generado: simulador_qr.png")
print(f"➡ Escanéalo para abrir: {url}")
