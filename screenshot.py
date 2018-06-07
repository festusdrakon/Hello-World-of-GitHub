#seven seconds to screenshot

import graphics, e32, time

print "looks like this is working"


def screenshot():
	img = graphics.screenshot()
	img.save(u"E:\\Images\Screenshot.png")

timer = e32.Ao_timer()
interval = 7.0

g = raw_input("GO?")
if g == 'GO.':
	timer.after(interval, screenshot)