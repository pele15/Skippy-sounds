ADAFRUIT_IO_USERNAME = "pele15"
ADAFRUIT_IO_KEY = "aio_GfHf16A3RCSsqTFx1Xn5nUuenF7a"

from pydub import AudioSegment
from pydub.playback import play
  
# # for playing wav file
song = AudioSegment.from_wav("sounds/h.wav")
print('playing sound using  pydub')
play(song)

