import json
import functools

class Video:
    def __init__(self, j) -> None:
        self.name = j['title'][8:]
        self.url = j.get('titleUrl', None)
        if 'subtitles' in j:
            self.ch_name = j['subtitles'][0]['name'] 
            self.ch_url = j['subtitles'][0]['url']

@functools.cache
def load_watch_history() -> list[Video]:
    path = 'Takeout/YouTube and YouTube Music/history/watch-history.json'
    with open(path, encoding='utf-8') as f:
        return [Video(v) for v in json.load(f) if 'titleUrl' in v]

