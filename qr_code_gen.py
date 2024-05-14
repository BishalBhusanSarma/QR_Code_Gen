import qrcode

def generate_qr_code(data, file_path, version=7, box_size=10, border=5):
    try:
        qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(file_path)
        print(f"QR code saved as {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    data = input("Enter Your Link or Data Here:\n")
    file_path = "testQR.png"
    generate_qr_code(data, file_path)



