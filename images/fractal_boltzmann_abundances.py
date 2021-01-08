#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import numpy as np
#from sklearn import linear_model
import scipy.stats as stats
#import json
import os.path
import collections
import operator
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import skbio.diversity as skdiv


reader = csv.reader(open( "ginipaper_sedata.txt" ), delimiter='\t')
data = list(reader)
edata = []

for sd in data:
	if ( sd[0] == "mqw" and sd[2] == "6" and sd[3] == "sd" ):
		sd5 = sd[5].split( " " )
		sd5.remove( "" )
		si = map( int, sd5 )
		if len( si ) < 100:
			continue
		edata.append( si )

fig, ax = plt.subplots( 1, 1, figsize=(15,15), dpi=80 )	

ymax = 0

for si in edata:
	accsum = 1
	tsum = len( si )
	vsum = sum( si )
	underest = max( 200 - tsum, 0 )
	ymax = max( ymax, tsum + underest )
	y_x = []
	y_y = []
	y_xlin = []
	for k in range( len( si ) ):
		y_y.append( math.log( k + 1 + underest ) )#- math.log( tsum + underest ) )
		y_x.append( math.log( si[k] ) )
		y_xlin.append( si[k] )
		
	npoints = int( tsum * 0.5 )
	nppoints = int( tsum * 0.7 )
	(a_s,b_s,r,tt,stderr) = stats.linregress( y_xlin[-npoints:], y_y[ -npoints:] )
	#print "%g %g" % ( a_s, b_s )

	y_xboltz = y_x[ -nppoints: ] 
	y_yboltz = []
	for x in y_xboltz:
		y_yboltz.append( math.exp( x ) * a_s + b_s )
	ax.scatter( y_x, y_y, c="#6666aa", edgecolors="none" )
	ax.plot( y_x, y_y, c="#535366", lw=.7 )
	ax.plot( y_xboltz, y_yboltz, c ="black", lw = 2, ls = "dashed" )
ax.set_yticks( [ math.log( math.exp( max( y_y ) ) - 150 ), math.log( math.exp( max( y_y ) ) - 50 ) , max( y_y ) ] )
ax.set_yticklabels( [ "-150", "-50", u"Макс." ], size=22, rotation="vertical" , va="center")
ax.set_ylabel( u"Порядковый номер", size=32 ) 
ax.set_xticks( [ 0, math.log( 10 ), math.log( 100 ), math.log( 1000 ) ] )
ax.set_xticklabels( [ "0", "10", "100", "1000" ], size=22 )
ax.set_xlabel( u"Количество", size=32 ) 

plt.tight_layout()
plt.savefig( "fractal_boltzmann_abundances.png" )
	

