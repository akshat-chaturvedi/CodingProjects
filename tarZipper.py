#!/usr/bin/env python3

import sys
import shutil

shutil.make_archive(sys.argv[1], 'gztar', sys.argv[2])