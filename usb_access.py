# Currently programmed to send the word Test to the LCD screen through the arduino.
# When executed, the system reports that the resource is busy.
# Arduino needs to be programmed to receive signals from the Pi, and pass them on to the LCD screen
# as well as transmitting keypad presses to the Pi. In progress... 3/1/13 3AM

import usb.core
import usb.util

# Find Keypad
dev = usb.core.find(idVendor = 0x2341, idProduct = 0x0043)

# Check if found
if dev is None:
 raise ValueError('Device not found')

# Set Active Configuration
dev.set_configuration()

# Get endpoint instance
cfg = dev.get_active_configuration
interface_number = cfg [(0,0)],bInterfaceNumber
alternate_setting = usb.control.get_inter(interface_number)
intf = usb.util.find_descriptor(cfg, bInterfaceNumber = interface_number, bAlternateSetting = alternate_setting)

ep = usb.util.find_descriptor( intf, custom_match =  lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_Out)

assert ep is not None

# Write Data
ep.write('Test')