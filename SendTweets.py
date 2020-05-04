# Send tweet to twitter
# pip3 install TwitterAPI

# twittername: TweetPy, mail = fpmkreuwel+10@gmail.com, Supergeheim1

import secrets
from TwitterAPI import TwitterAPI

class TwitterSender:
    def __init__(self):
        consumer_key = secrets.api_key
        consumer_secret = secrets.api_secret_key
        access_token_key = secrets.access_token
        access_token_secret = secrets.access_token_secret

        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    
    def send_msg(self, msg):
        request = self.api.request('statuses/update', {'status': msg})
        if request.status_code == 200:
            print('Message posted')
        else:
            print('Unsuccesful post:', request.status_code, request.text)
    
    def send_img(self, imgloc, msg):      
        # STEP 1 - upload image
        with open(imgloc, 'rb') as f:
            data = f.read()
            r = self.api.request('media/upload', None, {'media': data})
            if r.status_code != 200:
                print('UPLOAD MEDIA FAILURE', r.text)

        # STEP 2 - post tweet with reference to uploaded image
        if r.status_code == 200:
            media_id = r.json()['media_id']
            r = self.api.request('statuses/update', {'status':msg, 'media_ids':media_id})
            print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE')
        
if __name__=='__main__':
    ts = TwitterSender()
    #ts.send_msg('Just came online onceagain')
    #ts.send_img('/home/pi/Pictures/birds.jpeg','Look at this jpeg picture!')
    