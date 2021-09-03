 # import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
from pydub import AudioSegment
from pydub.playback import play
  

ADAFRUIT_IO_USERNAME = "pele15"
ADAFRUIT_IO_KEY = "aio_OpZB40phr1U0eoJZ1dV2Oly0jnm9"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# try:
#     hellofeed = aio.feeds('hello')
# except RequestError: # create feeds
#     feed = Feed(name="hello")
#     hellofeed = aio.create_feed(feed)


hellofeed = aio.feeds('hello-key')
song = AudioSegment.from_wav("sounds/h.wav")
# print('playing sound using  pydub')

while True:
    hello = aio.receive(hellofeed.key)
    if (int(hello.value) == 1):
        #print('hi')
        play(song)

