
import math

keys = [ "protein", "expression", "cell", "patient" ] 
years = [ "2003", "2012" ]
sizebase = 200				
print "<svg height=\"%d\" width=\"%d\">" % ( sizebase, 2 * sizebase )

rangelimit = 100
ynum = 0
radii = [ dict( [ ( key, 0. ) for key in keys ] ) for yc in xrange( len( years ) ) ]

print "<defs>"

for year in years:
	kstats = dict( [ ( key, [ 0 ] * rangelimit ) for key in keys ] )
	maxrange = dict( [ ( key, 0 ) for key in keys ] )
	maxcount = 0
	

	with open( year + "-m.txt" ) as f:
		for line in f:
			p1 = line.find( "<S>" ) + 3
			p2 = line.find( "</>", p1 )
			p3 = p2 + 6
			p4 = line.find( "</>", p3 )
			mem = line[ p1 : p2 - 1 ].split()
			mem_size = len( line[ p3 : p4 - 1 ].split( "," ) )
			for key in keys:
				if key.upper() in mem:
					kstats[ key ][ mem_size ] += 1
					maxrange[ key ]  = max( maxrange[ key ], mem_size )
					maxcount = max( maxcount, kstats[ key ][ mem_size ] )

	for key in keys:
		print "<radialGradient id=\"grad_" + key + year + "\" cx=\"50%\" cy=\"50%\" r=\"50%\" fx=\"50%\" fy=\"50%\">" 
		
		rbase = sum( kstats[key] )
		curnum = 0 #int( 0.5 * rbase )
		maxnum = rbase + curnum
		rangedic = {}
		for lsize in range( 3, maxrange[ key ] ):
			rangedic[ maxrange[key] + 2 - lsize ] = curnum
			curnum += kstats[ key ][ lsize ]

		opshift = 1.1
		for lsize in range( 3, maxrange[ key ] ):#rgb(96,124,60)
			print "<stop offset=\"%5.1f%%\" style=\"stop-color:#d45500;stop-opacity:%5.3f\" />" % ( float( maxnum - rangedic[ lsize ] ) * 100.0 / maxnum, float( ( maxrange[key] - lsize + opshift ) ) / ( maxrange[key] + opshift - 3 ) ) 

		print "</radialGradient>"
		radii[ ynum ][ key ] = 0.007 * math.sqrt( sum( kstats[key] ) ) * sizebase
	ynum += 1

print "</defs>" 

ynum = 0
for year in years:
	points = dict( [ ( keys[ knum ], int( ( knum + 1.5 ) * sizebase * 0.7  ) / len( keys ) ) for knum in range( len( keys ) ) ] )
	for key in keys:
		radius = radii[ ynum ][ key ]
		point = ( points[key] + ynum * sizebase, sizebase - points[key] )
		print "<ellipse cx=\"%d\" cy=\"%d\" rx=\"%4.1g\" ry=\"%4.1g\" fill=\"url(#grad_%s)\" style=\"stroke:#803300;stroke-width:0.4\" />" % ( point[0], point[1], radius, radius, ( key + year ) )
		print "<text fill=\"black\" font-size=\"8\" font-family=\"Times\" x=\"%d\" y=\"%d\">%s</text>" % ( point[0] + 0.03 * sizebase, point[1], key )
	print "<text fill=\"black\" font-size=\"10\" font-family=\"Times\" x=\"%d\" y=\"%d\">%s</text>" % ( sizebase * ( 0.2 + ynum ), sizebase * 0.1, year )
	ynum += 1
	
print "</svg>"
		