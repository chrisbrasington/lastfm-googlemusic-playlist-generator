#lastfm-grooveshark-playlist-generator

Goal: to takes top recently played music from a LAST.FM user and sent it to GROOVESHARK as a playlist to share.

Language: python

###keys.py 

Not included in repository, but add your keys to a python file as such..

```
class grooveshark:
    key = ''
    secret = ''
    username = ''
    password = ''


class lastfm:
    key = ''
    secret = ''
    username = ''
    password = ''
```

####last.fm api: [get API Key](http://www.last.fm/api/account/create), [documentation](http://www.last.fm/api)

####grooveshark api: [request API key](http://developers.grooveshark.com/api), [documentation](http://developers.grooveshark.com/docs/public_api/v3/), [sandbox](http://developers.grooveshark.com/docs/public_api/v3/sandbox)

### pyLast
[code.google.com/p/pylast/](https://code.google.com/p/pylast/)

A python interface to last.fm

### Grooveshark Public API Wrapper
[kaitlin/Grooveshark](https://github.com/kaitlin/Grooveshark)

This is a pretty simple python wrapper for the grooveshark [public api](http://developers.grooveshark.com/api).