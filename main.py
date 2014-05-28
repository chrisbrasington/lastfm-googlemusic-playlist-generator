##import sys
import pylast
import pygrooveshark
from keys import lastfm

LASTFM_KEY = ''
LASTFM_SECRET = ''
LASTFM_USERNAME = ''
LASTFM_PASSWORD = ''

LASTFM_NETWORK  = ''
GROOVESHARK_NETWORK = ''
	  
def init(key='', secret=''):
    global LASTFM_KEY
    global LASTFM_SECRET
    global LASTFM_USERNAME
    global LASTFM_PASSWORD
    global LASTFM_NETWORK
    global GROOVESHARK_NETWORK
    LASTFM_KEY = lastfm.key
    LASTFM_SECRET = lastfm.secret
    USERNAME = lastfm.username
    PASSWORD = pylast.md5(lastfm.password)
    LASTFM_NETWORK = pylast.LastFMNetwork(api_key = LASTFM_KEY, api_secret = LASTFM_SECRET, username = LASTFM_USERNAME, password_hash = LASTFM_PASSWORD)
    GROOVESHARK_NETWORK = pygrooveshark.GrooveSharkNetwork()

if __name__ == '__main__':
    init()
    
    raylinth = pylast.User('raylinth',LASTFM_NETWORK)
    print 'lastfm user: ', raylinth.name
    
    recenttrack =  raylinth.get_recent_tracks(1)[0].track
    artist = recenttrack.get_artist().name

    print 'last artist: ', artist
    
    groovedata = GROOVESHARK_NETWORK.get_song_search_results(artist,limit=1)
    print '\ngrooveshark song search: \n\n',groovedata
    
