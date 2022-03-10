def check_input():
    for i in range(3):
        yousaid = speech_text()
        print("Bạn:" + yousaid)
        if(yousaid != ""):
            return yousaid
        else:
            speak("Bot không nghe rõ, bạn nói lại được không!")

    speak("Bot đã không nhận phản hồi từ bạn 3 lần, Tạm biệt hẹn gặp lại!")
    return 0
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

def send_email():
    speak('Bạn gửi email cho ai nhỉ')
    #lấy tên mail
    name_mail = check_input()
    
    speak('Nội dung bạn muốn gửi là gì')
    #lấy nd gởi
    content = get_text()

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login('chanhn1229@gmail.com', 'Chanhn9221000630@')
    mail.sendmail('chanhn1229@gmail.com',
                  'chanhn098@gmail.com', content.encode('utf-8'))
    mail.close()
    speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
else:
    speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?'

send_mail()