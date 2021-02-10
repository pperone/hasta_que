import tweepy

# OAuth2 authentication
auth = tweepy.AppAuthHandler("fwBcUpUv0O193Pe5O33qBlBLq", 
    "XRDPn08Zd0ARDRIkqjn7x9T2A8lSMmXF31khySWVRRLF8141T3")

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)'
