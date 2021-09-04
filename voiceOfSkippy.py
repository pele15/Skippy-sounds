 # import Adafruit IO REST client.
from threading import main_thread
from Adafruit_IO import Client, Feed, RequestError
from pydub import AudioSegment
from pydub.playback import play
import time  
import threading

ADAFRUIT_IO_USERNAME = "pele15"
ADAFRUIT_IO_KEY = "aio_dYvR65F3zytX0KEbDdNonAHdcgAZ"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# try:
#     hellofeed = aio.feeds('hello')
# except RequestError: # create feeds
#     feed = Feed(name="hello")
#     hellofeed = aio.create_feed(feed)

def execute_feed(key, sound):
    while True:
        start = time.time()
        feed = aio.receive(key)
        print(feed.value)
        if (int(feed.value) == 1 and int(feed.value) != 45):
            print(key + 'played')
            play(sound)
        end = time.time()
        print(end - start)

# def pickle(feed, sound):
#     feed = aio.receive(picklefeed.key) 
#     if (int(pickle.value) == 1 and int(pickle.value) != 45):
#         print('pickle')
#         play(pickleSound)

# while True:
#     start = time.time()
#     hello = aio.receive(hellofeed.key)
#     #pickle = aio.receive(picklefeed.key)
#     if (int(hello.value) == 1 and int(hello.value) != 45):
#         print('hi')
#         play(skippyHello)
#     elif (int(pickle.value) == 1 and int(pickle.value) != 45):
#         print('pickle')
#         play(pickleSound)
#     end = time.time()
#     print("time difference: ", end - start)

def main():
    # feed defines
    hellofeed = aio.feeds('hello-key')
    #picklefeed = aio.feeds('pickle')
    byefeed = aio.feeds('bye-feed')
    # audio segments
    skippyHello = AudioSegment.from_wav("sounds/h.wav")
    pickleSound = AudioSegment.from_wav("sounds/p.wav")
    
    # feeds
    hello = aio.receive(hellofeed.key)
    #pickle = aio.receive(picklefeed.key)
    #hello = threading.Thread(target=execute_feed, args=(hellofeed.key , skippyHello), daemon=True)
    #pickle = threading.Thread(target=execute_feed, args=(picklefeed.key , pickleSound), daemon=True)
    #hello.start()
    #pickle.start()
    feeds = aio.feeds()
    print('Feeds: ', feeds[0].value)
    # while True:
    #     pass




if __name__ == "__main__":
    main()
    # hellofeed = aio.feeds('hello-key')
    # picklefeed = aio.feeds('pickle')
    
    # # audio segments
    # skippyHello = AudioSegment.from_wav("sounds/h.wav")
    # pickleSound = AudioSegment.from_wav("sounds/p.wav")
    
    # hello = threading.Thread(target=execute_feed, args=(hellofeed.key , skippyHello), daemon=True)
    # pickle = threading.Thread(target=execute_feed, args=(picklefeed.key , pickleSound), daemon=True)
    # hello.start()
    # pickle.start()

    # while True:
    #     pass
