# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 1. **Positional Arguments**

def display_weather(temp, humidity, wind_speed):
    print(f'Temparature => {temp}C, Humidity => {humidity}%, wind Speed => {wind_speed}km/h')

display_weather(22, 70, 30)

# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.

# Using keyword arguments (order does not matter)
display_weather(humidity=70, temp=22, wind_speed=15)

display_weather(70, wind_speed=15, humidity=22)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(70, 15, wind_speed=22)

# ❌ This will cause a **SyntaxError**
display_weather(15, humidity=70, wind_speed=22)  # Positional argument after keyword argument is not allowed

# 3. **Default Arguments**

def adjust_lightning(room, brightness=75, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

adjust_lightning('Living Room')

adjust_lightning('Kitchen', 50, 3500)

adjust_lightning('Bedroom', brightness=80)




