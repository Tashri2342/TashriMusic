import os

thumbs = []

for filename in os.listdir("./TashriX/assets"):
    if filename.endswith("png"):
        thumbs.append(filename[:-4])
