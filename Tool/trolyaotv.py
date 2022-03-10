#!/usr/bin/python
# -*- coding: utf8 -*-
import unidecode
import speech_recognition as sr
import pyttsx3 
from datetime import date
from datetime import datetime
import os
import time
import webbrowser
import smtplib
import requests
from youtube_search import YoutubeSearch
import wikipedia


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
#lay duong dan tu dong
from webdriver_manager.chrome import ChromeDriverManager

path = ChromeDriverManager().install()
#Đường dẫn được lấy tự động

#ngay hien tai
def get_ngay():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1;

#gio hien tai
def get_gio():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

#chao hoi
def get_chao():
    now = datetime.now()
    time = int(now.strftime('%H'))
    if time < 12:
        chao = "Chào buổi sáng bạn! Chúc bạn một ngày tốt lành."
    elif 12 <= time < 18:
        chao = "Chào buổi chiều bạn! Bạn đã dự định làm gì chưa?"
    else:
        chao = "Chào buổi tối bạn! Bạn ăn tối chưa nhỉ?"
    return chao
def rep_chao(chao,tukhoa):
    if chao == "Chào buổi sáng bạn! Chúc bạn một ngày tốt lành." or tukhoa == "":
        help_robot = "Rất vui khi gặp bạn,Bây giờ tôi có thể giúp gì cho bạn?"
        print("Robot:" + help_robot)
        speak(help_robot)
        return
    elif chao == "Chào buổi chiều bạn! Bạn đã dự định làm gì chưa?":
        if "chưa" in tukhoa:
            help_robot = "À vậy chúng ta có thể trò chuyện cùng nhau, biết đâu bạn sẽ biết làm gì đấy!"
            print("Robot:" + help_robot)
            speak(help_robot)
            return
        elif ("định" in tukhoa) or ("tính" in tukhoa):
            help_robot = "Vậy chúc bạn làm thật tốt nhé, bây giờ chúng ta có thể trò chuyện chứ nhỉ?"
            print("Robot:" + help_robot)
            speak(help_robot)
            return
        else:
            help_robot = "À vậy à, rất vui khi gặp bạn,Bây giờ tôi có thể giúp gì cho bạn?"
            print("Robot:" + help_robot)
            speak(help_robot)
            return
    else:
        if "chưa" in tukhoa:
            help_robot = "Tôi cũng chưa nè, mà chắc tôi cũng không cần ăn đâu. Bây giờ tui có thể giúp gì cho bạn?"
            print("Robot:" + help_robot)
            speak(help_robot)
            return
        elif "rồi" in tukhoa:
            help_robot = "Tốt quá bây giờ chúng ta có thể trò chuyện cùng nhau, bạn muốn hỏi gì không?"
            print("Robot:" + help_robot)
            speak(help_robot)
            return
        else:
            help_robot = "À vậy à, rất vui khi gặp bạn,Bây giờ tôi có thể giúp gì cho bạn?"
            print("Robot:" + help_robot)
            speak(help_robot)
            return

#âm thanh sang text
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
#đọc
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return

#Kiểm tra chuỗi rỗng, không nói 3 lần thoát
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

#Mở app
def open_app(tu_open):
    if "google" in tu_open:
        print("Đang mở Google Chrome...")
        os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
    elif "trình duyệt" in tu_open:
        print(" Đang mở Firefox...")
        os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')
    elif "zalo" in tu_open:
        print("Đang mở Zalo...")
        os.startfile('C:/Users/chanh/AppData/Local/Programs/Zalo/Zalo.exe')
    else:
        brain_robot("Ứng dụng chưa được cài đặt, bạn vui lòng thử lại!")
        return False;
    time.sleep(10)
    return True;

#mở trang web
def open_website(domain):
        domain = convert_domain(domain)
        url = 'https://www.' + domain + ".com"
        print("Đang mở trang web: " + url)
        webbrowser.open(url)
        time.sleep(3)
#chuyen domain    
def convert_domain(text_web):
    text_web = text_web.replace(" ", "")
    text_web_converted = unidecode.unidecode(text_web)
    return text_web_converted
#Mở gg và tìm kiếm
def open_google_and_search(text):
    search_for = text
    print("...Đang tìm kiếm theo từ khóa: " + search_for +"...")
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")

    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)

    assert "No results found." not in driver.page_source
    time.sleep(10)
#gởi email
def send_email():
    speak('Bạn cần gởi email cho ai nhỉ')
    #lấy tên mail
    name_mail = check_input()
    if not name_mail:
        speak("Bot đã không nhận phản hồi tên người cần gởi từ bạn 3 lần")
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

        speak('Email của bạn vừa được gửi. Bạn check lại email nhé hihi.')
        time.sleep(3)
        return True
    else:
        speak('Không tìm thấy người gởi, bạn vui lòng thử lại!')
        return False
#Dừng hoặc tiếp tục(xét qua các từ khóa)
def stop_or_continue(tl):
    if("dừng" in tl or "thoát" in tl or "tạm biệt" in tl or "bai" in tl or "bye" in tl):
        return True
    else: 
        return False
#Đưa ra câu trả lời dựa trên chuỗi
def brain_robot(robot_brain):    
    print("Đang tìm câu trả lời...")
    print("Robot:" + robot_brain)
    speak(robot_brain)

#Xem thời tiết
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = check_input()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.

        Bot vừa dự báo thời tiết cho bạn, chúng ta tiếp tục nhé!!!""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        brain_robot(content)
        time.sleep(3)
        return True
    else:
        return False
#Phát nhạc youtube tự động
def play_song():
    speak('Bạn muốn nghe nhạc gì?')
    mysong = check_input()
    if not mysong:
        speak("Bot đã không nghe phản hồi những gì bạn muốn nghe 3 lần...")
        return False
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    print("Đang mở " + url)
    webbrowser.open(url)
    speak("Video yêu cầu đã được mở...")
    time.sleep(3)
#Thay đổi ảnh nền máy tính
def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    f = urlopen(url)
    json_string = f.read()
    f.close()
    #chuyển dạng json sang python#
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    print(photo)
    urlretrieve(photo, "C:/Users/test/Downloads/a.png")
    image=os.path.join("C:/Users/test/Downloads/a.png")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,0)
    speak('Hình nền máy tính vừa được thay đổi')
    time.sleep(3)

#Đọc báo
def read_news():
    speak("Bạn muốn đọc báo về gì")
    
    queue = check_input()
    if not queue:
        speak("Bot đã không nghe phản hồi 3 lần...")
        return False
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    # print(api_result.url)
    # http://newsapi.org/v2/top-headlines?apiKey=30d02d187f7140faacf9ccd27a1441ad&q=b%C3%B3ng+%C4%91%C3%A1(từ khóa được mã hóa)

    # print(api_result)
    #<Response [200]>

    api_response = api_result.json()
    # print(api_response)
    #{'status': 'ok', 'totalResults': 0, 'articles': []}

    if api_response['totalResults'] != 0:
        print("Tin tức")
        #number = 1,api_response['articles'][đầu tiên]
        for number, result in enumerate(api_response['articles'], start=1):
            print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
        """)
            if number <= 3:
                webbrowser.open(result['url'])
        speak("Bài báo theo chủ đề của bạn đã được mở!")
        time.sleep(3)
        return True
    else:
        speak("Không thể tìm thấy chủ đề bài báo của bạn, hãy thử lại!")
        return False

#Tra wikipedia
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = check_input()
        if not text:
            speak("Bot đã không nghe phản hồi 3 lần...")
            time.sleep(1)
            return False
        wikipedia.set_lang("vi")
        contents = wikipedia.summary(text).split('\n')
        brain_robot(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = check_input()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3)
        return True
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        time.sleep(1)
        return False

#Xuất ra chuỗi chức năng
def help_me():
    brain_robot("""Bot có thể giúp bạn thực hiện những việc sau đây:
    1. Trò truyện cùng bạn.
    2. Hiển thị ngày.
    3. Hiển thị giờ.
    4. Mở ứng dụng tự động.
    5. Mở website tự động.
    6. Tìm kiếm từ khóa trên Google.
    7. Gửi email tự động.
    8. Dự báo thời tiết.
    9. Mở video nhạc tự động
    10. Thay đổi hình nền máy tính.
    11. Đọc báo hôm nay.
    12. Kể bạn biết về thế giới """)
    



#chương trình chính chạy

speak("Bạn tên gì nhỉ?")
name = speech_text()
print("Bạn:" + name)
if name:
    speak("Chào {}".format(name))
speak("Bot có thể giúp gì cho bạn ạ?")

while(True):
    yousaid = check_input()
    if not yousaid:
        break
    if "giúp tôi với" in yousaid or "có thể làm gì" in yousaid or "chức năng" in yousaid or "hỏi gì" in yousaid or "làm được" in yousaid: 
        help_me()
        time.sleep(10)
        speak("Nào bạn muốn tôi giúp gì?")
        continue
    elif "chào" in yousaid:
        robot_brain = get_chao()
        brain_robot(robot_brain)
        tl = speech_text()
        print("Bạn:" + tl)
        rep_chao(loichao,tl)
        continue
    elif "ok" in yousaid:
        robot_brain = "Ô kê bạn muốn hỏi gì nào?"
    elif "tên bạn" in yousaid:
        robot_brain = "Tôi là Rô Bốt"
    elif "tuổi của bạn" in yousaid:
        robot_brain = "Rô bốt thì không có tuổi chứ nhỉ?"    
    elif "1" in yousaid or "trò chuyện" in yousaid or "đầu tiên" in yousaid:
        robot_brain = "Nào bạn muốn hỏi gì nhỉ?"
    elif "ngày" in yousaid or "2" in yousaid or "thứ hai" in yousaid:
        d = get_ngay()
        robot_brain = d
    elif "giờ" in yousaid or "3" in yousaid  or "thứ ba" in yousaid:
        current_time = get_gio()
        robot_brain = current_time 
    elif "ứng dụng" in yousaid or "4" in yousaid or "thứ tư" in yousaid:
        speak("Ô kê, Nào hãy nói cho tôi biết bạn muốn mở gì nào?")
        tu_open = check_input()
        if not tu_open:
            break
        if(open_app(tu_open) == True):
            speak("Tôi vừa mở ứng dụng cho bạn. Chúng ta có tiếp tục chứ?")
            tl = speech_text()
            print("Bạn:"+tl)
            if(stop_or_continue(tl)):
                speak("Ô kê tạm biệt..")
                break
            else: 
                speak("Ô kê vậy giờ chúng ta có thể tiếp tục..")
                continue
        else:
            speak("Ô kê vậy giờ chúng ta có thể tiếp tục cuộc trò tuyện..")
            continue 
    elif "web" in yousaid or "trang web" in yousaid or "5" in yousaid or "thứ năm" in yousaid:
        speak("Ô kê, Nào hãy nói cho tôi biết bạn muốn mở trang web với tên miền gì nào?")
        domain = check_input()
        if not domain:
            break
        open_website(domain)
        speak("Tôi vừa mở trang web cho bạn. Chúng ta có tiếp tục chứ?")
        tl = speech_text()
        print("Bạn:"+tl)
        if(stop_or_continue(tl)==True):
            speak("Ô kê tạm biệt..")
            break
        else:
            speak("Ô kê vậy giờ chúng ta có thể tiếp tục..")
            continue

    elif "tìm kiếm" in yousaid or "từ khóa" in yousaid or "tra cứu" in yousaid or "google" in yousaid or "6" in yousaid or "thứ sáu" in yousaid:
        speak("Ô kê, Nào hãy nói cho tôi biết bạn muốn tìm kiếm từ khóa gì nào?")
        tukhoatk = check_input()
        if not tukhoatk:
            break
        open_google_and_search(tukhoatk)
        speak("Bot vừa tìm kiếm theo từ khóa cho bạn. Chúng ta có tiếp tục chứ?")
        tl = speech_text()
        print("Bạn:"+tl)
        if(stop_or_continue(tl)==True):
            speak("Ô kê tạm biệt..")
            break
        else:
            speak("Ô kê vậy giờ chúng ta có thể tiếp tục..")
            continue
    elif "email" in yousaid or "thư" in yousaid or "mail" in yousaid or "gửi" in yousaid or "gởi" in yousaid or "7" in yousaid or "thứ bảy" in yousaid:
        if(send_email()):
            speak("Bot vừa giúp bạn gởi email. Chúng ta có tiếp tục nhé?")
        else:
            speak("Ô kê vậy giờ chúng ta tiếp tục cuộc trò truyện nào!")
        continue
    elif "dự báo" in yousaid or "thời tiết" in yousaid or "khí hậu" in yousaid or "trời hôm nay" in yousaid or "8" in yousaid or "thứ tám" in yousaid:
        thoitiet = current_weather()
        if not thoitiet:
            speak("Tôi không có thông tin của địa chỉ này, bạn vui lòng thử lại")
            speak("Chúng ta tiếp tục nhé?")
        continue
    elif "youtube" in yousaid or "video" in yousaid or "phát nhạc" in yousaid or "9" in yousaid or "thứ chín" in yousaid:
        if(play_song()):
            speak("Tôi vừa mở youtube cho bạn, Chúng ta tiếp tục nhé?")
        else:
            speak("Chúng ta tiếp tục nhé?")
        continue
    elif "ảnh nền" in yousaid or "đổi" in yousaid or "10" in yousaid or "thứ 10" in yousaid:
        change_wallpaper()
        speak("Tôi vừa thay đổi ảnh nền cho bạn, chúng ta tiếp tục nhé..")
        continue
    elif "đọc báo" in yousaid or "tin tức" in yousaid or "11" in yousaid or "mười một" in yousaid:
        if(read_news()):  
            speak("Tôi vừa giúp bạn đọc báo, chúng ta tiếp tục nhé..")
        else:
            speak("Chúng ta bắt đầu lại nhé..")
        continue
    elif "định nghĩa" in yousaid or "là gì" in yousaid or "thông tin" in yousaid or "wikipedia" in yousaid or "12" in yousaid or "mười hai" in yousaid:
        tell_me_about()
        speak("Nào, chúng ta bắt đầu lại nhé..")
        continue
    elif "tạm biệt" in yousaid or "bai" in yousaid or "bye" in yousaid or "dừng" in yousaid or "thoát" in yousaid:
        brain_robot("Ô kê, tạm biệt hẹn gặp lại!")
        break
    else:
        robot_brain = "Bot chưa hiểu ý bạn, bạn nói lại được không?"

    brain_robot(robot_brain)
    time.sleep(3)

           
       
