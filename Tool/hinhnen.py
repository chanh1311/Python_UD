from urllib.request import urlopen
import json



def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    json_string  = urlopen(url).read()
    print(json_string)
    parsed_json = json.loads(json_string)
    print(parsed_json)
    photo = parsed_json['urls']['full']
    print(photo)

    # f.close()
    # parsed_json = json.loads(json_string)
    # photo = parsed_json['urls']['full']
    # # Location where we download the image to.
    # urllib2.urlretrieve(photo, "C:/Users/Night Fury/Downloads/a.png")
    # image=os.path.join("C:/Users/Night Fury/Downloads/a.png")
    # ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    # speak('Hình nền máy tính vừa được thay đổi')
change_wallpaper()