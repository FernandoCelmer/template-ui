from pathlib import Path
from PIL import Image

path = Path("./docs/assets/colors")

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "grey": (105, 105, 105),
    "blue": (64, 81, 181),
    "green": (76, 174, 79),
    "yellow": (241, 220, 21),
    "orange": (255, 167, 36),
    "purple": (171, 71, 189),
    "red": (255, 44, 6)
}

for color in colors:
    img_color  = Image.new(mode="RGB", size=(15, 15), color = colors.get(color))
    img_color.save(path.joinpath(f"{color}.png"))
