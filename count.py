import collections
import load

data = load.load_watch_history()
url_map = {v.url: v for v in data}
best = collections.Counter([v.url for v in data]).most_common()
for (v, n) in best:
  print(url_map[v].name, n)