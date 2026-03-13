# Tiny Mouse Jiggler

A simple, unobtrusive mouse jiggler that prevents your computer from going to sleep.

## Features

- Moves the mouse cursor by 1 pixel every 60 seconds
- Immediately returns to the original position
- Minimal and unobtrusive
- Easy to stop with Ctrl+C

## Installation

Install the required dependency:

```bash
uv pip install --native-tls -r requirements.txt
```

Or using standard pip:

```bash
pip install pyautogui
```

## Usage

Run the script:

```bash
python3 tiny_jiggler.py
```

To stop the jiggler, press `Ctrl+C` in the terminal.

## Configuration

You can adjust the behavior by modifying these constants in `tiny_jiggler.py`:

- `INTERVAL_SECONDS`: Time between jiggles (default: 60 seconds)
- `PIXEL_MOVE`: Number of pixels to move (default: 1 pixel)

## Note

On macOS, you may need to grant accessibility permissions to your terminal application for the script to control the mouse.
