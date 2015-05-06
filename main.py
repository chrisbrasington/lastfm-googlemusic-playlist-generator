import pylast, getpass
from gmusicapi import Mobileclient
import datetime, time
from pprint import pprint
from keys import lastfm

import sys

LASTFM_NETWORK = ''
GOOGLE_NETWORK = ''

# initialize LASTFM and GOOGLEMUSIC API
def init():
    global LASTFM_NETWORK
    global GOOGLE_NETWORK

    LASTFM_NETWORK = pylast.LastFMNetwork(api_key=lastfm.key, api_secret=lastfm.secret, username=lastfm.username,
                                          password_hash=pylast.md5(lastfm.password))

    GOOGLE_NETWORK = Mobileclient()

    google_login()

# authenticate with google music
def google_login():
    global GOOGLE_NETWORK

    logged_in = False

    # ask user for credentials if not loaded
    if 'google' not in globals():
        username = raw_input('google email: ')
        password = getpass.getpass('password: ')
        logged_in = GOOGLE_NETWORK.login(username, password)   
    else:
        logged_in = GOOGLE_NETWORK.login(google.username, google.password)

    if logged_in:
        print 'Logged into google music.\n'
        return True
    else:
        print 'unable to login to google music'
        return False

# convert datetime object to timestamp
def convert_time_stamp(t):
    timestamp = time.mktime(t.timetuple()) + t.microsecond / 1E6
    return timestamp

# get individual song ID for google musc
def get_song_id(song):
    global GOOGLE_NETWORK
    try:
    	result = GOOGLE_NETWORK.search_all_access(song,10)
    # occasionally creating bad search
    except:
    	return False
    
    # take first song hit
    if len(result['song_hits']) > 0:
    	found_song = result['song_hits'][0]
    	id = found_song['track']['nid']
    	return id
    else:
    	return False

# off we go!
if __name__ == '__main__':
    # initialize API networks
    init()

    # lastFM user to create playlist from
    source = raw_input('LastFM UserName: ').lower()

    # time range: last month to current date
    timerange = 30

    # set time range - default last month
    from_date = convert_time_stamp(datetime.datetime.today() - datetime.timedelta(days=timerange))

    # grooveshark playlist name
    playlist_name = 'lastfm ' + source + ' ' + str(datetime.datetime.today())

    # get source LASTM user
    source = pylast.User(source, LASTFM_NETWORK)

    # song id array (added per season to single playlist)
    song_ids = []

    # request lastFM user.getWeeklyTrackChart
    print '\nrequesting last month\'s lastFM tracks...'
    lastFMrecenttracks = source.get_weekly_track_charts(from_date)

    # for each track found in lastFM's recent tracks
    for tracks in lastFMrecenttracks:
        # search for song_id in google music
        search = str(tracks.item)
        id = get_song_id(search)
        print search,
        if(id):
            print str(tracks.item)
            song_ids.append(id)
            print ' ('+ id +')'
        else:
            print ' (not found)'

    # create playlist in google music
    print '\nCreating playlist: ' + playlist_name
    playlist_id = GOOGLE_NETWORK.create_playlist(playlist_name)
    
    GOOGLE_NETWORK.add_songs_to_playlist(playlist_id, song_ids)
    
    print 'Done'
