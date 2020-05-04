# Send tweet to twitter
# pip3 install TwitterAPI

# twittername: TweetPy, mail = fpmkreuwel+10@gmail.com, Supergeheim1

from TwitterAPI import TwitterAPI
# consumer_key = <your own key>
# consumer_secret = <your own secret>
# access_token_key = <your own token key>
# access_token_secret = <your own token secret>
# 
# api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
# 
# msg = 'This is a tweet!'
# 
# request = api.request('statuses/update', {'status': msg})
# print(request.status_code)

class TwitterSender:
    def __init__(self):
        pass
    
    def send_img(self, imgloc):
        print('Send image!')
        
if __name__=='main':
    print('Do stuff!')