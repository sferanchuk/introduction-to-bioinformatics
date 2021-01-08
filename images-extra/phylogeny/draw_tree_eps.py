#!/usr/bin/python
# -*- coding: utf-8 -*-


#import numpy as np
import matplotlib
#from matplotlib import gridspec
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import math
from Bio import Phylo
#from StringIO import StringIO
import sys

fig = plt.figure( figsize=(10,10), dpi=80 )
tree = Phylo.read( sys.argv[1], 'newick' )
Phylo.draw( tree )
plt.savefig( sys.argv[2] )

