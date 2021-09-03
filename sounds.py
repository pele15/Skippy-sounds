# from playsound import playsound

# playsound('hiSkippy.wav')

from pydub import AudioSegment
from pydub.playback import play
  
# for playing wav file
song = AudioSegment.from_wav("hiSkippy.wav")
#song = AudioSegment.from_wav()
print('playing sound using  pydub')
play(song)



# import os
  
# # play sound
# file = "hello_im_skippy.mp3"
# print('playing sound using native player')
# os.system("mpg123 " + file)
