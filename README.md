#lastfm-googlemusic-playlist-generator
Python script which generates a google-music playlist from a lastFM user's play history for a time range.
Default time range is last month. Top songs are picked. Any lastFM user can be declared the source.

###last.fm api: [generate API Key](http://www.last.fm/api/account/create), [documentation](http://www.last.fm/api)
#### pyLast
[code.google.com/p/pylast/](https://code.google.com/p/pylast/)
A python interface to last.fm

###gmusicapi
Uses [gmusicapi](https://github.com/simon-weber/Unofficial-Google-Music-API) to authenticate and create a playlist on google-music. [Further documentation here](https://unofficial-google-music-api.readthedocs.org/en/latest/). **gmusicapi is not supported nor endorsed by Google,** but it is actively maintained.

###keys.py 
Not included in repository, but add your keys to a python file as such..

```
class lastfm:
    key = ''
    secret = ''

    username = ''
    password = ''

```


