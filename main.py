##import sys
import pylast
import pygrooveshark
import hashlib
from keys import lastfm, grooveshark

LASTFM_NETWORK = ''
GROOVESHARK_NETWORK = ''

def init():
    global LASTFM_NETWORK
    global GROOVESHARK_NETWORK
    LASTFM_NETWORK = pylast.LastFMNetwork(api_key=lastfm.key, api_secret=lastfm.secret, username=lastfm.username,
                                          password_hash=pylast.md5(lastfm.password))
    GROOVESHARK_NETWORK = pygrooveshark.GrooveSharkNetwork()


if __name__ == '__main__':
    init()

    '''
    raylinth = pylast.User('raylinth', LASTFM_NETWORK)
    print 'lastfm user: ', raylinth.name

    recenttracks = raylinth.get_recent_tracks()
    lasttrack = recenttracks[0].track
    artist = lasttrack.get_artist().name
    print 'last listened to: ', lasttrack
    '''

    #groovedata = GROOVESHARK_NETWORK.get_song_search_results(lasttrack.title, limit=1)
    # faking the request temporarily
    #groovedata = GROOVESHARK_NETWORK.api_call('getSongSearchResults', {'query': 'coloris', 'country': '', 'limit': 5, 'offset': ''})
    lasttrack = 'Coloris'
    artist = 'she'
    groovedata = {u'header': {u'hostname': u'RHL072'}, u'result': {u'songs': [{u'SongID': 36034397, u'IsLowBitrateAvailable': True, u'Popularity': 1407500203, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Autumn in Space'}, {u'SongID': 35760171, u'IsLowBitrateAvailable': True, u'Popularity': 1407500033, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Coloris'}, {u'SongID': 27275619, u'IsLowBitrateAvailable': True, u'Popularity': 1404500008, u'AlbumName': u'Chapter 2', u'AlbumID': 4016513, u'ArtistID': 222614, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'Lesi\xebm', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 3391872, u'IsLowBitrateAvailable': True, u'Popularity': 1404500006, u'AlbumName': u'Illumination', u'AlbumID': 169595, u'ArtistID': 222614, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'Lesi\xebm', u'CoverArtFilename': u'169595.png', u'SongName': u'Coloris'}, {u'SongID': 36043054, u'IsLowBitrateAvailable': True, u'Popularity': 1401300006, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'your love'}, {u'SongID': 37698125, u'IsLowBitrateAvailable': True, u'Popularity': 1402600005, u'AlbumName': u'none', u'AlbumID': 8512888, u'ArtistID': 28821, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'She', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 36043058, u'IsLowBitrateAvailable': True, u'Popularity': 1403500005, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'drones'}, {u'SongID': 36043052, u'IsLowBitrateAvailable': True, u'Popularity': 1404500004, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'traveling by night'}, {u'SongID': 29384567, u'IsLowBitrateAvailable': True, u'Popularity': 1330400003, u'AlbumName': u'www.biggreenbeats.com', u'AlbumID': 5828552, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'5828552.jpg', u'SongName': u'Coloris'}, {u'SongID': 30531410, u'IsLowBitrateAvailable': True, u'Popularity': 1403500003, u'AlbumName': u'Replay Music 2010-12-29', u'AlbumID': 6244862, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 36034291, u'IsLowBitrateAvailable': True, u'Popularity': 1407100003, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Gum'}, {u'SongID': 36034428, u'IsLowBitrateAvailable': True, u'Popularity': 1407300002, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'In Time'}, {u'SongID': 36034444, u'IsLowBitrateAvailable': True, u'Popularity': 1407400001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Destination Luna4'}, {u'SongID': 23343628, u'IsLowBitrateAvailable': True, u'Popularity': 1326300001, u'AlbumName': u'Illumination', u'AlbumID': 3553964, u'ArtistID': 180987, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'Lesiem', u'CoverArtFilename': u'3553964.jpg', u'SongName': u'Coloris'}, {u'SongID': 34851248, u'IsLowBitrateAvailable': True, u'Popularity': 1317200001, u'AlbumName': u'She', u'AlbumID': 4198023, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'she', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 29999475, u'IsLowBitrateAvailable': True, u'Popularity': 1324100001, u'AlbumName': u'-', u'AlbumID': 6049626, u'ArtistID': 1856255, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'Coloris (S-T3RRA Remix)', u'CoverArtFilename': u'', u'SongName': u'She'}, {u'SongID': 33894157, u'IsLowBitrateAvailable': True, u'Popularity': 1315000001, u'AlbumName': u'My Little DJ Tunes', u'AlbumID': 6763690, u'ArtistID': 2237716, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'markingdude', u'CoverArtFilename': u'', u'SongName': u"Wrappin' Up The Coloris"}, {u'SongID': 36198447, u'IsLowBitrateAvailable': True, u'Popularity': 1325500001, u'AlbumName': u'http://AmigaRemix.com/', u'AlbumID': 4062684, u'ArtistID': 1189577, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'daXX', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 36034486, u'IsLowBitrateAvailable': True, u'Popularity': 1407000001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Together'}, {u'SongID': 36034327, u'IsLowBitrateAvailable': True, u'Popularity': 1407500001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Tokyo Nights'}, {u'SongID': 36034550, u'IsLowBitrateAvailable': True, u'Popularity': 1405700001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Distort Into Me'}, {u'SongID': 36034350, u'IsLowBitrateAvailable': True, u'Popularity': 1406500001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Monochrome'}, {u'SongID': 36034265, u'IsLowBitrateAvailable': True, u'Popularity': 1405800001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Orbit'}, {u'SongID': 36034375, u'IsLowBitrateAvailable': True, u'Popularity': 1407500001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Fuse'}, {u'SongID': 36043048, u'IsLowBitrateAvailable': True, u'Popularity': 1405900001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Touch and Go'}, {u'SongID': 36034531, u'IsLowBitrateAvailable': True, u'Popularity': 1407500001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Reality'}, {u'SongID': 36034226, u'IsLowBitrateAvailable': True, u'Popularity': 1407500001, u'AlbumName': u'Coloris', u'AlbumID': 2854239, u'ArtistID': 402877, u'Flags': 0, u'IsVerified': True, u'ArtistName': u'she', u'CoverArtFilename': u'2854239.jpg', u'SongName': u'Circuit Lover'}, {u'SongID': 40111888, u'IsLowBitrateAvailable': True, u'Popularity': 0, u'AlbumName': u'b', u'AlbumID': 9351820, u'ArtistID': 28821, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'She', u'CoverArtFilename': u'', u'SongName': u'Coloris'}, {u'SongID': 23105376, u'IsLowBitrateAvailable': True, u'Popularity': 0, u'AlbumName': u'Illumination', u'AlbumID': 3424444, u'ArtistID': 1173259, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'Lesi?m', u'CoverArtFilename': u'3424444.jpg', u'SongName': u'Coloris'}, {u'SongID': 27932581, u'IsLowBitrateAvailable': True, u'Popularity': 0, u'AlbumName': u'trancemission', u'AlbumID': 5311458, u'ArtistID': 1647888, u'Flags': 0, u'IsVerified': False, u'ArtistName': u'Lesi\xffm', u'CoverArtFilename': u'', u'SongName': u'Coloris'}]}}
    #print '\ngrooveshark song search: \n', groovedata, '\n'

    for track in groovedata['result']['songs']:
        # print track['SongName']
        if track['SongName'] == lasttrack and track['ArtistName'] == artist:
            print 'found'
            groovedata = track
            break

    print groovedata

    playlist = 'generator'
    print 'SongID: ', groovedata['SongID']

    # create the playlist
    #
    sessionID = GROOVESHARK_NETWORK.api_call('startSession')['result']['sessionID']
    print '\nsession established: ', sessionID
    token = hashlib.md5(grooveshark.username.lower() + hashlib.md5(grooveshark.password).hexdigest()).hexdigest()
    #print 'token: ', token

    auth = GROOVESHARK_NETWORK.api_call('authenticateUser', {'username': grooveshark.username, 'token': token})
    print '\nauthenticate\n', auth

    #response = GROOVESHARK_NETWORK.api_call('createPlaylist', sessionID, {'name': playlist, 'songIDs': groovedata['SongID']})
    #response = GROOVESHARK_NETWORK.api_call('createPlaylist', sessionID, {'name': playlist, 'songIDs': '35760171'})
    #print '\ncreate playlist\n', response
    # why do you fail when I specify songIDs, yet can create an empty playlist...

    playlistID = 98294973
    songID = 35760171

    print 'manually adding song to playlist as test'

    playlistCheck = GROOVESHARK_NETWORK.api_call('getPlaylistSongs', {'playlistID': playlistID})
    print '\ncheck playlist exists\n', playlistCheck

    songCheck = GROOVESHARK_NETWORK.api_call('getSongsInfo', {'songIDs': songID})
    print '\ncheck song exists: ', songID
    print songCheck

    print 'manually using playlist: ', playlistID
    response = GROOVESHARK_NETWORK.api_call('setPlaylistSongs', {'playlistID': playlistID, 'songIDs': songID})
    print '\nadd to playlist:\n ', response['result']['success']
    print response

    if not response['result']['success']:
        print '\nwhy FUCKING NOT? hm?'

    # getSongURLFromSongID find the song...
    # I can create an empty playlist so session is working...
    # failing to add songs to playlist.... songIDs... string.. why

