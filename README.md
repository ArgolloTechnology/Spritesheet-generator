# Spritesheet Generator

A simple Python script to generate a spritesheet from a collection of individual frame images. The script arranges the frames into a single PNG image, with the option to specify the maximum number of frames per row and the folder containing the frames.

## Features:
- Automatically arranges frames into a single spritesheet image.
- Allows customization of the number of frames per row.
- Supports custom input folder paths for frame images.
- Saves the resulting spritesheet with a timestamped filename.

## Requirements:
- Python 3.x
- Pillow library (Python Imaging Library)

## Installation:

1. **Install Python** (if not already installed):

   Download and install Python from the official website: https://www.python.org/downloads/

2. **Install the required Python libraries**:

   To install the necessary Python packages, run:
   ```bash
   pip install pillow
   ```
   or
   ```bash
   sudo pacman -S python-pillow
   ```
## Usage:
### Basic Usage:
To run the script, simply execute it from the command line with the following syntax:

```bash
python spritesheet.py [frames_folder] [max_frames_row]
```
Where:
frames_folder (optional): Path to the folder containing the frame images. Default is frames/ if not provided.
max_frames_row (optional): The maximum number of frames per row in the spritesheet. If not provided, it will be calculated automatically to fit the frames into a square layout.
### Example 1: Using Default Folder and Auto Layout
If you have a folder called frames/ containing your image frames, you can run the script without any arguments, and it will automatically calculate the layout:

```bash
python spritesheet.py
```
### Example 2: Custom Folder and Auto Layout
If you want to specify a custom folder for your frames, pass the folder path as the first argument:

```bash
python spritesheet.py path/to/your/frames
```
### Example 3: Custom Folder and Custom Frames per Row
You can also specify the number of frames per row by passing a second argument:

```bash
python spritesheet.py path/to/your/frames 8
```
This will create a spritesheet with 8 frames per row.

### Output:
The resulting spritesheet will be saved as a PNG file with a timestamped filename in the current directory:

```bash
spritesheet_2025-03-30T12-34-56.png
```
## How it Works:
The script reads all image files in the specified folder.
It arranges them into a grid, where each frame is placed in a position based on the provided or calculated number of frames per row.
The final spritesheet image is created and saved as a PNG file with a unique timestamp.

## License:
This project is licensed under the MIT License. See the LICENSE file for more information.
