import tweepy

# OAuth2 authentication
auth = tweepy.AppAuthHandler("fwBcUpUv0O193Pe5O33qBlBLq", 
    "XRDPn08Zd0ARDRIkqjn7x9T2A8lSMmXF31khySWVRRLF8141T3")

api = tweepy.API(auth)

# Setting up the streamer to listen to mentions
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['python'])

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        if 'RT' not in status.text:
            # Prints the text of the tweet
            print('Tweet text: ' + status.text)
            s = status.author.screen_name
            print(s)
            api.create_favorite(status.id)

            try:
                api.retweet(status.id)
                message = '@' + s + ' You tweeted with my hashtag!'
                api.update_status(status=message, in_reply_to_status_id=status.id)
            except:
                try:
                    print('duplicate tweet error')
                    message = '@' + s + ' You tweeted with my hashtag AGAIN!'
                    api.update_status(status=message, in_reply_to_status_id=status.id)
                except:
                    print('double duplicate tweet error')
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
 
    def on_timeout(self):
        print('Timeout...')
        return True
 
if __name__ == '__main__':
    listener = StdOutListener()
 
    stream = Stream(auth, listener)
    stream.filter(track=['#aribot', '#botbotbot'])
