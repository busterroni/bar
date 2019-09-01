import sys
import time
import board
import neopixel

pixel_pin = board.D12
num_pixels = 18
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

seconds = sys.argv[1]

pixels.fill((0, 0, 0))

time_per_pixel = float(seconds) / num_pixels

for i in range(num_pixels):
	pixels[i] = (0, 0, 255)
	pixels.fill((random.randint(0, 255)))
	time.sleep(time_per_pixel)