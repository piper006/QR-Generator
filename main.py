import qrcode
from PIL import Image

url = "12345"
logo_path = ''
# taking base width (if you can only see the logo, reduce the base_width)
base_width = 100
filename_to_save = 'qr_code_with_logo.png'

logo = Image.open(logo_path)


# adjust image size
width_percent = (base_width / float(logo.size[0]))
height_size = int((float(logo.size[1]) * float(width_percent)))
logo = logo.resize((base_width, height_size), Image.BICUBIC)
qr_code = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# adding URL or text to QRcode
qr_code.add_data(url)

# generating QR code
qr_code.make()

# taking color name from user
qr_color = 'Black'

# adding color to QR code
qr_img = qr_code.make_image(
    fill_color=qr_color, back_color="white").convert('RGB')

# set size of QR code
pos = ((qr_img.size[0] - logo.size[0]) // 2,
       (qr_img.size[1] - logo.size[1]) // 2)
qr_img.paste(logo, pos)

# Save the final QR code image with the logo
qr_img.save(filename_to_save)
