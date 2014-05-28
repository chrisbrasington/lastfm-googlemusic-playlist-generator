import pprint
import pylast
from keys import keys

API_KEY = ''
API_SECRET = ''
USERNAME = ''
PASSWORD = ''
NETWORK  = ''  
	  
def init(key='', secret=''):
    ''' Create session'''
    if keys:
        global API_KEY
        global API_SECRET
        global USERNAME
        global PASSWORD
        global NETWORK
        API_KEY = keys.key
        API_SECRET = keys.secret
        USERNAME = keys.username
        PASSWORD = pylast.md5(keys.password)
        NETWORK = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = USERNAME, password_hash = PASSWORD)
	

if __name__ == '__main__':
	init()
	
	raylinth = pylast.User('raylinth',NETWORK)
	print raylinth.name
	print raylinth.get_recent_tracks(),'\n'
	
	geddy = pylast.User('eclisiast',NETWORK)
	print geddy.name
	print geddy.get_recent_tracks()