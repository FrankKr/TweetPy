# Detect Motion, Take Picture, Send Tweet

# add to crontab, run each hour, finish after 55 minutes

from GetCamera import CamCapt
from DetectBird import BirdDetector
from SendTweets import TwitterSender

import time
import datetime
print(__name__)
print('Initializing classes')
# Initialize functionalities
watchdog = BirdDetector()
paperazzi = CamCapt()
shouter = TwitterSender()

sleeptime = 10 # seconds

# Notify Followers of starting loop
try:
    print('Sending Ping')
    shouter.send_msg("I'm Alive! @ {}".format(datetime.datetime.utcnow().time()))
except Exception:
    print('Could not notify followers, starting anyway...')

previously_triggered = False
i=0
print('Starting wachtdogloop')
while i < (55*60)/sleeptime:
    # Check if there is movement
    triggered = watchdog.detect()
    if triggered and not previously_triggered:
        print('Triggered!')
        # Take image
        print('Taking image')
        imgloc = './photo.jpeg'
        paperazzi.take_image(imgloc)
        # Post Tweet
        print('Sending image')
        shouter.send_img(imgloc,'Look at this picture!')
    
    # Remember previous state
    previously_triggered = triggered
    print('Sleeping', 'triggered' if triggered else '')
    time.sleep(sleeptime)

print('Finished!')