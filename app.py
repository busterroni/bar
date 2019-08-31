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
web.config.debug = True
pixel_pin = board.D12
num_pixels = 18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

drink_data = json.load(open('static/drinks.json', 'r'))

class Index:
	def GET(self):
		pixels.fill((random.randint(0, 255)))
		return render.index()

class Pour:
	def GET(self):
		data = web.input()

		if data['pump-id'].startswith('pump-'):
			pump = data['pump-id'].replace('pump-', '')
		elif data['pump-id'].startswith('mixed-drink-'):
			pump = data['pump-id']

		pins = []

		if pump.isdigit():
			pins.append(drink_data['pump-pin'][pump])
		else:
			if pump == "Jack & Coke":
				jack_drink = get_drink("Jack Daniel's")
				coke_drink = get_drink("Coca Cola")

				# pins.append(drink_data['pump-pin'][jack_drink['pump']])
				# pins.append(drink_data['pump-pin'][jack_drink['pump']])
		print pins
		seconds=10
		pixels.fill((0, 0, 0))
		time_per_pixel = float(seconds) / num_pixels

		for pin in pins:
			RPi.GPIO.output(21, RPi.GPIO.HIGH)

			for i in range(num_pixels):
				pixels[i] = (0, 0, 255)
		
				time.sleep(time_per_pixel)
				
			RPi.GPIO.output(21, RPi.GPIO.LOW)

		pixels.fill((random.randint(0, 255)))

		return json.dumps({'success': False})

def get_drink(name):
	for drink in drink_data['drinks']:
		if drink['name'] == name:
			return drink

if __name__ == '__main__':
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(21, RPi.GPIO.OUT)
	app.run()



