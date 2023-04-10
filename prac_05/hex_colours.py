COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
}

while True:
    color_name = input("Enter a color name to look up the hexadecimal code (or press Enter to quit): ").upper()
    if not color_name:
        break
    color_code = COLORS.get(color_name)
    if color_code:
        print(f"The hexadecimal code for {color_name} is {color_code}.")
    else:
        print(f"Sorry, {color_name} is not a valid color name.")
