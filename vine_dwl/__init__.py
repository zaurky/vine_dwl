# -*- coding: utf-8 -*-

"""
Usage :

from vine_dwl import VineDwl

url = 'https://vine.co/v/xyxyxyxy'
filename = '/tmp/test.flv'
VineDwl(url).write_video(filename)

"""

import urllib2
from BeautifulSoup import BeautifulSoup


class VineDwl(object):
    """
    Vine downloader class, get the vine url, download the video content
    """

    def __init__(self, url):
        self._url = url
        self._video_url = None

    @property
    def video_url(self):
        """ extracting url from html data gotten at `self.url` """
        if not self._video_url:
            soup = BeautifulSoup(urllib2.urlopen(self._url))
            source = soup.body.find('source', attrs={'type': 'video/mp4'})
            self._video_url = dict(source.attrs)['src']
            if not self._video_url.startswith('http'):
                self._video_url = self._video_url.replace('.*//', 'http://')

        return self._video_url

    def write_video(self, filename):
        """ write the video content into file `filename` """
        fhandle = open(filename, 'w')
        fhandle.write(urllib2.urlopen(self.video_url).read())
        fhandle.close()

    def get_video(self):
        """ return the video content """
        return urllib2.urlopen(self.video_url).read()
