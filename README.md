# Panoply
Panoply is a Python program to drive an RGB Matrix display. This program comes with Home Assistant integration, which makes it a great display to view Home Assistant info.  

## Examples

<img src="https://raw.githubusercontent.com/diademiemi/Pi-RGB/main/images/MyConfig.jpg" align="right" title="Static colour" width="256" height="256" />  
In this image my configuration is shown. I have the time and date displayed at the top. The temperature is shown after being retrieved from Home Assistant.  
Beneath that is a horizontal line which takes the colour of my LED strip (Which you can see in the reflection!), and below that are 6 icons representing my ceiling bulbs, these also take the colour they are set to. At the bottom there is text which says my phone's current battery level, and the entire panel is wrapped in a red square.  

The configuration used for it is the following:

<details><summary>config.py</summary><p>

## config.py
```python
# How often the display refreshes
DISPLAY_REFRESH_RATE = 0.25
# How often information on the device is polled (Date, time)
LOCAL_REFRESH_INTERVAL = 0.4
# How often information over web requests is polled (Home Assistant)
WEB_REFRESH_INTERVAL = 10

# Put your display resolution here
DISPLAY_WIDTH = 64
DISPLAY_HEIGHT = 64
# If you need any rotation, specify this as a multiple of 90, otherwise leave it at 0
DISPLAY_ROTATION = 180
# Display mapping, read https://github.com/hzeller/rpi-rgb-led-matrix#changing-parameters-via-command-line-flags
DISPLAY_HARDWARE_MAPPING = "adafruit-hat"

# Path to font files, NEEDS TO BE "BDF" bitmap fonts!
TINY_FONT = "../fonts/Tiny-4x6.bdf"
SMALL_FONT = "../fonts/Small-5x7.bdf"
LARGE_FONT = "../fonts/PixeloidMono.bdf"

# This defines placeholders which are retrieved from shell commands
# These are refreshed according to LOCAL_REFRESH_INTERVAL
# '<new placeholder name>' : '<shell command>'
COMMAND_PLACEHOLDERS = {
    'time' : 'date +"%H:%M:%S"',
    'date' : 'date +"%Y-%m-%d"'
}

# URL of your Home Assistant instance
HOME_ASSISTANT_URL = "https://home.example.com"
# Long-lived access token
HOME_ASSISTANT_KEY = "ABCDEF"

# This defines placeholders which are retrieved from a Home Assistant instance
# Leave blank to disable entirely
# These are refreshed according to WEB_REFRESH_INTERVAL
# '<new placeholder name>' : '<home assistant entity>' 
HOME_ASSISTANT_STATE_PLACEHOLDERS = {
    'temp' : 'sensor.room_temperature',
    'phonebattery' : 'sensor.phone_battery_level'
}

# Colors that are retrieved from a Home Assistant lightbulb
# These can be used instead of the usual tuple:
# 'text definition' : (<x position>, <y position>, 'bulbs')
# Leave blank to disable entirely
# These are refreshed according to WEB_REFRESH_INTERVAL
# '<new color name>' : '<home assistant entity>' 
HOME_ASSISTANT_COLOURS = {
    'bulb1' : 'light.bulb1',
    'bulb2' : 'light.bulb2',
    'bulb3' : 'light.bulb3',
    'bulb4' : 'light.bulb4',
    'bulb5' : 'light.bulb5',
    'bulb6' : 'light.bulb6',
    'led_01' : 'light.led_01'
}

# Layout settings
# Here you can customise the location and content of text elements or place shapes

# Large text, using the PixeloidMono font
# '<text %placeholder%>' : (<x position bottom-left>, <y position bottom-left>, (<red>, <green>, <blue>))
LARGE_TEXT_ELEMENTS = {
    '%time%' : (8, 9, (200, 200, 200)),
    '%temp%' : (17, 38, (200, 200, 200)),
    '●' : (21, 48, 'bulb1'),
    '● ' : (21, 55, 'bulb2'),
    '●  ' : (29, 48, 'bulb3'),
    '●   ' : (29, 55, 'bulb4'),
    '●    ' : (37, 48, 'bulb5'),
    '●     ' : (37, 55, 'bulb6') # The spaces are required so these show up as unique values in the dict, but they do not get rendered!
}

# Small text, using the 5x7 font
# '<text %placeholder%>' : (<x position bottom-left>, <y position bottom-left>, (<red>, <green>, <blue>))
SMALL_TEXT_ELEMENTS = {
    '%date%' : (7, 18, (200, 200, 200)),
    'it is' : (18, 30, (200, 200, 200))
}

# Tiny text, using the 4x6 font
# '<text %placeholder%>' : (<x position bottom-left>, <y position bottom-left>, (<red>, <green>, <blue>))
TINY_TEXT_ELEMENTS = {
    'c' : (43, 38, (200, 200, 200)),
    'Phone at %phonebattery%%' : (7, 62, (200, 200, 200))
}

# Place a horizontal line, starting from the left
# (<x position top-left>, <y position top-left>, <length> (<red>, <green>, <blue>))
HORIZONTAL_LINES = [
    (16, 40, 31, 'led_01')
]

# Place a vertical line, starting from the top
# (<x position top-left>, <y position top-left>, <length> (<red>, <green>, <blue>))
VERTICAL_LINES = [
]

# Place a hollow rectangle
# (<x position top-left>, <y position top-left>, <x length>, <y length> (<red>, <green>, <blue>))
RECTANGLES = [
    (0, 0, 64, 64, (64, 0, 0))
]
```
</p></details>
