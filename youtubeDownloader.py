# how to download youtube playlist videos all at once
import random as rd

from mhyt import yt_download
from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PLB6MUoMXv9xcGOPDraWI707O7Zj5qVrDW')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video_url in playlist.video_urls:
    yt_download(video_url, "download_{}.mp4".format(rd.randint(1, len(playlist.video_urls))))
