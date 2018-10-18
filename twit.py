import twitter
import time
import secret

class twitterIsStupid:


    def __init__(self):
        self.api = secret.getAPI()

    def getTweets(self,screen_name="@realDonaldTrump",numTweets=100):
        
        user = self.api.GetUser(screen_name=screen_name)

        all_tweets = []


        tweet = self.api.GetUserTimeline(user.id,count=1,include_rts=False,exclude_replies=True)[0]
        lastID = tweet.id
        all_tweets.append(tweet)
        lastCount = -1
        while len(all_tweets) < numTweets:
            lastCount = len(all_tweets)
            print len(all_tweets)
            tweets = self.api.GetUserTimeline(dt.id,count=200,include_rts=False,exclude_replies=True,max_id=lastID-1)
            for tweet in tweets:
                all_tweets.append(tweet)
                lastID = all_tweets[-1].id
                if lastCount == len(all_tweets):
                    print "end of tweets"
                    break
                
        return all_tweets


    def trackNewTweets(self,screen_name="@realDonaldTrump"):
        
        user = self.api.GetUser(screen_name=screen_name)
        
        to_track = []


        while True:
            try:
                newestTweets = self.api.GetUserTimeline(user.id,count=10,include_rts=False,exclude_replies=True)

                for tweet in newestTweets:
                    name = str(tweet.id)+".dat"
                    outfile = open(name,"a")
                    outfile.write(str(time.time())+","+str(tweet.favorite_count)+"\n")
                    print tweet.favorite_count,
                    outfile.close()

                print
                time.sleep(2)

            except KeyboardInterrupt:
                print "done!"
                return
