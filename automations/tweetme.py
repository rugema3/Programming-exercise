import GetOldTweets3 as got

# Define the tweet criteria
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('rwanda') \
                                           .setSince("2022-01-01") \
                                           .setUntil("2022-12-31") \
                                           .setMaxTweets(10)

# Get the tweets based on the criteria
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# Print the text of the tweets
for tweet in tweets:
    print(tweet.text)

