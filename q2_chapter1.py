from PIL import Image
import time


current_time = int(time.time())


generated_number_n = ((current_time % 100) * 50) + 50


if generated_number_n % 2 == 0:
    generated_number_n = generated_number_n - 10

print(generated_number_n)  


image = Image.open("chapter1.jpg")


pixels = image.load()

# width and height of chapter1.jpg
width, height = image.size

# variable to store the sum of modified red pixel values
total_red_sum = 0

# Iterate through each pixel
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]  # RGB values of each pixel

        # Calculate average brightness
        brightness = (r + g + b) / 3

        # Subtract instead of add if the image is bright 
        if brightness > 200:
            new_r = max(0, r - generated_number_n)
            new_g = max(0, g - generated_number_n)
            new_b = max(0, b - generated_number_n)
        else:
            
            new_r = max(0, min(255, r + generated_number_n))
            new_g = max(0, min(255, g + generated_number_n))
            new_b = max(0, min(255, b + generated_number_n))

        # Update the pixel with the new RGB values
        pixels[x, y] = (new_r, new_g, new_b)

        # Add the modified red value to the total sum
        total_red_sum += new_r

image.save("chapter1out.png")

print("Sum of modified red pixel values:", total_red_sum)