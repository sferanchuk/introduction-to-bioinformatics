#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid( np.arange( -0.7, 0.8, .2), np.arange( -0.7, 0.8, .2) )
#r = np.square( X ) + np.square( Y )
rX = np.sqrt( np.square( X ) + np.square( X.transpose() ) ) * 1.5
rY = np.sqrt( np.square( Y ) + np.square( Y.transpose() ) ) * 1.5
UC = X / rX
US = -X / rX
VC = Y / rY
VS = -Y / rY

fig, ax = plt.subplots( 1, 3, figsize=(30,10), dpi=80 )
#ax1.set_title('Arrows scale with plot width, not view')
ax[0].quiver( X, Y, VC, US, units='width', width = 0.004 )
ax[1].quiver( X, Y, US, VS, units='width', width = 0.004 )
ax[2].quiver( X, Y, UC, VS, units='width', width = 0.004 )
for pn in range( 3 ):
	ax[ pn ].set_xticks( [] )
	ax[ pn ].set_yticks( [] )
	ax[ pn ].set_xlabel( "x", size = 36 )
	ax[ pn ].set_ylabel( "y", size = 36 )
ax[ 0 ].set_title( u"Фокус (im)", size = 36 )
ax[ 1 ].set_title( u"Узел (-/-)", size = 36 )
ax[ 2 ].set_title( u"Седло (+/-)", size = 36 )

#Q = ax[3].quiver( X, Y, US, VS, units='width' )
#qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E', coordinates='figure')
fig.tight_layout()
plt.savefig( "poincare.png" )