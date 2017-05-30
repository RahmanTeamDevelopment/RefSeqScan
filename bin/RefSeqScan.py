#!env/bin/python

import datetime
from optparse import OptionParser
from refseqscan.main import main


ver = '0.1.0'

# Command line argument parsing
descr = 'refseq_scan v'+ver
parser = OptionParser(usage='python path/to/refseq_scan/refseq_scan.py <options>', version=ver, description=descr)
parser.add_option('-i', "--in", default=None, dest='input', action='store', help="Input RefSeq database file")
parser.add_option('-r', "--ref", default='...', dest='reference', action='store', help="Reference genome file [default value: %default]")
parser.add_option('-o', "--out", default='output.txt', dest='output', action='store', help="Output file name [default value: %default]")
(options, args) = parser.parse_args()

# Welcome message
print '\n'+'='*100
print 'refseq_scan v'+ver+' started: '+str(datetime.datetime.now())+'\n'

main(options)

# Goodbye message
print '\nFinished: '+str(datetime.datetime.now())
print '='*100+'\n'