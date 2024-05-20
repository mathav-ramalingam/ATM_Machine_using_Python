import qrcode

def generate_qr(url,filename):

    qr = qrcode.QRCode(
        version=1,      #size of the QR Code 
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # controls the error correction used for the QR Code
        box_size=10,         #how many pixels each “box” of the QR code is
        border=3,            #how many boxes thick the border
    )
    
    #Create QR code
    qr.add_data(url)

    #Generate QR code image
    img = qr.make_image(fill="black", back_color="white")
    
    #Save the image
    img.save(filename)

    # Display the QR code image
    img.show()
    

if __name__ == "__main__":
    url = input("Enter the Url or Text to encode in the QR code: ")
    filename = input("Enter the filename to save the QR image : ")
    generate_qr(url,filename)