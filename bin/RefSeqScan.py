#!env/bin/python

from optparse import OptionParser
from refseqscan.main import main
import datetime
import sys


ver = '0.1.0'

# Command line argument parsing
descr = 'RefSeqScan v'+ver
parser = OptionParser(version=ver, description=descr)
parser.add_option('-i', default=None, dest='input', action='store', help="Input RefSeq database file")
parser.add_option('-r', default=None, dest='reference', action='store', help="Reference genome file")
parser.add_option('-o', default='output.txt', dest='output', action='store', help="Output file name [default value: %default]")
(options, args) = parser.parse_args()

if options.input is None:
    sys.exit('\nInput RefSeq database file not specified.')
if options.reference is None:
    sys.exit('\nReference genome file not specified.')

# Welcome message
print '\n'+'='*100
print 'RefSeqScan v'+ver+' started: '+str(datetime.datetime.now())+'\n'

main(options)

# Goodbye message
print '\nFinished: '+str(datetime.datetime.now())
print '='*100+'\n'