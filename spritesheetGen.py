from PIL import Image
import os, math, time
import sys

frames = []

# Default values
frames_folder = "frames/"  # Default folder
max_frames_row = None  # Auto-calculate if not provided

# Check arguments
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

    if arg1.isdigit():  # If the first argument is a number
        max_frames_row = int(arg1)
    elif os.path.isdir(arg1):  # If it's a valid folder
        frames_folder = arg1
    else:
        print("Error: First argument must be either a folder path or an integer.")
        exit()

if len(sys.argv) > 2:
    try:
        max_frames_row = int(sys.argv[2])  # Second argument must be max_frames_row
    except ValueError:
        print("Error: Second argument must be an integer.")
        exit()

# Ensure the folder exists
if not os.path.isdir(frames_folder):
    print(f"Error: The folder '{frames_folder}' does not exist.")
    exit()

# Load image files
files = os.listdir(frames_folder)
files.sort()

for current_file in files:
    try:
        with Image.open(os.path.join(frames_folder, current_file)) as im:
            frames.append(im.copy())  # Store the image, not pixel data
    except Exception as e:
        print(f"{current_file} is not a valid image: {e}")

# Ensure there are valid images
if not frames:
    print("No valid images found!")
    exit()

# Tile dimensions
tile_width = frames[0].width
tile_height = frames[0].height

# Number of frames
num_frames = len(frames)

# If max_frames_row is not provided, calculate it automatically for a square layout
if max_frames_row is None:
    max_frames_row = math.ceil(math.sqrt(num_frames))

# Determine spritesheet size
spritesheet_width = tile_width * max_frames_row
required_rows = math.ceil(num_frames / max_frames_row)
spritesheet_height = tile_height * required_rows

# Create the spritesheet
spritesheet = Image.new("RGBA", (spritesheet_width, spritesheet_height))

# Position each frame in the spritesheet
for i, frame in enumerate(frames):
    left = (i % max_frames_row) * tile_width
    top = (i // max_frames_row) * tile_height
    spritesheet.paste(frame, (left, top))

# Save spritesheet with a timestamped filename
output_file = f"spritesheet_{time.strftime('%Y-%m-%dT%H-%M-%S')}.png"
spritesheet.save(output_file, "PNG")
print(f"Spritesheet saved as {output_file}")
