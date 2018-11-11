import youtube_dl
import sys
import urllib
from objc_util import nsurl,UIApplication

ydl_opts = {
    'format': 'best[ext=mp4]/best',
    'simulate': True,
    'quiet': True,
    'forceurl': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(sys.argv[1], download = False)
	
    base_url = 'https://watchable-video.github.io/player'
    video_url = info['url']
    title = info['title']
    poster = info['thumbnail']
	
    args = {
        'url': video_url, 
        'poster': poster,
        'title': title
	}
	url = base_url + '?' + urllib.parse.urlencode(args)
	
	app = UIApplication.sharedApplication()
	app.openURL_(nsurl(url))
