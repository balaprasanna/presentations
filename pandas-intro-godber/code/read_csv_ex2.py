#!/usr/bin/env python

import pandas as pd

phxtemps2 = pd.read_csv('phx-temps.csv', index_col=0,
                        names=['highs', 'lows'],
                        parse_dates=True)
print "=" * 80
print phxtemps2
print "=" * 80
print phxtemps2.head()
print "=" * 80
