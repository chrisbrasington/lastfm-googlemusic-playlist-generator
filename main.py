import sys
import api.lastfm.pylast as pylast
import api.grooveshark.grooveshark as pygrooveshark

import hashlib
from keys import lastfm, grooveshark

LASTFM_NETWORK = ''
GROOVESHARK_NETWORK = ''

# initialize LASTFM and GROOVESHARK API connections
def init():
    global LASTFM_NETWORK
    global GROOVESHARK_NETWORK
    LASTFM_NETWORK = pylast.LastFMNetwork(api_key=lastfm.key, api_secret=lastfm.secret, username=lastfm.username,
                                          password_hash=pylast.md5(lastfm.password))
    GROOVESHARK_NETWORK = pygrooveshark.GrooveSharkNetwork()

# off we go!
if __name__ == '__main__':
    init()

    # get recent tracks of LASTM user
    raylinth = pylast.User('raylinth', LASTFM_NETWORK)
    print 'lastfm user: ', raylinth.name
    lastFMrecenttracks = raylinth.get_recent_tracks()
    print 'received recent lastFM tracks'

    print 'searching for songs in grooveshark...\n'
    songs = []
    for lastFMtrack in lastFMrecenttracks:
        title = lastFMtrack.track.title.lower()
        artist = lastFMtrack.track.artist.name.lower()

        groovedata = GROOVESHARK_NETWORK.get_song_search_results(lastFMtrack.track.title)

        ####################################
        # problem with exceeding rate limit!
        # need to switch song searching to tinysong API

        if 'errors' in groovedata:
            for error in groovedata['errors']:
                print error['message']
            sys.exit()

        for track in groovedata['result']['songs']:
            if track['SongName'].lower() == title and track['ArtistName'].lower() == artist:
               songs.append(track['SongID'])
               print 'found match: ', track['SongName'], ' - ', track['ArtistName']
            break;

    # start the grooveshark session
    sessionID = GROOVESHARK_NETWORK.api_call('startSession')['result']['sessionID']
    print '\nsession established: ', sessionID

    # authenticate grooveshark user
    token = hashlib.md5(grooveshark.username.lower() + hashlib.md5(grooveshark.password).hexdigest()).hexdigest()
    auth = GROOVESHARK_NETWORK.api_call('authenticateUser', {'username': grooveshark.username, 'token': token})
    print '\nauthentication: \n', auth['result']['success']

    # get user's playlists
    playlists = GROOVESHARK_NETWORK.api_call('getUserPlaylists',  {'limit': 50})['result']['playlists']

    playlist = False
    for p in playlists:
        if p['PlaylistName'] == 'generator':
            playlist = p['PlaylistID']

    # create or update playlist
    if playlist:
        print '\nUPDATING existing generator playlist... '
        response = GROOVESHARK_NETWORK.api_call('setPlaylistSongs', {'playlistID': playlist, 'songIDs': songs})
    else:
        print '\nCREATING new generator playlist... '
        response = GROOVESHARK_NETWORK.api_call('createPlaylist', {'name': 'generator', 'songIDs': songs})
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

    print 'done'







