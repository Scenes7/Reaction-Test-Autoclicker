from PIL import ImageGrab
from pynput.mouse import Button, Controller
import time
from click import click_when_green


mouse = Controller()
PIXEL_X, PIXEL_Y = 1000, 400 #these are the x and y positions of the cordinates that are used
TIME_LIMIT = 20 #the program will halt if green is not detected on pixel (1000, 4000) within 20 seconds of the program starting
GREEN_RGB = (75, 219, 106)


def main():

    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)

    for i in range(5):
        click_when_green(mouse, PIXEL_X, PIXEL_Y, GREEN_RGB, TIME_LIMIT)

        time.sleep(0.5) #0.5 second pause after each reaction test
        mouse.press(Button.left)
        mouse.release(Button.left)


if __name__ == "__main__":
    main()
