# -*- coding: utf-8 -*-
import dbm
from urlparse import parse_qs
from user_credentials_dbm import dbm_create, dbm_fetch

from packages.clint import resources
from packages import requests
from packages.requests_oauthlib import OAuth1


# these are the client key and secret needed 
# for oauth authentication with the twitter api
client_key = "66sIdXgLMzUlO7DHG3e7A"
client_secret = "bCkGtHVC1sOJC13HUJqESc5GlJl2McbtokG3R7gXIw"


# these are the user credentials for oauth authentication
# with the twitter api
user_token = ""
user_secret = ""


def get_token(client_key, client_secret, user_token, user_secret):

    oauth = OAuth1(client_key, client_secret)

    url = 'https://api.twitter.com/oauth/request_token'

    token_requests = requests.post(url, auth=oauth)

    credentials = parse_qs(token_requests.content)

    user_token = credentials.get('oauth_token')[0]

    user_secret = credentials.get('oauth_token_secret')[0]

    return user_token, user_secret


def authorize(client_key, client_secret, user_token, user_secret):

    url = 'https://api.twitter.com/oauth/authorize?oauth_token=' + user_token

    print ''
    print 'Copy Paste in your browser this link %s' % url
    print (
        'Click the authorize button to give TweeтCoммander access to your'
        ' twitter account information and put the pin code in the prompt'
        ' below.'
    )
    print ''
    print '+----------------------------------------------+'

    verifier = raw_input('Put your PIN code here: ')

    return verifier


def get_access(client_key, client_secret, user_token, user_secret, verifier):

    url = 'https://api.twitter.com/oauth/access_token'

    oauth = OAuth1(client_key,
                   client_secret,
                   user_token,
                   user_secret,
                   verifier=verifier)

    access_request = requests.post(url=url, auth=oauth)

    credentials = parse_qs(access_request.content)
    
    user_token = credentials.get('oauth_token')[0]
    user_secret = credentials.get('oauth_token_secret')[0]

    dbm_create(user_token, user_secret)


def connection(client_key=client_key, client_secret=client_secret):

    user_token, user_secret = dbm_fetch()

    oauth = OAuth1(client_key, client_secret, user_token, user_secret)

    return oauth


def first_time_oauth(client_key=client_key, client_secret=client_secret, 
                     user_token=user_token, user_secret=user_secret):

    print (
        'This is your first time with TweeтCoммander.' 
        ' Please follow the instructions below.'
    )
    user_token, user_secret = get_token(client_key, client_secret, 
                                        user_token, user_secret)

    verifier = authorize(client_key, client_secret, user_token, user_secret)

    get_access(client_key, client_secret, user_token, user_secret, verifier)
