# Example of using the MQTT client class to subscribe to a feed and print out
# any changes made to the feed.  Edit the variables below to configure the key,
# username, and feed to subscribe to for changes.

# Import standard python modules.
import sys
from pydub import AudioSegment
from pydub.playback import play

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
import random

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_sssN36O1kpV4LH7qc4YpYj1m2RcY'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'carbonorigins'

# Set to the ID of the feed to subscribe to for updates.
FEED_IDs_SOUNDS_DICT = {
    'hello-key': "hello.wav",
    'bye-feed': "bye.wav",
    #'yo':       "yo.wav",
    'coffee': "coffee.wav",
    'friend': "friend.wav",
    'skippy': "skippy.wav",
    'jokes': "jokes.wav",
    'drink': "drink.wav",
    'food-btn': "food.wav",
    'great': "great.wav",
    #'ad': "ad.wav",
    'notsure': "notsure.wav",
    'hry': "hry.wav",
    'food-list': "food-list.wav",
    #'noprob':"noprob.wav",
    'deliver':"deliver.wav",
    'way':"way.wav",
    'roll':"roll.wav", 
    'joke-question': "", # limit,
    'punchline': "",
    #'caribou': "caribou.wav",
    #'potbelly': "potbelly.wav",
    'scan': "scan.wav",
    'hungry':"hungry.wav",
    'pickup':"rene.wav",
    'open':"open.wav",
    'close':"close.wav",
    'thanks':"thanks.wav",
    'matt' "matt.wav",
}

JOKES_DICT = {
    'guac':"guac-resp",
    'sweden':"sweden-resp",
    'vaccum':"vaccum-resp",
    'cross-road': "cross-road-resp",
    'texas':"texas-resp"
}

global joke_key, ind
ind = 0
joke_key = ""
FEED_IDs = FEED_IDs_SOUNDS_DICT.keys()
JOKES_IDs = list(JOKES_DICT.keys())
JOKES_IDs_INDS = random.sample(JOKES_IDs, len(JOKES_IDs))


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    
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
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    global joke_key
    global ind
    if payload == "1":
        try:
            if (feed_id == "joke-question"):
                joke_key = JOKES_IDs_INDS[ind]
                ind = (ind + 1) % len(JOKES_IDs)
                audio = AudioSegment.from_wav("sounds/" + str(joke_key) + ".wav")

            elif (feed_id == "punchline"):
                print("elif")
                print("sounds/" + str(JOKES_DICT[joke_key]) + ".wav")
                audio = AudioSegment.from_wav("sounds/" + str(JOKES_DICT[joke_key]) + ".wav")
            else:
                print("else")
                audio = AudioSegment.from_wav("sounds/" + str(FEED_IDs_SOUNDS_DICT[feed_id]))
            play(audio)
        except:
            print('Couldn\'t find the audio file. Please add one')
            pass


print("Total feed to be subscribed: ", len(FEED_IDs))
# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

# Connect to the Adafruit IO server.
client.connect()

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
client.loop_blocking()
