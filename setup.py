from setuptools import setup

setup(
    name = 'RefSeqScan',
    version = '0.2.0',
    description = 'A tool for finding discrepancies of RefSeq transcript sequences and the reference genome sequence',
    url = 'https://github.com/RahmanTeamDevelopment/RefSeqScan',
    author = 'Marton Munz',
    author_email = 'munzmarci@gmail.com',
    license = 'MIT',
    packages=['refseqscan'],
    scripts=['bin/RefSeqScan.py', 'bin/refseqscan'],
    zip_safe=False
)
