#!/usr/bin/env python
import argparse
from datetime import datetime
import os
import sys

# Wrapper around `montage` command line tool from 
# ImageMagick for making diptychs
parser = argparse.ArgumentParser()
parser.add_argument("file1", help="First image file")
parser.add_argument("file2", help="Second image file")
parser.add_argument("--vertical", help="Make vertical diptych",
                    action="store_true")
parser.add_argument("--bordercolor", help="Border color")
parser.add_argument("--dryrun", help="Don't run montage",
                    action="store_true")
args = parser.parse_args()

f1 = args.file1
f2 = args.file2

mon_vertical = ""
if args.vertical:
  mon_vertical = " -tile 1x2 "

color = args.bordercolor
if not color:
  color = "black"
mon_color = " -bordercolor " + color + " "

f1name = os.path.splitext(os.path.basename(f1))[0]
f2name = os.path.splitext(os.path.basename(f2))[0]


outname = f1name + "_" + f2name + \
          datetime.today().strftime('%Y-%m-%d_%H%M%S') + ".png"

command = "montage -geometry +0+0 -border 5 " + mon_color + \
          " " + mon_vertical + " " + f1 + " " + f2 + " " + outname

if args.dryrun:
  print command
else:
  os.system(command)
  print "Created " + outname
