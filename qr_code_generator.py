import qrcode as qr
from PIL import Image

# img = qr.make("https://www.python.org/")
# img.save("Daniyal_Akhtar.png")



# Create the QR code object with specified parameters
qr_var = qr.QRCode(
    version=1, 
    error_correction=qr.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4
)

# Add data to the QR code
qr_var.add_data("https://seavycloudinc.com/")

# Generate the QR code
qr_var.make(fit=True)

# Create an image from the QR code with custom colors
img = qr_var.make_image(fill_color="red", back_color="blue")

# Save the image to a file
img.save("Seavy_Cloud.png")
