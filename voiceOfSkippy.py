 # import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
from pydub import AudioSegment
from pydub.playback import play
  

ADAFRUIT_IO_USERNAME = "pele15"
ADAFRUIT_IO_KEY = "aio_NGId95PrxExxSWBSAzVQbj4HyJUI"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# try:
#     hellofeed = aio.feeds('hello')
# except RequestError: # create feeds
#     feed = Feed(name="hello")
#     hellofeed = aio.create_feed(feed)


hellofeed = aio.feeds('hello-key')
picklefeed = aio.feeds('pickle-feed')
skippyHello = AudioSegment.from_wav("sounds/h.wav")
pickleSound = AudioSegment.from_wav("sounds/p.wav")
# print('playing sound using  pydub')

while True:
    hello = aio.receive(hellofeed.key)
    pickle = aio.receive(pickle.key)
    if (int(hello.value) == 1):
        #print('hi')
        play(skippyHello)
    elif (int(pickle.value) == 1):
        print('pickle')
        play(pickleSound)
