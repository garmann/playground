#!/usr/bin/env python3

import progressbar
import time

# doc: http://pythonhosted.org/progressbar2/
# pip lastest version: progressbar2

count = 100

bar = progressbar.ReverseBar()
for i in bar(range(count)):
	time.sleep(0.2)