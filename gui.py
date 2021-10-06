import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout, QRadioButton)

import json
# from awscrt import io, mqtt, auth, http
# import configparser
# import publish as pub

import sys
import os
import random
import configparser
import random
import time

from pydub import AudioSegment
from pydub.playback import play
from functools import partial


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
            #'coffee', 
            'friend', 
            'jokes', 
            'drink', 
            'food-btn',
            #'food-list', 
            'great', 
            'notsure', 
            'hry', 
            'noprob', 
            #'deliver', 
            'way', 
            #'roll', 
            'joke-question', 
            'punchline', 
            # 'caribou', 
            # 'potbelly', 
            # 'scan', 
            #'hungry', 
            'yes',
            'phrases', 
            'thankyou', 
            # #'ricos',
            # #'freshii',
            # 'betteryou.hello-better-you',
            #'seth',
            #'pickup',
            #'open',
            #'redbull.ad',
            #'redbull.ofcourse',
            #'redbull.um',
        ]

JOKES_IDs = list(JOKES_DICT.keys())
JOKES_IDs_INDS = random.sample(JOKES_IDs, len(JOKES_IDs))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Push Buttons
        self.buttons = []
        for i in range(len(FEED_IDs)):
            self.buttons.append(QPushButton(FEED_IDs[i]))
            self.buttons[i].clicked.connect(partial(self.on_button_clicked, FEED_IDs[i]))
            main_layout.addWidget(self.buttons[i]) 
        
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)  

    def on_button_clicked(self, feed_id):
        global joke_key
        global ind
        print("feed id = ", feed_id)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow() 
    w.show()
    sys.exit(app.exec_())    