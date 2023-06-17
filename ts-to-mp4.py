#!/usr/local/opt/python/bin/python2.7
# Required ffmpeg

import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
count = 0


def is_entry_exists(dir_name):
  path = os.path.join(BASE_DIR, dir_name)
  if not os.path.isdir(path):
    os.mkdir(path)


def get_videos():
  is_entry_exists('videos')
  videos_dir = os.path.join(BASE_DIR, 'videos')
  videos = os.listdir(videos_dir)
  return videos, videos_dir


videos, videos_dir = get_videos()

for video in videos:
  if (video.split(".")[-1].lower() == 'ts'):
    filePath = os.path.join(videos_dir, video)
    mp4FilePath = os.path.join(videos_dir, os.path.splitext(video)[0] + ".mp4")
    if os.path.isfile(mp4FilePath):
      continue
    os.system("ffmpeg -i " + "\"" + filePath + "\""  + " \"" + mp4FilePath + "\"")
    count = count + 1
    print("\"" + filePath + "\"")
print("Done the total number of file was be converted: ", count)
