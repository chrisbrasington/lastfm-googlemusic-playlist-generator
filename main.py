##import sys
import pylast
import pygrooveshark
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

    # raylinth = pylast.User('raylinth', LASTFM_NETWORK)
    # print 'lastfm user: ', raylinth.name
    # recenttracks = raylinth.get_recent_tracks()
    # lasttrack = recenttracks[0].track
    # artist = lasttrack.get_artist().name
    # print 'last listened to: ', lasttrack

    # find recent track's songsIDs for grooveshark

    #groovedata = GROOVESHARK_NETWORK.get_song_search_results(lasttrack.title, limit=1)
    #print '\ngrooveshark song search: \n', groovedata, '\n'

    # check for first match
    # for track in groovedata['result']['songs']:
    #     # print track['SongName']
    #     if track['SongName'] == lasttrack and track['ArtistName'] == artist:
    #         print 'found'
    #         groovedata = track
    #         break
    # print groovedata

    #playlist = 'generator'
    #print 'SongID: ', groovedata['SongID']

    ###############################################################################################
    # FAKING REQUEST for testing manually

    # start the grooveshark session
    sessionID = GROOVESHARK_NETWORK.api_call('startSession')['result']['sessionID']
    print '\nsession established: ', sessionID

    # authenticate grooveshark user
    token = hashlib.md5(grooveshark.username.lower() + hashlib.md5(grooveshark.password).hexdigest()).hexdigest()
    auth = GROOVESHARK_NETWORK.api_call('authenticateUser', {'username': grooveshark.username, 'token': token})
    print '\nauthenticate\n', auth

    # create playlist with songs
    # PROBLEM: only adds empty playlist, failure with sending song IDs... tested in sandbox
    #response = GROOVESHARK_NETWORK.api_call('createPlaylist', sessionID, {'name': playlist, 'songIDs': groovedata['SongID']})
    #response = GROOVESHARK_NETWORK.api_call('createPlaylist', sessionID, {'name': playlist, 'songIDs': '35760171'})
    #print '\ncreate playlist\n', response

    # known existing playlist for my user
    playlistID = 98318603
    # known existing song
    songID = 35760171

    print 'manually adding song to playlist as test'

    # check playlist exists
    playlistCheck = GROOVESHARK_NETWORK.api_call('getPlaylistSongs', {'playlistID': playlistID})
    print '\ncheck playlist exists\n', playlistCheck

    songs = GROOVESHARK_NETWORK.api_call('getSongsInfo', {'songIDs': 35760171})['result']['songs']

    print '\nsong:\n', songs
    # check song exists
    # songCheck = GROOVESHARK_NETWORK.api_call('getSongsInfo', {'songIDs': songs})
    # print '\ncheck song exists: ', songID
    # print songCheck
    #
    # # add to playlist
    #print 'manually using playlist: ', playlistID
    #
    #response = GROOVESHARK_NETWORK.api_call('createPlaylist', {'name': 'generator', 'songIDs': songs})
    songs = ['35760171']

    playlists = GROOVESHARK_NETWORK.api_call('getUserPlaylists',  {'limit': 50})['result']['playlists']

    playlist = False
    for p in playlists:
        if p['PlaylistName'] == 'generator':
            playlist = p['PlaylistID']

    if playlist:
        print '\nUPDATING existing generator playlist... '
        response = GROOVESHARK_NETWORK.api_call('setPlaylistSongs', {'playlistID': playlist, 'songIDs': songs})
    else:
        print '\nCREATING new generator playlis... '
        response = GROOVESHARK_NETWORK.api_call('createPlaylist', {'name': 'generator', 'songIDs': songs})
        playlist = response['result']['playlistID']

    if response['result']['success']:
        print 'successful\n'
        playlistInfo = GROOVESHARK_NETWORK.api_call('getPlaylistInfo', {'playlistID': playlist})['result']
        print 'playlist info\n', playlistInfo

        playlistsongs = GROOVESHARK_NETWORK.api_call('getPlaylistSongs', {'playlistID': playlist})['result']['songs']
        print '\nplaylist songs:\n', playlistsongs








