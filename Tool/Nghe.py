import speech_recognition as sr
import pyttsx3 
print("Đang lắng nghe...")
r = sr.Recognizer() 

with sr.Microphone() as source:
    # read the audio data from the default microphone
    robot_listen = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    yousaid = r.recognize_google(robot_listen)
    print(yousaid)