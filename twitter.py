# -*- coding: utf-8 -*-
import sys
import HTMLParser
import re

import oauth
from user_credentials_dbm import delete_dbm

from packages import requests
from packages.clint.textui import colored


class tweetcommander(object):
    
    def __init__(self):
        self.since_id = '1'
        self.timeline = []
        self.page = 0
        self.count = None
        self.command_re = re.compile('(\/?[a-z]+)\s?([A-Za-z0-9\s]+)*\s?')


    def welcome(self):
        print '+----------------------------------------------+'
        print ''
        print ' .•°¤*(¯`★´¯)*¤° TweeтCoммander °¤*(¯´★`¯)*¤°•.'
        print ''
        print '> type /h for a list fo commands.'
        print '+----------------------------------------------+'


    def get_timeline(self, url, url_params):
        ents = HTMLParser.HTMLParser()
        tweet_id = 0

        credentials = oauth.connection()
        twitter_request = requests.get(url, auth=credentials, params=url_params)

        if twitter_request.json() and twitter_request.status_code == 200:
            ref = self.page
            self.page += 1
            self.timeline.append(twitter_request.json())
            self.since_id = self.timeline[ref][0]['id_str']

            for i in range(len(self.timeline[ref])-1, -1, -1):

                tweet_id += 1

                try:
                    text = ents.unescape(self.timeline[ref][i]['retweeted_status']['text'])
                    print '%d %d %s from %s' % (
                        self.page, tweet_id,
                        colored.green('@' + self.timeline[ref][i]['user']['screen_name']),
                        colored.red('@' + self.timeline[ref][i]['retweeted_status']['user']['screen_name'])
                    )
                    print colored.yellow(text)
                    print ''
                except KeyError:
                    text = ents.unescape(self.timeline[ref][i]['text'])
                    print '%d %d %s' % (
                        self.page, tweet_id,
                        colored.green('@' + self.timeline[ref][i]['user']['screen_name'])
                    )
                    print colored.yellow(text)
                    print ''
        else:
            print colored.red('Theres no new tweets at the moment !!!')


    def home_timeline(self, count):
        url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
        print count
        url_params = {
            'count': count,
            'since_id': self.since_id,
        }

        self.get_timeline(url, url_params)


    def user_timeline(self, *args):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

        screen_name = raw_input("Who's timeline you want to see ? > ")
        count = raw_input('How many tweets you want to see ? > ')

        url_params = {
            'count': count,
            'screen_name': screen_name
        }

        get_timeline(url, url_params)


    def post_tweets(self, tweet):
        url = 'https://api.twitter.com/1.1/statuses/update.json'

        tweet = {
            'status': tweet
        }

        credentials = oauth.connection()

        requests.post(url, auth=credentials, params=tweet)


    def retweet(self, *args):
        index = len(self.timeline[int(args[0][0])-1])

        url = ('https://api.twitter.com/1.1/statuses/retweet/' +
               self.timeline[int(args[0][0])-1][index-int(args[0][1])]['id_str'] + '.json'
        )

        credentials = oauth.connection()
        retweet = requests.post(url, auth=credentials)


    def favorite(self, *args):
        url = 'https://api.twitter.com/1.1/favorites/create.json'

        index = len(self.timeline[int(args[0][0])-1])

        fav = {
            'id': self.timeline[int(args[0][0])-1][index-int(args[0][1])]['id_str']
        }

        credentials = oauth.connection()

        favorite = requests.post(url, auth=credentials, params=fav)


    def direct_m():
        pass


    def help(self):
        print '+------------------------------------------------------------+'
        print 'TweeтCoммander actions :'
        print ''
        print '> tl: get your last timeline'
        print '> tw: post a tweet ex. tw Hello, World!!!'
        print '> rt: retweet the number of a tweet from timeline page ex. rt 1 5'
        print '> utl: get the timeline of twitter user ex. utl > raqqun (user) > 20 (tweets)'
        print '> fv: favorite a tweet from timeline page ex. fv 1 5'
        print '> /h: open the help commands list'
        print '> /q: quit tweetcommander'
        print '> /rv: revoke access to your account by deleting your credentials from your computer'
        print '+------------------------------------------------------------+'


    def quit(self):
        sys.exit(0)


    def revoke(self):
        delete_dbm()
        sys.exit(0)


    def commands(self, action):
        command = self.command_re.search(action)
        
        if command.group(1) == 'tl':
            self.home_timeline(command.group(2))
        elif command == 'utl':
            pass
        elif command.group(1) == 'tw':
            self.post_tweets(command.group(2))
        elif command == 'rt':
            pass
        elif command == 'dm':
            pass
        elif command == 'fv':
            pass
        elif command.group(1) == '/h':
            self.help()
        elif command.group(1) == '/q':
            self.quit()
        elif command.group(1) == '/rv':
            self.revoke()
        else:
            print "This action doesn't exists"
