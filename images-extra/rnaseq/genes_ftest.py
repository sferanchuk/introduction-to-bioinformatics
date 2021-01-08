
import scipy.stats as stats
import math

ndic = [ "SRR1141179", "SRR1552967", "SRR1813003" ]

stages = [ { "brown" : [ "SRR1141188", "SRR1141189", "SRR1141193", "SRR1141196", "SRR1141213", "SRR1141214", "SRR1141216" ],
			 "cleavage" : [ "SRR1141187", "SRR1141201", "SRR1141203", "SRR1141210", "SRR1141218", "SRR1141223", "SRR1141237" ],
			 "cloud" : [ "SRR1141180", "SRR1141182", "SRR1141190", "SRR1141192", "SRR1141211", "SRR1141217", "SRR1141220" ],
			 "spot" : [ "SRR1141198", "SRR1141204", "SRR1141209", "SRR1141219", "SRR1141222", "SRR1141224", "SRR1141230" ] },
			{ "brown" : [ "SRR1552971", "SRR1552970", "SRR1552975", "SRR1552994", "SRR1553026", "SRR1553025", "SRR1553029" ],
			  "cleavage" : [ "SRR1552969", "SRR1553001", "SRR1553005", "SRR1553016", "SRR1553031", "SRR1553065", "SRR1553066" ],
			  "cloud" : [ "SRR1553017", "SRR1553030", "SRR1553034" ], 
			  "spot" : [ "SRR1552996", "SRR1553006", "SRR1553014", "SRR1553032", "SRR1553040", "SRR1553044", "SRR1553053" ] },
			{ "brown" : [ "SRR1813010", "SRR1813011", "SRR1813012", "SRR1813013", "SRR1813014", "SRR1813015" ],
			  "cleavage" : [ "SRR1813001", "SRR1813003", "SRR1813005", "SRR1813006", "SRR1813008", "SRR1813009" ],
			  "spot" : [ "SRR1813016", "SRR1813017", "SRR1813018", "SRR1813019", "SRR1813020", "SRR1813021" ] } ]
			
experiment3 = [ "SRR1813003", "SRR1813005", "SRR1813006", "SRR1813008", "SRR1813009", "SRR1813010", "SRR1813011", "SRR1813012", "SRR1813013", "SRR1813014", "SRR1813015", "SRR1813016", "SRR1813017", "SRR1813018", "SRR1813019", "SRR1813020", "SRR1813021", "SRR1813022", "SRR1813023", "SRR1813024", "SRR1813025", "SRR1813026", "SRR1813027", "SRR1813028", "SRR1813029", "SRR1813030", "SRR1813031", "SRR1813032", "SRR1813034", "SRR1813036", "SRR1813037", "SRR1813038", "SRR1813040", "SRR1813041", "SRR1813042", "SRR1813047", "SRR1813050", "SRR1813052", "SRR1813054", "SRR1813055", "SRR1813058", "SRR1813061", "SRR1813063", "SRR1813064", "SRR1813065", "SRR1813067", "SRR1813068", "SRR1813070", "SRR1813072", "SRR1813074", "SRR1813078", "SRR1813080", "SRR1813081", "SRR1813084", "SRR1813085", "SRR1813087", "SRR1813088", "SRR1813090", "SRR1813091" ]
			
			
ifile = open( "amph_emap.txt" )

volumes = ifile.readline().strip().split( "\t" )[ 1: ]

groups = [ "brown", "cleavage", "spot" ]

gnums = {}

acnum = 0
pgnum = 0

for vnum in range( len( volumes ) ):
	volume = volumes[ vnum ]
	vgroup = int( volume[1] )
	if vgroup >= len( ndic ):
		continue
	if vgroup != pgnum:
		acnum = vgnum + 1
		pgnum = vgroup
	vgnum = int( volume[ 3 : ] )
	sname = "SRR" + str( int( ndic[ vgroup ][ 3: ] ) + vgnum - acnum ) 
	if vgroup == 2:
		if vgnum == acnum:
			continue
		sname = experiment3[ vgnum - acnum - 1 ] 
	for group in groups:
		if sname in stages[ vgroup ][ group ]:
			gnums[ vnum ] = group

			
genes = []
gmeasure = []

for line in ifile:
	ls = line.strip().split( "\t" )
	gene = ls[0]
	expression = map( float, ls[1:] )
	rlist = [ [] for i in xrange( len( groups ) ) ]
	for vnum in range( len( expression ) ):
		if vnum in gnums:
			rlist[ groups.index( gnums[ vnum ] ) ].append( expression[ vnum ] )
	( fstat, pvalue ) = stats.f_oneway( *rlist )
	genes.append( gene )
	gmeasure.append( pvalue )
	
gorder = sorted( range( len( gmeasure ) ), key = lambda k: gmeasure[k] )

dgenes = []
for k in range( len( gorder ) ):
	if gmeasure[ gorder[ k ] ] > 0.001:
		break
	dgenes.append( genes[ gorder[ k ] ] )
	
dgset = set( dgenes )
gset = set( genes )

ggroups = []
groupmeasure = []

with open( "kgroups1.txt" ) as gf:
	for line in gf:
		ggenes = line.strip().split()
		intersect = len( dgset and set( ggenes ) )
		cintersect = len( gset and set( ggenes ) )
		ctable = [ [ intersect, cintersect  - intersect ], [ len( dgset ), len( gset ) - len( dgset ) ] ]
		( oddsratio, pvalue ) = stats.fisher_exact( ctable )
		if float( ctable[0][0] ) / cintersect < float( ctable[1][0] ) / len( gset ):
			continue
		ggroups.append( ggenes[:] )
		groupmeasure.append( pvalue )
		if len( ggroups ) > 1000:
			break
	
grouporder = sorted( range( len( groupmeasure ) ), key = lambda k: groupmeasure[k] )

selgroups = [ ggroups[ grouporder[k] ] for k in range( 3 ) ]
selgenes = set( selgroups[0] )

gexpr = [ [] for k in xrange( len( gnums ) ) ] 

ifile.seek( 0 )
ifile.readline()

for line in ifile:
	ls = line.strip().split( "\t" )
	gene = ls[0]
	if not gene in selgenes:
		continue
	expression = map( float, ls[1:] )
	vind = 0
	for vnum in range( len( expression ) ):
		if vnum in gnums:
			gexpr[ vind ].append( expression[ vnum ] )
			vind += 1

rgnums = [ [] for k in xrange( len( groups ) ) ]
vind = 0
for vnum in range( len( expression ) ):
	if vnum in gnums:
		rgnums[ groups.index( gnums[ vnum ] ) ].append( vind )
		vind += 1
		
gcenters = [ [ 0 ] * len( selgenes ) for k in xrange( len( groups ) ) ]
gkcenters = []

for cc in range( 3 ): 
	mmeasure = 0
	cnum = -1
	for vind in rgnums[ cc ]:
		for gind in range( len( selgenes ) ):
			gcenters[ cc ][ gind ] += gexpr[ vind ][ gind ] / len( rgnums[cc] )
		cmeasure = 0
		for vind2 in rgnums[ cc ]:
			if vind == vind2:
				continue
			corr, pvalue = stats.kendalltau( gexpr[ vind ], gexpr[ vind2 ] )
			cmeasure += -( math.log( pvalue ) )
		if cmeasure > mmeasure:
			mmeasure = cmeasure
			cnum = vind
	gkcenters.append( gexpr[ cnum ][:] )

gdists = [ [ 0 ] * len( gnums ) for k in xrange( len( groups ) ) ]

for cc in range( 3 ): 
	for vind in range( len( gnums ) ):
		esum = 0
		for gind in range( len( selgenes ) ):
			diff = gkcenters[ cc ][ gind ] - gexpr[ vind ][ gind ]
			esum += diff * diff
		corr, pvalue = stats.kendalltau( gcenters[ cc ], gexpr[ vind ] )
		lpv = -math.log( max( pvalue, 1e-40 ) )
		gdists[ cc ][ vind ] = float( corr ) #lpv * lpv )
		
print gdists
