import sys
import os
import random
import configparser
import random
import time

from pydub import AudioSegment
from pydub.playback import play
from Adafruit_IO import MQTTClient

JOKES_DICT = {
    'guac':"guac-resp",
    'sweden':"sweden-resp",
    'vaccum':"vaccum-resp",
    'cross-road': "cross-road-resp",
    'texas':"texas-resp",
    'metal': "metal-resp",
    'insecure':"insecure-resp",
    'rusty':"rusty-resp",
    'battery':"battery-resp",
}

global joke_key, ind
ind = 0
joke_key = ""

FEED_IDs = [
            'ad',
            'hello-key', 
            'bye-feed', 
            'coffee', 
            'friend', 
            'jokes', 
            'drink', 
            'food-btn',
            'food-list', 
            'great', 
            'notsure', 
            'hry', 
            # 'noprob', 
            # 'deliver', 
            # 'way', 
            # 'roll', 
            'joke-question', 
            'punchline', 
            # 'caribou', 
            # 'potbelly', 
            # 'scan', 
            # 'hungry', 
            # 'yes',
            # 'phrases', 
            # #'thankyou', 
            # #'ricos',
            # #'freshii',
            # 'betteryou.hello-better-you',
        ]
JOKES_IDs = list(JOKES_DICT.keys())
JOKES_IDs_INDS = random.sample(JOKES_IDs, len(JOKES_IDs))

# Define callback functions which will be called when certain events happen.
def connected(client):
    
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_IDs))
    # Subscribe to changes on a feed named DemoFeed.
    for FEED_ID in FEED_IDs:
        client.subscribe(FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('Subscribed to {0} with QoS {1}'.format(FEED_IDs, granted_qos[0]))
    

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    global joke_key
    global ind
    if payload == "1":
        try:
            if (feed_id == "joke-question"):
                joke_key = JOKES_IDs_INDS[ind]
                ind = (ind + 1) % len(JOKES_IDs)
                audio = AudioSegment.from_wav("sounds/joke-question/"  + str(joke_key) + ".wav")
            elif (feed_id == "punchline"):
                audio = AudioSegment.from_wav("sounds/punchline/" + str(JOKES_DICT[joke_key]) + ".wav")
            else:
                file = random.choice(os.listdir("sounds/" + feed_id))
                audio = AudioSegment.from_wav("sounds/" + feed_id + "/" + file)
            play(audio)
        except:
            print('Couldn\'t find the audio file. Please add one')
            pass


print("Total feed to be subscribed: ", len(FEED_IDs))

config = configparser.ConfigParser()
config.read('config.ini')
ADAFRUIT_IO_USERNAME = config['ADAFRUIT']['adafruit_io_username']
ADAFRUIT_IO_KEY = config['ADAFRUIT']['adafruit_io_key']

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

# Connect to the Adafruit IO server.
client.connect()

client.loop_blocking()
