#!/usr/bin/env python3
#-*- encodeing: utf-8 -*-

def table_99():
    for i in range(1,10):
        for j in range(1,10):
            if j<=i:
                print('%d x %d = %d ' % (j,i, j*i), end='')
        print('')

table_99()
