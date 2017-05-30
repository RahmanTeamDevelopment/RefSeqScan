import sys
import datetime
from utils.transcripts import TranscriptDB
from reference import Reference


def reverse_complement(s):
    """Return reverse complement sequence"""

    ret = ''
    complement = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N", "a": "t", "t": "a", "c": "g", "g": "c", "n": "n"}
    for base in s[::-1]:
        ret += complement[base]
    return ret


def get_reference_sequence(transcript, reference):
    """Return reference cDNA sequence of transcript"""

    exonseqs = []
    for exon in transcript.exons:
        if transcript.strand == '+':
            exonseq = reference.getSequence(transcript.chrom, exon.start+1, exon.end)
        else:
            exonseq = reverse_complement(reference.getSequence(transcript.chrom, exon.start+1, exon.end))
        exonseqs.append(exonseq)
    return ''.join(exonseqs)


def compare_sequences(ref, seq, cdna_coding_start, cdna_coding_end):
    """Compare transcript sequence with reference"""

    if ref == seq: return '.'
    if len(ref) != len(seq):
        return 'lengthChange'
    ret = []
    for i in range(len(ref)):
        if ref[i] != seq[i]:
            pos = i + 1
            if pos < cdna_coding_start: coord = str(pos - cdna_coding_start)
            elif pos > cdna_coding_end: coord = '+'+str(pos - cdna_coding_end)
            else: coord = str(pos - cdna_coding_start + 1)
            ret.append('c.'+coord+ref[i]+'>'+seq[i])
    return ','.join(ret)


def main(options):
    """Main function"""

    # Print reference genome name
    print 'Reference genome: ' + options.reference
    print ''

    # Initialize Reference object
    reference = Reference(options.reference)

    # Initialize output file
    outfile = open(options.output, 'w')
    outfile.write('#Created: ' + datetime.datetime.now().strftime("%d-%m-%Y") + '; Reference genome: ' + options.reference + '\n')
    outfile.write('#' + '\t'.join(['ID', 'VERSION', 'DIFFS']) + '\n')

    sys.stdout.write('Processing transcripts ... ')
    sys.stdout.flush()

    # Transcript database
    tdb = TranscriptDB(options.input)

    # Iterate through transcripts
    for transcript in tdb.generator():

        # Retrieve reference sequence corresponding to transcript
        ref = get_reference_sequence(transcript, reference)

        # Compare transcript sequence with reference sequence
        diffs = compare_sequences(ref, transcript.sequence, transcript.cdna_coding_start, transcript.cdna_coding_end)

        # Write results to output file
        outfile.write('\t'.join([transcript.id, transcript.version, diffs]) + '\n')

    print '- Done'

    # Close output files
    outfile.close()

    # Print output file name
    print '\nOutput file (' + options.output + ') created'

