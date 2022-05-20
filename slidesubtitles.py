#!/usr/bin/env python3
import os
import sys
import re
import glob
from datetime import time, timedelta

def show(td):
  hours = f'{int(td.seconds / 3600):02d}'
  minutes = f'{int((td.seconds % 3600 / 60)):02d}'
  seconds = f'{int((td.seconds % 60)):02d}'
  ms = f'{int(td.microseconds / 1000):03d}'
  return f'{hours}:{minutes}:{seconds},{ms}'

delta = timedelta(seconds=-2.8)

stpat = re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d).*(\d\d):(\d\d):(\d\d),(\d\d\d)')
for infile in glob.glob('*.srt'):
    print(infile)
    with open(infile, 'r') as inf:
      subtitles = inf.readlines()
    for i in range(len(subtitles)):
      m = re.match(stpat, subtitles[i])
      if m:
        start = timedelta(hours=int(m.group(1)), minutes=int(m.group(2)), seconds=int(m.group(3)), milliseconds=int(m.group(4)))
        finish = timedelta(hours=int(m.group(5)), minutes=int(m.group(6)), seconds=int(m.group(7)), milliseconds=int(m.group(8)))
        start = start  + delta
        finish = finish + delta

        subtitles[i] = f'{show(start)} --> {show(finish)}\n'

    with open(infile, 'w') as out:
      for l in subtitles:
        out.write(l)

