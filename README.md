#lastfm-grooveshark-playlist-generator

Generates a grooveshark playlist from a lastFM user's play history for a time range.

Default time range is last month. Top songs are picked. Default playlist size is 20. Any lastFM user can be declared the source.

Language: python

###keys.py 

Not included in repository, but add your keys to a python file as such..

```
# tinysong is used by grooveshark to find song IDs
# it has a higher rate limit of requests
# than grooveshark API search functionality
class tinysong:
    key = ''
    
class grooveshark:
    key = ''
    secret = ''
    
    # your grooveshark login information, where playlist is added
    username = ''
    password = ''

class lastfm:
    key = ''
    secret = ''
```

###tinysong api: [generate API Key](http://www.tinysong.com/api), [documentation](http://www.tinysong.com/api)
### - - pytinysong
[davidk/pytinysong](https://github.com/davidk/pytinysong)

A Python interface to the Tinysong (Grooveshark backed) service

###last.fm api: [generate API Key](http://www.last.fm/api/account/create), [documentation](http://www.last.fm/api)

### - - pyLast
[code.google.com/p/pylast/](https://code.google.com/p/pylast/)

A python interface to last.fm

###grooveshark api: [request API key](http://developers.grooveshark.com/api), [documentation](http://developers.grooveshark.com/docs/public_api/v3/), [sandbox](http://developers.grooveshark.com/docs/public_api/v3/sandbox)


### - - Grooveshark Public API Wrapper
[kaitlin/Grooveshark](https://github.com/kaitlin/Grooveshark)

This is a pretty simple python wrapper for the grooveshark [public api](http://developers.grooveshark.com/api).