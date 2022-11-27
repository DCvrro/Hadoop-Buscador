# -*-coding:utf-8 -*
#!/usr/bin/env python

import sys
import re
import os

txt = 1 
info = list() 
for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words = line.split('START')
    if(len(words) > 1 ): 
        txt = words[0]
        txt  = int(txt)
    words = line.split()
    for word in words:
        print('{} {} {}'.format(word,txt,1))
