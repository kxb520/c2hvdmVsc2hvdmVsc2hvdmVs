import os
import time

import pyttsx3
from removebg import RemoveBg

pyttsx3.speak("start")
while True:
    try:
        rmbg = RemoveBg("jt3KVFexzKL1uTvw5qTrPe2M", "error.log")
        path = './img/'
        for img in os.listdir(path):
            print("* running " + str(img))
            if (img.endswith('jpg') or img.endswith('png') or img.endswith('jpeg')) and not (
                    img.endswith('jpg_no_bg.png') or img.endswith('jpg_no_bg.png')):
                rmbg.remove_background_from_img_file(path + img)
                time.sleep(1)
        break
        # proxifer
    except Exception as e:
        pass
pyttsx3.speak("done")
# tensorflow
