#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

def maxwell( t, v ):
	boltzmann_k = 1.38e-23
	pi = 3.14159
	mass = 14 * 1.66e-27
	return 4 * pi * v * v * math.pow( mass / ( 2 * pi * boltzmann_k * t ), 1.5 ) * math.exp( - mass * v * v / ( 2 * boltzmann_k * t ) )


fig, ax = plt.subplots( 1, 1, figsize=(20,12), dpi=80 )

trange = [ 173, 293, 873 ]

for t in trange:
	xcoord = range( 0, 1400 )
	p = [ maxwell( t, v ) for v in xcoord ]
	ax.plot( xcoord, p, c = "steelblue", lw = 3, ls = [ "solid", "dashed", "dotted" ][ trange.index( t ) ], label = str( t - 273 ) + u" °C" )

ax.set_xticks( [ 0, 500, 1000 ] )
ax.set_xticklabels( [ "0", "500", "1000" ], size=22 )
ax.set_xlabel( u"скорость, м/сек", size=32 )
ax.set_yticks( [ 0, 0.0005, 0.001, 0.0015 ] )
ax.set_yticklabels( [ "0", "1000", "2000", "3000" ], size=22 )
ax.set_ylabel( u"количество молекул, у.е.", size=32 )
ax.legend( loc = "upper right", fontsize=32 )

plt.savefig( "maxwell_distribution.png" )
