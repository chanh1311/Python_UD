from pynput import keyboard

def on_press(key):
	print(key)                      


with keyboard.Listener(on_press=on_press) as hacker:
	hacker.join()

# listener = keyboard.Listener(
#     on_press=on_press,
#    	on_release=on_release)
# listener.start()

