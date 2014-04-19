#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import readline
import twitter

from user_credentials_dbm import db_path
from oauth import first_time_oauth
from packages.clint.textui import colored


# This is the main program of tweetcommander 
# you can execute it directly from your terminal 
# with python tweetcommander.py or just tweetcommander.py
def main():

    tweetcommander = twitter.tweetcommander();

    # Print welcome screen
    tweetcommander.welcome()
	
    # if the tweetcomm.db file doesn't exists 
    # in your ~/.config/tweetcommander path 
    # then it executes the oauth authentication
    if not os.path.exists(db_path):
        first_time_oauth()
        print 'Now you can use TweeтCoммander.'
        db_exists = True
    else:
        db_exists = True

    # core loop of the application takes an input option and print the results
    while db_exists:   	    
        # if eveything is ok tweetcommader waits for an input option
        action = raw_input(colored.red('> '))
        # if no action or non valid input print error message
        tweetcommander.commands(action)


if __name__ == "__main__":
    main()
