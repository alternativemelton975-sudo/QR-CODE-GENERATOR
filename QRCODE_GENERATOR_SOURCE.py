import qrcode 

def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    text = "https://b001.io"
    file_name = "qr_code.png"
    generate_qr_code(text, file_name)
    print(f"QR code saved as {file_name}")
