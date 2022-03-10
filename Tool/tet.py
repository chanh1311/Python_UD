
import unidecode
import speech_recognition as sr
import pyttsx3 
from datetime import date
import datetime
import os
import time
import webbrowser
import smtplib
import requests
from urllib.request import urlopen
from urllib.request import urlretrieve
import json
import ctypes
import wikipedia

#Kiểm tra rỗng (quá 3 lần thoát, ngược lại trả về chuỗi)
def check_input():
    for i in range(3):
        yousaid = speech_text()
        print("Bạn:" + yousaid)
        if(yousaid != ""):
            return yousaid
        else:
            brain_robot("Bot không nghe rõ, bạn nói lại được không!")

    speak("Bot đã không nhận phản hồi từ bạn 3 lần, Tạm biệt hẹn gặp lại!")
    return 0
#Xuất âm thanh ra thành text
def speech_text():
    print("Đang lắng nghe...")
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        robot_listen = r.record(source, duration=5) #tg lắng nghe
        print("Đang Nhận dạng...")
        # convert speech to text
        try:
            yousaid = r.recognize_google(robot_listen,language="vi-VN")
            yousaid = yousaid.lower()
            return yousaid
        except:
            yousaid = ""
            return yousaid
#Đọc
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return
#Đưa ra câu trả lời
def brain_robot(robot_brain):    
    print("Đang tìm câu trả lời...")
    print("Robot:" + robot_brain)
    speak(robot_brain)




text = "máy tính là gì"
wikipedia.set_lang("vi")
contents = wikipedia.summary(text).split('\n')
print(contents)




