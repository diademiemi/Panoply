# How often the display refreshes
DISPLAY_REFRESH_RATE = 0.25
# How often information on the device is polled (Date, time)
LOCAL_REFRESH_INTERVAL = 0.5
# How often information over web requests is polled (Home Assistant)
WEB_REFRESH_INTERVAL = 30

# Put your display resolution here
DISPLAY_WIDTH = 64
DISPLAY_HEIGHT = 64
# If you need any rotation, specify this as a multiple of 90, otherwise leave it at 0
DISPLAY_ROTATION = 0
# Display mapping, read https://github.com/hzeller/rpi-rgb-led-matrix#changing-parameters-via-command-line-flags
DISPLAY_HARDWARE_MAPPING = "adafruit-hat"

# Format used for %time%
TIME_FORMAT = "%H:%M:%S"
# Format used for %date%
DATE_FORMAT = "%Y-%m-%d"

# Path to font files, NEEDS TO BE "BDF" bitmap fonts!
TINY_FONT = "../fonts/Tiny-4x6.bdf"
SMALL_FONT = "../fonts/Small-5x7.bdf"
LARGE_FONT = "../fonts/PixeloidMono.bdf"

# URL of your Home Assistant instance
HOME_ASSISTANT_URL = "https://home.example.com"
# Long-lived access token
HOME_ASSISTANT_KEY = "ABCDEF"

# Dict of Home Assistant entities to track the state of
# '<new placeholder name>' : '<home assistant entity>' 
HOME_ASSISTANT_ENTITY_STATES = {
    'temp' : 'sensor.room_temperature',
    'phonebattery' : 'sensor.phone_battery_level'
}

# Layout settings
# Here you can customise the location and content of text elements or place shapes

# AVAILABLE TEXT PLACEHOLDERS:
# %time% - Replaced with the current time
# %date% - Replaced with the current date
# And any entities defined from Home Assistant

# Large text, using the PixeloidMono font
# '<text %placeholder%>' : (<x position top-left>, <y position top-left>, (<red>, <green>, <blue>))
LARGE_TEXT_ELEMENTS = {
    '%time%' : (2, 9, (200, 200, 200)),
    '%temp%' : (2, 38, (200, 200, 200))
}

# Small text, using the 5x7 font
# '<text %placeholder%>' : (<x position top-left>, <y position top-left>, (<red>, <green>, <blue>))
SMALL_TEXT_ELEMENTS = {
    '%date%' : (2, 18, (200, 200, 200)),
    'it is' : (2, 30, (200, 200, 200))
}

# Tiny text, using the 4x6 font
# '<text %placeholder%>' : (<x position top-left>, <y position top-left>, (<red>, <green>, <blue>))
TINY_TEXT_ELEMENTS = {
    'c' : (27, 38, (200, 200, 200)),
    'Hello, world!' : (2, 56, (200, 200, 200))
}

# Place a horizontal line, starting from the left
# (<x position top-left>, <y position top-left>, <length> (<red>, <green>, <blue>))
HORIZONTAL_LINES = [
    (0, 10, 64, (200, 0, 0)),
]

# Place a vertical line, starting from the top
# (<x position top-left>, <y position top-left>, <length> (<red>, <green>, <blue>))
VERTICAL_LINES = [
    (53, 0, 64, (0, 0, 200))
]

# Place a hollow rectangle
# (<x position top-left>, <y position top-left>, <x length>, <y length> (<red>, <green>, <blue>))
RECTANGLES = [
    (0, 0, 64, 64, (0, 200, 0)),
    (1, 23, 32, 16, (200, 0, 200))
]