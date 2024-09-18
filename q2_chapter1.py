from PIL import Image
import time
'''
STEP 1: Run the provided code to reveal number based on real-time
Added variable 'formatted_time' is added to show the time the code was run
'''
# Get the current Unix time
current_time = int(time.time())

# Format the Unix time to a human-readable format
formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))

# Generate a number based on the current time
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Print the result with the formatted time
print(f"Number {generated_number} was generated at {formatted_time}")

'''
STEP 2: Adjust the image
'''
image_path = "chapter1.jpg"
image = Image.open(image_path)
pixels = image.load()

# Iterate over each pixel and modify the RGB values by adding the generated number
width, height = image.size
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        # Add generated_number to each channel, ensuring values are within 0-255
        r = min(255, r + generated_number)
        g = min(255, g + generated_number)
        b = min(255, b + generated_number)
        pixels[x, y] = (r, g, b)

# Save the modified image
output_image_path = "chapter1out.png"
image.save(output_image_path)

# Print the result
print(f"Modified image saved as {output_image_path}")

'''
OUTPUT:
Number 141 was generated at 2024-09-18 20:49:51
Modified image saved as chapter1out.png
'''