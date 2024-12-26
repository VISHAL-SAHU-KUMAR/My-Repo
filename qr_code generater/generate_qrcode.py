import qrcode

def generate_qr(data, filename):
    """
    Generate a QR code and save it as an image.
    
    Parameters:
    data (str): The data to encode in the QR code.
    filename (str): The filename to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    # Replace 'Hello, World!' with your data
    data = input("Enter the data for the QR code: ")
    filename = input("Enter the filename (e.g., qr.png): ")
    generate_qr(data, filename)
