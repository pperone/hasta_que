import tweepy

# OAuth2 authentication
auth = tweepy.AppAuthHandler("fwBcUpUv0O193Pe5O33qBlBLq", 
    "XRDPn08Zd0ARDRIkqjn7x9T2A8lSMmXF31khySWVRRLF8141T3")

api = tweepy.API(auth)

# Setting up the streamer to listen to mentions
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['python'])

# Custom class for the modified stream listener
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)