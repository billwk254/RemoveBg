from rembg import remove
from PIL import Image
import easygui as eg
import os
from pathlib import Path

try:
    image_location = eg.fileopenbox(title="Open Image file")
    Open_image = Image.open(image_location)
    input_path = os.path.abspath(image_location)
    rgb_im = Open_image.convert('RGB')
    new_file = os.path.basename(input_path)
    new_file = os.path.splitext(new_file)[0]
    output = remove(rgb_im)
    bg_removed = eg.filesavebox(title="Save file to", default=f'{Path.home() / "Pictures"}\\{new_file}-removedBG.png')
    if bg_removed:
        print(f"File was saved to {os.path.abspath(bg_removed)}")
    output.save(bg_removed)

except KeyboardInterrupt as e:
    print("Program KeyboardInterrupt\n ")

except AttributeError:
    print("No image was Selected \n")
