import tweepy

consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# text of the thread
my_thread = "It is possible to use the Twitter API to post an arbitrarily long thread. This is just an example, where the text of a long string of test has been split into numbered tweets. The Python code to do this, which uses Tweepy, is available at "

# list that will host the strings that constitute the individual tweets in the thread
split = []

# the unpopulated first tweet
tweet_text = ""

# We split the thread into words and loop over such words to create the individual tweets
for text in my_thread.split(" "):
    
    # I have not optimized the lenght of the individual tweets, nor run many tests; this may be modified
    # but the idea is that it ensures that the longest tweet is not too long
    if len(tweet_text) + len(text) <= 266:
        
        tweet_text += text + " "
        
    else:
        
        split.append(tweet_text[:-1])
        tweet_text = text + " "

#Takes care of the last tweet        
if len(tweet_text[:-1])>0:

    split.append(tweet_text[:-1])
        
#We publish the thread, adding #/# to every tweet
thread_length = len(split)

#we want to keep track of the id of the tweets to append the tweets to the thread and to be able to delete easily the thread
id_tweets = []

for idx, tweet_text in enumerate(split):

    tweet_text = (tweet_text+"\n\n"+str(idx+1)+"/"+str(thread_length))
    
    if idx == 0:
        
        tweet = api.update_status(status = tweet_text)
    
    else:
        
        tweet = api.update_status(status = tweet_text,
                           in_reply_to_status_id = tweet.id,
                           auto_populate_reply_metadata=True)
        
    id_tweets.append(tweet.id)
    
# TO DELETE THE THREAD, JUST RUN THIS SEPARATELY USEING THE id_tweets POPULATED ABOVE
#
# for id in id_tweets:  
#     api.destroy_status(id = id)
