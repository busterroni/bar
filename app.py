import web
import time
import json
import RPi.GPIO
import board
import neopixel
import random

urls = (
	'/', 'Index',
	'/pour', 'Pour',
)

app = web.application(urls, globals())
render = web.template.render('templates')

pixel_pin = board.D12
num_pixels = 18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

class Index:
	def GET(self):
		pixels.fill((random.randint(0, 255)))
		return render.index()

class Pour:
	def GET(self):
		RPi.GPIO.output(21, RPi.GPIO.HIGH)
		
		seconds = 30

		pixels.fill((0, 0, 0))

		time_per_pixel = seconds/num_pixels

		for i in range(num_pixels):
			pixels[i] = (0, 0, 255)

			time.sleep(time_per_pixel)

		RPi.GPIO.output(21, RPi.GPIO.LOW)

		return json.dumps({'success': True})

if __name__ == '__main__':
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(21, RPi.GPIO.OUT)
	app.run()



