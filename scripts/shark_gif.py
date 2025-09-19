import numpy as np
from PIL import Image, ImageDraw

# GIF parameters
frames = []
width, height = 400, 200
num_frames = 30
amplitude = 30
frequency = 0.3

for t in range(num_frames):
    img = Image.new("RGB", (width, height), "skyblue")
    draw = ImageDraw.Draw(img)

    # Draw sea
    for x in range(width):
        y = int(height/2 + amplitude * np.sin(frequency * (x + t*10)))
        draw.line((x, y, x, height), fill="blue")

    # Draw shark fin (triangle)
    shark_x = (t * 10) % width
    shark_y = int(height/2 + amplitude * np.sin(frequency * (shark_x + t*10))) - 20
    draw.polygon(
        [(shark_x, shark_y), (shark_x+20, shark_y+40), (shark_x-20, shark_y+40)],
        fill="gray"
    )

    frames.append(img)

# Save GIF
frames[0].save("shark.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
print("Generated shark.gif")
