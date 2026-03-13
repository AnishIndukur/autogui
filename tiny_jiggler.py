import time
import random
import pyautogui

INTERVAL_SECONDS = 60
PIXEL_MOVE = 1

print("Mouse jiggler started. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()

        # Random direction (8 directions including diagonals)
        dx = random.choice([-PIXEL_MOVE, 0, PIXEL_MOVE])
        dy = random.choice([-PIXEL_MOVE, 0, PIXEL_MOVE])
        while dx == 0 and dy == 0:
            dx = random.choice([-PIXEL_MOVE, 0, PIXEL_MOVE])
            dy = random.choice([-PIXEL_MOVE, 0, PIXEL_MOVE])

        pyautogui.moveTo(x + dx, y + dy, duration=0)
        time.sleep(0.1)
        pyautogui.moveTo(x, y, duration=0)

        time.sleep(INTERVAL_SECONDS)
except KeyboardInterrupt:
    print("\nStopped.")
