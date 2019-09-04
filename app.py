import web
import time
import json
import RPi.GPIO
import subprocess
import random

urls = (
	'/', 'Index',
	'/pour', 'Pour',
)

app = web.application(urls, globals())
render = web.template.render('templates')
web.config.debug = True

drink_data = json.load(open('static/drinks.json', 'r'))
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(21, RPi.GPIO.OUT)
RPi.GPIO.setup(20, RPi.GPIO.OUT)
RPi.GPIO.setup(16, RPi.GPIO.OUT)
RPi.GPIO.setup(26, RPi.GPIO.OUT)
RPi.GPIO.output(21, RPi.GPIO.HIGH)
RPi.GPIO.output(20, RPi.GPIO.HIGH)
RPi.GPIO.output(16, RPi.GPIO.HIGH)
RPi.GPIO.output(26, RPi.GPIO.HIGH)


class Index:
	def GET(self):
		subprocess.Popen(['python3', 'light_led.py'])
		return render.index()

class Pour:
	def GET(self):
		data = web.input()

		if data['pump-id'].startswith('pump-'):
			pump = data['pump-id'].replace('pump-', '')
		elif data['pump-id'].startswith('mixed-drink-'):
			pump = data['pump-id'].replace('mixed-drink-', '')

		pins = []

		if pump.isdigit():
			pins.append(drink_data['pump-pin'][pump])
		else:
			if pump == "Jack & Coke":
				jack_drink = get_drink("Jack Daniel's")
				coke_drink = get_drink("Coca Cola")

				# pins.append(50)
				pins.append(50)

				# pins.append(drink_data['pump-pin'][jack_drink['pump']])
				# pins.append(drink_data['pump-pin'][jack_drink['pump']])

		seconds=3

		subprocess.Popen(['python3', 'light_led_time.py', str(seconds)])

		for pin in pins:
			RPi.GPIO.output(21, RPi.GPIO.LOW)

			time.sleep(seconds)

			RPi.GPIO.output(21, RPi.GPIO.HIGH)

		return json.dumps({'success': False})

def get_drink(name):
	for drink in drink_data['drinks']:
		if drink['name'] == name:
			return drink

if __name__ == '__main__':
	app.run()



