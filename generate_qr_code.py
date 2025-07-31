import qrcode

def generate_qr_code(data, file_name="qr_code.png"):
    """
    Generate a QR code from the given data and save it as a PNG file.

    :param data: The data (URL or text) to be embedded in the QR code.
    :param file_name: The name of the output PNG file.
    """
    # Generate the QR code
    qr_img = qrcode.make(data)

    # Save the QR code image as a PNG file
    qr_img.save(file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    # Prompt the user to enter the data (URL or text)
    data = input("Enter the text or URL for the QR code: ")

    # Optional: Ask for the file name (default: qr_code.png)
    file_name = input("Enter the file name for the QR code (default: qr_code.png): ") or "qr_code.png"

    # Generate and save the QR code
    generate_qr_code(data, file_name)