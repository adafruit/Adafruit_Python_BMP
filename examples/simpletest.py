# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import Adafruit_BMP.BMP085 as BMP085

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor = BMP085.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER, 
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
