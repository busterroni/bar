import sys
import time
import board
import neopixel

pixel_pin = board.D12
num_pixels = 22
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
pixels.fill((0, 0, 0))

seconds = sys.argv[1]
time_per_pixel = float(seconds) / num_pixels

for i in range(num_pixels):
	pixels[i] = (0, 0, 255)
	time.sleep(time_per_pixel)