from pytube import YouTube

url = "https://www.youtube.com/watch?v=ouNQ7wofAYo&list=RDouNQ7wofAYo&start_radio=1"
yt = YouTube(url).streams.filter(progressive=True,file_extension="mp4").last().download()
print(yt)