import time
import random
import board
import neopixel

pixel_pin = board.D12
num_pixels = 18
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

while True:
	pixels.fill((random.randint(0, 255)))
	time.sleep(10)