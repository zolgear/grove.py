'''
Test: grove_ledbar 

    original <https://github.com/mcauser/micropython-my9221/blob/master/my9221_test.py>
'''
import time
from grove_ledbar import GroveLedBar

# connect to pin 5 (slot D5)
PIN = 5
ledbar = GroveLedBar(PIN)

# all LEDS on, full brightness
ledbar.level(10)

time.sleep(1)

# four LEDS on, half brightness
ledbar.level(4, 0x0F)

time.sleep(1)

# reverse orientation, first LED is green
ledbar.reverse = True
ledbar.level(1)

time.sleep(1)

# normal orientation, first LED is red
ledbar.reverse = False
ledbar.level(1)

time.sleep(1)

# switch on specific leds
ledbar.bits(0b1111100000)
time.sleep(1)

ledbar.bits(0b0000011111)
time.sleep(1)
ledbar.bits(1)
time.sleep(1)
ledbar.bits(3)
time.sleep(1)
ledbar.bits(7)
time.sleep(1)

# first and last LED on, very dim
ledbar.bits(513, 7)
time.sleep(1)

# alternating LEDs
ledbar.bits(0b0101010101)
time.sleep(1)
ledbar.bits(0b1010101010)
time.sleep(1)
buf = b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff'
ledbar.bytes(buf)
time.sleep(1)

# fade out LEDs
buf = bytearray([0,1,3,7,15,31,63,127,255,255])
ledbar.reverse = True
ledbar.bytes(buf)
time.sleep(1)
ledbar.reverse = False
ledbar.bytes(buf)
time.sleep(1)

# various brightnesses
buf = [0,0,0,0,0,255,127,63,15,7]
ledbar.bytes(buf)
time.sleep(1)

# cycle through LEDS with various brightnesses
buf = [0,1,3,7,15,31,63,127,255,255]
for i in range(50):
    buf.insert(0,buf.pop())
    ledbar.bytes(buf)
    time.sleep(.01)

# random LEDs
import random
for i in range(100):
    ledbar.bits(random.getrandbits(10))
    time.sleep(.01)

# walk through all possible LED combinations
for i in range(1024):
    ledbar.bits(i)
    time.sleep(.001)

# Use 8bit greyscale mode (default)
# LED brightness 0x00-0xFF
ledbar._write16(0x00) # command
ledbar._write16(0xFF) # led 1
ledbar._write16(0xFF) # led 2
ledbar._write16(0x00) # led 3
ledbar._write16(0x00) # led 4
ledbar._write16(0x00) # led 5
ledbar._write16(0xFF) # led 6
ledbar._write16(0xFF) # led 7
ledbar._write16(0x00) # led 8
ledbar._write16(0x00) # led 9
ledbar._write16(0x00) # led 10
ledbar._write16(0x00) # unused channel, required
ledbar._write16(0x00) # unused channel, required
ledbar._latch()
time.sleep(1)

# Use 12bit greyscale mode
# LED brightness 0x000-0xFFF
ledbar._write16(0x0100) # command
ledbar._write16(0x0FFF) # led 1
ledbar._write16(0x0000) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x000F) # led 5
ledbar._write16(0x000F) # led 6
ledbar._write16(0x0000) # led 7
ledbar._write16(0x00FF) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0FFF) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()
time.sleep(1)

# Use 14bit greyscale mode
# LED brightness 0x000-0x3FFF
ledbar._write16(0x0200) # command
ledbar._write16(0x3FFF) # led 1
ledbar._write16(0x03FF) # led 2
ledbar._write16(0x0000) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x0000) # led 5
ledbar._write16(0x003F) # led 6
ledbar._write16(0x0003) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()
time.sleep(1)

# Use 16bit greyscale mode
# LED brightness 0x0000-0xFFFF
ledbar._write16(0x0300) # command
ledbar._write16(0xFFFF) # led 1
ledbar._write16(0x0FFF) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x000F) # led 4
ledbar._write16(0x0007) # led 5
ledbar._write16(0x0003) # led 6
ledbar._write16(0x0001) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()
time.sleep(1)
