import speech_recognition as sr
import pyttsx3 
import pyttsx3
from datetime import date
from datetime import datetime
#ngay hien tai
today = date.today()
d = today.strftime("%B %d, %Y")

#gio hien tai
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
while(True):

    print("Đang lắng nghe...")
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        robot_listen = r.record(source, duration=5)
        print("Đang Nhận dạng...")
        # convert speech to text
        try:
            yousaid = r.recognize_google(robot_listen)
        except:
            yousaid = ""

        print(yousaid)

        if yousaid == "":
            robot_brain = "Can't hear, please speak again"
        elif "hello" in yousaid:
            robot_brain = "Hello Chanh"
        elif "name" in yousaid:
            robot_brain = "My Robot"
        elif "today" in yousaid:
            robot_brain = d
        elif "now" in yousaid:
            robot_brain = current_time
        elif "bye" in yousaid:
            robot_brain = "Good Bye"
            engine = pyttsx3.init()
            engine.say(robot_brain)
            print(robot_brain)
            engine.runAndWait()
            break;
        else:
            robot_brain = "There is no lazy answer, please say again!!!"

        print("Đang tìm câu trả lời...")

        engine = pyttsx3.init()
        engine.say(robot_brain)
        print(robot_brain)
        engine.runAndWait()

