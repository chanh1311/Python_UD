import os
if os.path.exists("C:\\test\\demofile4.txt"):
  os.remove("C:\\test\\demofile4.txt")
else:
  print("The file does not exist")