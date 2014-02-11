TweeтCoммander
==============

Latest release and installation instructions http://raqqun.github.io/tweetcommander/


TweeтCoммander is a command line twitter client, written in python, for people who love minimalism and command line simplicity.


Features
========

- View and update home timeline
- View who's tweeting and from who's retweet
- View your timeline and the timeline of a specific user
- Send tweets
- Make retweets
- Favorite a tweet
- Revoke access to your account


modules used
-------------

requests, requests_oauthlib, oauthlib, clint

TODO
----


- fix issues with json parsing and tweets pages
- add support for directs messages

Examples
========

	# to update your timeline and get the last 20 tweets if there is much
	# if not prints out as many tweets since your last update
	# you can also put a number after tl action to fetch a specific number of tweet ex. tl 30
	> tl
	1 1 @realdemgr from @Revoltistanbul
	Animate Gezi
	#OccupyGezi
	#direngeziparkı 
	#direngezi
	http://t.co/TOkag6FX22

	1 2 @NikSfikas
	όταν ήρθαν να πάρουν εσένα οι γείτονες γελούσαν χωρίς να ξέρουν 
	οτι και αυτούς θα τους έπαιρναν

	1 3 @MavriMelani
	Ποιος/α θα βαλει ενα γαματο τραγουδι για να παω να ξεραθω ηρεμος αποψε;;;

	1 4 @kanekos69 from @f_head_entropy
	πηρα δυο χαπια της επομενης ημερας.αρχιδια...ακομα τεταρτη ειναι.

	1 5 @kanaliotis
	Μη σε φοβίζουν... Τρόμαξέ τους, ΕΣΥ!!!: http://t.co/DZLdt93qxx via @youtube

	1 6 @kanekos69 from @MilkosV
	Απόψε θυμηθήκαμε τα ωραιότερα μας χρόνια, η συναυλία των Pet Shop Boys 
	δεν χανόταν με τίποτα. Βουλή και νομοσχέδια θα υπάρχουν και αυριο.

	1 7 @NikSfikas
	όταν σας πήγαν εκεί που σας πήγαν, εσένα και τον γείτονα, 
	πλακωνόσαστε και έριχνε την ευθύνη ο ένας στον άλλον
	
	
	# to fetch tweet from a specific user
	# you can also omit the number and fetch directly the 20 last tweet
	> utl
	Who's timeline you want to see ? > raqqun
	How many tweets you want to see ? > 30 

	# to post a tweet to your timeline 
	> tw "your fancy tweet"

	# to make a retweet
	> rt 1 6
	
	# to favorite a tweet
	> fv 1 1
	
	# quit TweeтCoммander
	> /q
	
	# print help screen with TweeтCoммander actions
	> /h


