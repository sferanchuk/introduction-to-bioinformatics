
from mpl_toolkits.mplot3d import axes3d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import random

random.seed(a=2)

coords = [ [], [], [] ]
dirs = [ [], [], [] ]


for i in range( 20 ):
   module = 0.2
   mnorm = 0.01
   coords[ 0 ].append( random.uniform( 0, 1 ) )
   coords[ 1 ].append( random.uniform( 0, 1 ) )
   coords[ 2 ].append( random.uniform( 0, 1 ) )
   dirs[ 0 ].append( random.expovariate( module ) * random.choice( [ -1., 1. ] ) * mnorm )
   dirs[ 1 ].append( random.expovariate( module ) * random.choice( [ -1., 1. ] ) * mnorm )
   dirs[ 2 ].append( random.expovariate( module ) * random.choice( [ -1., 1. ] ) * mnorm )

fig = plt.figure( figsize=(15,15), dpi=80 )
ax = fig.gca(projection='3d')

ax.quiver( coords[0], coords[1], coords[2], dirs[0], dirs[1], dirs[2], arrow_length_ratio = 0.3 )#colors = [ ( 0, 0, 0.5, 0.8 ) ] * len( coords[0] ) )
ax.scatter(  coords[0], coords[1], coords[2], s=200, c="#36648B", depthshade=False )
ax.set_xticklabels( [] )
ax.set_yticklabels( [] )
ax.set_zticklabels( [] )
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')

plt.savefig( "idealgas.png" )
