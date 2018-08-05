#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('hello, %s' % 'world')
print("hello world")

#format output
print("%.2f%%" % ((85 - 72)*100/85 ))
# ''' for print n lines
print('''aaa
bbb
ccc
''')

#r'' for avoid Escape String
print("\r\n\\\\")
print(r"\r\n\\\\")
#len function, encode function
print(len('中文'.encode('utf-8')))

#decode bytes to utf-8 b'\xe4\xb8\ad'='中', ignore the error byte xff
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


exit()
