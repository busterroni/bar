import time
import random
import board
import neopixel

pixel_pin = board.D12
num_pixels = 22
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
pixels.fill((0, 0, 0))

while True:
	pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
	time.sleep(0.5)