import dbm
import os
import shutil

# create a path to the database directory
db_path = os.path.join(os.getenv('XDG_CONFIG_HOME', os.path.expanduser("~/.config")), 'tweetcommander')

def dbm_create(user_token, user_secret, path=db_path):
	# this function create the dbm file in USER/.config/tweetcommander directory

	# create the path directory
	os.mkdir(db_path)
	# and change the cwd to the path
	os.chdir(db_path)

	# create the dbm file
	user_credentials = dbm.open('tweetcomm', 'c')
	# store the credentials in to the dbm file
	user_credentials['token'] = user_token
	user_credentials['secret'] = user_secret
	# and close the database
	user_credentials.close()


def dbm_fetch(path=db_path):

	# change the cwd to the path
	os.chdir(db_path)

	# create the dbm file
	user_credentials = dbm.open('tweetcomm', 'c')

	return user_credentials['token'], user_credentials['secret']

def delete_dbm(path=db_path):
    
    # delete path to the dbm file
    shutil.rmtree(db_path)

    # check if directory is deleted
    if not os.path.exists(db_path):
        print 'Your credentials are deleted. Goodbye.'
    else:
        print 'It seems your credentials are still there.'
        print 'Go to ' + db_path + ' and delete the tweetcommander directory manually.'
