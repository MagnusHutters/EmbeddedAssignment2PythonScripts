from PIL import Image
import numpy as np


def png_to_c_array(png_path):
    # Open the PNG image and convert it to RGBA (in case it is RGB or else)
    with Image.open("image.png") as img:
        rgba_img = img.convert('RGBA')

    # Convert the image to raw data
    raw_data = np.array(rgba_img)

    # Initialize the C array string
    c_array_string = "u32 raw_pixel_data[] = {\n"

    # Process the raw data
    for row in raw_data:
        for pixel in row:
            # Convert the pixel to 0xRRGGBBAA format
            r, g, b, a = pixel
            c_array_string += f"    0x{r:02X}{g:02X}{b:02X}{a:02X},\n"

    # Remove the last comma and add closing bracket
    c_array_string = c_array_string.rstrip(',\n') + "\n};"

    return c_array_string


# Replace 'input.png' with the path to your PNG file
c_array_output = png_to_c_array('input.png')

# Save to a text file that can be included in a C script
with open('output_c_array.txt', 'w') as file:
    file.write(c_array_output)

print("The PNG has been converted to a C array and saved to output_c_array.txt")
