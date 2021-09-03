 # import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
from pydub import AudioSegment
from pydub.playback import play
  

ADAFRUIT_IO_USERNAME = "pele15"
ADAFRUIT_IO_KEY = "aio_GfHf16A3RCSsqTFx1Xn5nUuenF7a"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    hellofeed = aio.feeds('hello')
# # for playing wav file
except RequestError: # create feeds
    feed = Feed(name="hello")
    hellofeed = aio.create_feed(feed)

song = AudioSegment.from_wav("sounds/h.wav")
print('playing sound using  pydub')

while True:
    hello = aio.recieve(hello.key)
    if (int(hello.value)):
        play(song)

