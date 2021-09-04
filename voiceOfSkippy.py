 # import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
from pydub import AudioSegment
from pydub.playback import play
import time  

ADAFRUIT_IO_USERNAME = "pele15"

ADAFRUIT_IO_KEY = "aio_lMFJ91KR0BjAS2hohaJkr5x923yN"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# try:
#     hellofeed = aio.feeds('hello')
# except RequestError: # create feeds
#     feed = Feed(name="hello")
#     hellofeed = aio.create_feed(feed)


hellofeed = aio.feeds('hello-key')
picklefeed = aio.feeds('pickle')
skippyHello = AudioSegment.from_wav("sounds/h.wav")
pickleSound = AudioSegment.from_wav("sounds/p.wav")
# print('playing sound using  pydub')

while True:
    start = time.time()
    hello = aio.receive(hellofeed.key)
    pickle = aio.receive(picklefeed.key)
   # print(hello.value)
    if (int(hello.value) == 1 and int(hello.value) != 45):
        print('hi')
        play(skippyHello)
    elif (int(pickle.value) == 1 and int(pickle.value) != 45):
        print('pickle')
        play(pickleSound)
    end = time.time()
    print(end - start)
