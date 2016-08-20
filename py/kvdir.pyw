#!/usr/bin/python
# -*- coding: UTF-8 -*-

# KVdir v. 1.0.0

import sys
import os

Dirs = [ '1', '2', '3', '4', '5', '8', '9', '10', 'PDF', 'WEB', 'Реклама', ]
for i in range (len(Dirs)) :
    if not os.path.exists(Dirs[i]) :
        os.mkdir(Dirs[i])
sys.exit()