from youtube_search import YoutubeSearch

def play_song():
    speak('Bạn muốn nghe nhạc gì?')
    mysong = check_input()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[1]['url_suffix']
    webbrowser.open(url)

    return url