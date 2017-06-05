#!/usr/bin/env python
"""
Fix the modified time of all Apple Photos exported .MOV files in one directory.
"""

import sys
import os
import glob
import subprocess as sp
from time import strptime, strftime


def fix_mov_timestamp(path='./'):
    """
    Touch the modified timestamp of all .MOV files in a directory with
    quicktime.creationdate.
    """
    for mov in glob.iglob(os.path.join(os.path.abspath(path), '*.MOV')):
        ts = str(sp.check_output(
            'mplayer -vo null -ao null -frames 0 -identify ' + mov +
            ' 2>/dev/null|grep quicktime.creationdate:', shell=True))

        # Format as '2017-05-21T15:32:35-0700'
        ts = ts.split('quicktime.creationdate: ')[1].split('\\')[0]

        # Format as '201705211532.35'
        timestr = strftime('%Y%m%d%H%M.%S',
                           strptime(ts, '%Y-%m-%dT%H:%M:%S%z'))

        # touch access and modification time stamp
        sp.run('touch -amt ' + timestr + ' ' + mov, shell=True)


if __name__ == '__main__':
    fix_mov_timestamp(sys.argv[1])
