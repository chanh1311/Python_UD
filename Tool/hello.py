import speech_recognition as sr
import pyttsx3 
from datetime import date
from datetime import datetime
import os
import re
import webbrowser
import time
import smtplib
import webbrowser

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
            
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return

def check_input():
    for i in range(3):
        yousaid = speech_text()
        print("Bạn:" + yousaid)
        if(yousaid != ""):
            return yousaid
        else:
            speak("Bot không nghe rõ, bạn nói lại được không!")

    speak("Bot đã không nhận phản hồi từ bạn 3 lần, Tạm biệt hẹn gặp lại!")
    return False


def send_email():
    speak('Bạn cần gởi email cho ai nhỉ')
    #lấy tên mail
    name_mail = check_input()
    if not name_mail:
        return False
    if "khánh" in name_mail or "chánh" in name_mail:

        speak('Nội dung bạn muốn gửi là gì')
        #lấy nd gởi
        content = check_input()
        if not name_mail:
            return False
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()

        mail.login('nguyenvannnk@gmail.com','nnkdz123')
        if "chánh" in name_mail:
            mail.sendmail('nguyenvannnk@gmail.com',
                          'chanhn098@gmail.com', content.encode('utf-8'))
        else:
            mail.sendmail('nguyenvannnk@gmail.com',
                          'chanhn1229@gmail.com', content.encode('utf-8'))
        mail.close()

        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
        return True
    else:
        speak('Không tìm thấy người gởi, bạn vui lòng thử lại!')
        return False


send_email()
