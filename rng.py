import random
from sys import argv
import load

data = load.load_watch_history()
playlist = random.choices(data, k = int(argv[1]))
for x in playlist:
  print(x.url)
