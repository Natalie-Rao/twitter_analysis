import connect;


import twint


tweets = []

c = twint.Config()


c.Username = 'noneprivacy'
c.Limit = 20
c.Store_object = True

c.Store_object_tweets_list = tweets

twint.run.Search(c)

tweets2db = [];
for t in tweets:
    tweets2db.append([c.Username, t.datestamp + " " + t.timestamp, t.tweet])

connect.insert(tweets2db);

