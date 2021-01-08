#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib
from matplotlib import gridspec
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
from Bio import Phylo
from StringIO import StringIO

gs = gridspec.GridSpec( 1, 4, width_ratios = [ 1, 1, 1, 0.7 ] )
fig = plt.figure( figsize=(25,10), dpi=80 )

scmap = { "CEU" : "#6666aa", "JPT": "#806046",  "CHB": "#806046", "YRI": "#c45555", "LWK": "#c45555", "MKK": "#c45555", "MXL" : "#ad9657", "TSI" : "#6666aa", "GIH" : "#2b6b42" }

aut_sel = """
((((((NA20847_GIH:18.1067,NA20845_GIH:18.0548):4.8426,NA20846_GIH:22.6956):1.4676,NA20850_GIH:23.9672):2.2316,(((((NA20510_TSI:17.7302,NA20509_TSI:17.8350):4.8668,NA20502_TSI:22.5174):2.7030,(NA20511_TSI:18.1823,NA06994_CEU:18.1954):6.9642):0.0000,NA06985_CEU:24.8760):1.2325,NA19649_MXL:25.7321):1.6717):0.6086,(((NA19735_MXL:18.2055,NA19670_MXL:17.9040):8.2782,(((NA18956_JPT:16.6804,NA18947_JPT:16.6479):6.1358,(NA18942_JPT:16.6588,NA18940_JPT:16.5946):6.1576):1.0177,(NA18558_CHB:21.8925,((NA18555_CHB:16.4810,NA18526_CHB:16.4716):4.4670,NA18537_CHB:20.6162):1.4115):1.7402):3.6631):0.9505,NA19669_MXL:27.2695):0.5923):4.9643,(((((((NA19239_YRI:17.6840,NA18502_YRI:17.6218):4.7445,NA18501_YRI:22.1619):1.4864,NA19238_YRI:23.3927):1.1715,NA19017_LWK:24.2914):0.5608,NA19025_LWK:24.6785):0.3803,NA19026_LWK:24.8949):0.5058,NA19020_LWK:25.2074):5.3814);
"""

mt_sel = """
(((NA19670_MXL:46.5874,(NA20510_TSI:45.4032,((NA20502_TSI:19.7254,((NA20511_TSI:17.1441,NA20509_TSI:16.4804):5.2477,NA20850_GIH:22.6760):2.8111):8.3857,((((NA18947_JPT:33.2622,NA18537_CHB:21.7608):9.1924,NA18555_CHB:29.7182):3.9068,(NA06994_CEU:26.2150,NA06985_CEU:36.8599):15.2853):0.2630,(NA20847_GIH:41.3275,(NA19735_MXL:11.3614,(NA19669_MXL:6.7833,NA19649_MXL:11.3273):7.0212):24.5685):8.3315):0.2075):2.6653):1.1879):8.9659,((((NA20846_GIH:3.0829,NA20845_GIH:8.9597):11.0769,NA18940_JPT:27.4872):8.1031,((NA19025_LWK:36.6862,NA18942_JPT:38.6557):13.9743,(NA18956_JPT:20.8791,NA18526_CHB:33.7365):14.7730):1.6189):0.5636,NA18558_CHB:39.0060):12.8236):0.5461,(((NA19239_YRI:71.7440,NA18501_YRI:55.9210):11.6456,(NA19026_LWK:5.6339,NA19017_LWK:6.0567):48.0204):3.6375,((NA19238_YRI:6.4642,NA18502_YRI:21.6814):7.1880,NA19020_LWK:18.3826):22.9433):0.4845);
"""

y_sel = """
(NA18940_JPT:120.4349,((NA19670_MXL:72.8442,((NA20511_TSI:16.3809,NA06994_CEU:17.0121):58.4329,(NA18558_CHB:64.1353,(NA19735_MXL:43.4602,(NA20845_GIH:40.3244,((NA20509_TSI:8.7128,NA19649_MXL:8.1193):21.7487,(NA20846_GIH:6.9580,NA20850_GIH:8.6474):24.4271):8.5782):9.3561):20.0022):5.0595):4.1480):29.8782,((NA20510_TSI:60.7027,(NA19026_LWK:18.5374,((NA19025_LWK:5.3344,NA19020_LWK:5.8093):5.4579,NA18501_YRI:7.6502):7.6962):40.5940):16.3093,NA19239_YRI:68.1889):22.9555):0);
"""


snmap = {}
sndic = {}

tree = Phylo.read( StringIO( aut_sel ), 'newick' )
terminals = tree.get_terminals()
for t in terminals:
	tn = t.name
	tng = tn[ -3: ]
	if not tng in sndic:
		sndic[ tng ] = 1
	snmap[ tn ] = tng + str( sndic[ tng ] )
	sndic[ tng ] += 1


def plot_tree( fn, title, axnum, lim ):
	#print fn
	maxdate = 0
	tree = Phylo.read( StringIO( fn ), 'newick' )
	scexmap = {}
	terminals = tree.get_terminals()
	#print terminals
	for t in terminals:
		tn = t.name
		tng = tn[ -3: ]
		if tn in snmap:
			scexmap[ snmap[tn] ] = scmap[ tng ]
			
	def labelfunc( n ):
		sn = str( n )
		if sn != 'Clade':
			snm = sn[-3:] 
			if sn in snmap:
				return snmap[ sn ]
			else:
				return snm
		return ''
	#Phylo.draw( tree, label_func = labelfunc, label_colors = scmap, axes=ax[ cax ] )	
	cax = plt.subplot( gs[ axnum ] )
	Phylo.draw( tree, label_colors = scexmap, label_func = labelfunc, axes=cax )	
	cax.set_title( title, loc="center", size=24 )
	cax.set_yticks( () )
	cax.set_ylabel( "" )
	#cax.set_xlabel( u"длины ветвей, тыс. лет", size = 20 )
	cax.set_xlabel( "" )
	cax.set_xlim( [-5, lim + 5 ] )
	cax.tick_params( axis='x', labelsize = 20 )
	cax.set_xticks( () )
	cax.axis( "off" )

matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['font.weight'] = "bold"
plot_tree( aut_sel, u"Полный геном", 0, 40 )
plot_tree( mt_sel, u"Митохондриальная ДНК", 1, 100 )
matplotlib.rcParams['font.size'] = 16
plot_tree( y_sel, u"Y-хромосома", 2, 200 )
matplotlib.rcParams['font.weight'] = "normal"

rcolors = [ "#6666aa", "#806046", "#2b6b42", "#c45555", "#ad9657" ]
rlabels = [ u"Европа", u"Восточная Азия", u"Индия", u"Африка", u"Америка" ]
rlnum = len( rcolors )
		   
axlegend = plt.subplot( gs[ 3 ] )
axlegend.barh( range( rlnum ), [ 1 ] * rlnum, height = 0.5, align = "edge", color = rcolors )
for k in range( rlnum ):
	axlegend.text( 1.5, k + 0.05, rlabels[k], ha="left", va="bottom", size = 20 )
axlegend.set_xlim( [ 0, 5 ] )
axlegend.set_ylim( [ -1, 12 ] )
axlegend.set_xticks( () )
axlegend.set_yticks( () )
axlegend.axis('off')

plt.tight_layout()
plt.savefig( "h_evol.png" )
plt.savefig( "h_evol.svg" )
