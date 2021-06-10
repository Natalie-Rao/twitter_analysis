import connect;
import configparser

import twint


def queryFollowers(feed, followersCount):
    c = twint.Config()

    c.Username = feed
    c.Limit = followersCount
    c.Store_object = True

    twint.run.Followers(c)
    followers = twint.output.follows_list
    print(followers)


def queryFeedStatus(feed, timerange, twittercount):
    return ""


def crawler(feed, level, timerange, twittercount):
    tweets = []
    c = twint.Config()


    c.Username = feed
    c.Limit = 20
    c.Store_object = True

    c.Store_object_tweets_list = tweets

    twint.run.Search(c)

    tweets2db = [];
    for t in tweets:
        tweets2db.append([c.Username, t.datestamp + " " + t.timestamp, t.tweet])

    connect.insert(tweets2db);


# main entry

config = configparser.ConfigParser()
config.read('crawler.ini')

crawler_feeds = config['feeds']['feeds']

feeds = crawler_feeds.split(",")
print(feeds);

for feed in feeds:
    if not feed:
        continue
    print(feed)
    _level = config[feed]['level']
    _timerange = config[feed]['timerange']
    _twittercount = config[feed]['twittercount']
    _followers = config[feed]['followers']
    print('start to crawl :', 'feed=' + feed, 'level='+_level, 'timerange='+_timerange, 'twittercount='+_twittercount, 'followers=' + _followers)
    queryFollowers(feed, _followers)











