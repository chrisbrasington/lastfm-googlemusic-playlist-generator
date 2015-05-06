import pylast
from gmusicapi import Mobileclient
import datetime, time
from pprint import pprint
from keys import lastfm


LASTFM_NETWORK = ''
GOOGLE_NETWORK = ''#gmusicapi.MobileClient()

# initialize LASTFM, TINYSONG, and GROOVESHARK API connections
def init():
    global LASTFM_NETWORK
    global GOOGLE_NETWORK

    LASTFM_NETWORK = pylast.LastFMNetwork(api_key=lastfm.key, api_secret=lastfm.secret, username=lastfm.username,
                                          password_hash=pylast.md5(lastfm.password))

    GOOGLE_NETWORK = Mobileclient()

# authenticate with google music
def login():
    '''
    global api

    logged_in = False

    # ask user for credentials if not loaded
    if 'google' not in globals():
        username = raw_input('google email: ')
        password = getpass.getpass('password: ')
        logged_in = api.login(username, password)   
    else:
        logged_in = api.login(google.username, google.password)

    if logged_in:
        return True
    else:
        print 'unable to login to google music'
        return False
    '''

# convert datetime object to timestamp
def converttimestamp(t):
    timestamp = time.mktime(t.timetuple()) + t.microsecond / 1E6
    return timestamp

# off we go!
if __name__ == '__main__':
    # initialize API networks
    init()

    # lastFM user to create playlist from
    source = 'raylinth'
    #source = raw_input('UserName: ').lower()

    # time range: last month to current date
    timerange = 30

    # grooveshark playlist name
    playlistname = 'generator'

    # lastFM user to pull history from
    print 'lastfm souce: ', source

    # get source LASTM user
    source = pylast.User(source, LASTFM_NETWORK)

    # set time range - default last month
    from_date = converttimestamp(datetime.datetime.today() - datetime.timedelta(days=timerange))

    # request lastFM user.getWeeklyTrackChart
    print '\nrequesting recent lastFM tracks...'
    lastFMrecenttracks = source.get_weekly_track_charts(from_date)

    for tracks in lastFMrecenttracks:
        print tracks.item

    '''
    print 'received recent lastFM tracks'
    print 'grabbing IDs from TINYSONG...\n'
    print '----------'

    # song IDs array
    songs = []

    # find IDs from TINYSONG
    # limit to 20 searches to avoid exceeding rate limit
    count = 0
    limit = 20
    for t in lastFMrecenttracks:

        # artist, track title information, unicode safe
        track = t.item
        artist = track.artist.name.encode('utf-8').strip()
        title = track.title.encode('utf-8').strip()
        print artist, ' - ', title

        # search TINYSONG api
        results = TINYSONG_NETWORK.search(title+' '+artist)

        # accept 1st search result (seems pretty accurate)
        for song in results:
            print 'ID: ', song.song_id, ' ', song.artist_name, '-', song.song_name
        if results.__len__() > 0:
            songs.append(results[0].song_id)
        else:
            print 'Not Found, Skipping'
        print '----------'

        # break if at limit
        if count == limit:
            break
        count += 1

    # start the grooveshark session
    sessionID = GROOVESHARK_NETWORK.api_call('startSession')['result']['sessionID']
    print '\nsession established: ', sessionID

    # authenticate grooveshark user
    token = hashlib.md5(grooveshark.username.lower() + hashlib.md5(grooveshark.password).hexdigest()).hexdigest()
    auth = GROOVESHARK_NETWORK.api_call('authenticateUser', {'username': grooveshark.username, 'token': token})
    print '\nauthentication: ', auth['result']['success']

    # get user's playlists
    playlists = GROOVESHARK_NETWORK.api_call('getUserPlaylists',  {'limit': 50})['result']['playlists']

    # search for playlist name
    playlist = False
    for p in playlists:
        if p['PlaylistName'] == playlistname:
            playlist = p['PlaylistID']

    # create or update playlist
    if playlist:
        print '\nUPDATING existing generator playlist... '
        response = GROOVESHARK_NETWORK.api_call('setPlaylistSongs', {'playlistID': playlist, 'songIDs': songs})
    else:
        print '\nCREATING new generator playlist... '
        response = GROOVESHARK_NETWORK.api_call('createPlaylist', {'name': playlistname, 'songIDs': songs})
        playlist = response['result']['playlistID']

    # check playlist
    if response['result']['success']:
        print 'successful\n'
        playlistInfo = GROOVESHARK_NETWORK.api_call('getPlaylistInfo', {'playlistID': playlist})['result']
        print 'playlist info: '
        print 'name: generator'
        print 'ID: ', playlist

        playlistsongs = GROOVESHARK_NETWORK.api_call('getPlaylistSongs', {'playlistID': playlist})['result']['songs']
        print '\nplaylist songs:'
        for song in playlistsongs:
            print song['SongName'], ' - ', song['ArtistName']

    print '\nPlaylist generation complete.'
    '''









