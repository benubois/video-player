import youtube_dl
import sys
import urllib
from objc_util import nsurl,UIApplication

ydl_opts = {
    'format': 'best[ext=mp4]/best',
    'simulate': True,
    'quiet': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    source_url = sys.argv[1]
    info = ydl.extract_info(source_url, download = False)

    base_url = 'https://watchable-video.github.io/player'

    query = urllib.parse.urlencode({
        'url': info.get('url'),
        'poster': info.get('title', ''),
        'title': info.get('thumbnail', '')
    })

    url = base_url + '?' + query

    app = UIApplication.sharedApplication()
    app.openURL_(nsurl(url))
