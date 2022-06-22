from PIL import ImageGrab
from pynput.mouse import Button, Controller
import time


def click_when_green(mouse, PIXEL_X, PIXEL_Y, GREEN_RGB, TIME_LIMIT):
    initial_time = time.time()
    while True:
        if time.time()-initial_time >= TIME_LIMIT: return

        px = ImageGrab.grab().load()

        if px[PIXEL_X, PIXEL_Y] == GREEN_RGB:
            mouse.position = (PIXEL_X, PIXEL_Y)
            mouse.press(Button.left)
            mouse.release(Button.left)
            break