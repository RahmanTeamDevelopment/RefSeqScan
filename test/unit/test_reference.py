from unittest import TestCase
from refseqscan.reference import Reference

class TestReference(TestCase):

    def test_get_sequence(self):
        ref = Reference('/Users/munz/root/work/data/genomes/GRCh37/human_g1k_v37.fasta')

        assert ref.get_sequence('1', 231762560, 231762589) == 'GGAAGGAGCAGGAGGCAGCCCAGGCGGAG'
        assert ref.get_sequence('Z', 231762560, 231762589) is None
        assert ref.get_sequence('MT', 0, 100) == ref.get_sequence('MT', -10, 100)
        assert ref.get_sequence('MT', 120, 100) == ''
        assert ref.get_sequence('MT', 0, 99999999999) == ref.get_sequence('MT', 0, 99999999998)


