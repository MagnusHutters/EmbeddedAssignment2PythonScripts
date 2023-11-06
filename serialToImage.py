import serial
from PIL import Image

# Configure the serial connection settings
COM_PORT = '/dev/ttyUSB1'  # Replace with your COM port (e.g., 'COM3' for Windows)
BAUD_RATE = 115200  # Set your baud rate
IMAGE_WIDTH = 32  # Replace with the actual width of your image
IMAGE_HEIGHT = 32  # Replace with the actual height of your image

# Initialize an empty list to hold pixel data
pixels = []
# Open the serial port
with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
    # Read lines until we have enough pixel data
    while len(pixels) < IMAGE_WIDTH * IMAGE_HEIGHT:
        line = ser.readline().decode('utf-8').strip()
        # Assuming the line is a hex color in the format '0xRRGGBBAA'
        if line.startswith('0x'):
            # Convert the hex color to a tuple (R, G, B, A) and append to the list
            color = int(line, 16)
            r = (color >> 24) & 0xFF
            g = (color >> 16) & 0xFF
            b = (color >> 8) & 0xFF
            a = color & 0xFF
            pixels.append((r, g, b, a))
            print(f"Received pixel [{len(pixels)}]: {line}")

# Create an image from the pixel data
image = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT))
image.putdata(pixels)

# Save the image
image.save('output.png')
print("Image saved as output.png.")