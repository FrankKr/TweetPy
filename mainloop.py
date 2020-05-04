# Detect Motion, Take Picture, Send Tweet


from GetCamera import CamCapt
from DetectBird import BirdDetector
from SendTweets import TwitterSender

import time

# Initialize functionalities
watchdog = BirdDetector()
paperazzi = CamCapt()
shouter = TwitterSender()

previously_triggered = False
while True:
    # Check if there is movement
    triggered = watchdog.detect()
    if triggered and not previously_triggered:
        print('Triggered!')
        # Take image
        print('Taking image')
        imgloc = './photo.pjg'
        paperazzi.take_image(imgloc)
        # Post Tweet
        print('Sending image')
        shouter.send_img(imgloc)
    previously_triggered = triggered
    print('Sleeping')
    time.sleep(1)
    