from poolseq.processing.samtools.mpileup import Mpileup


class Samtools():

    def __init__(self, data):
        self.mpileup = Mpileup(data)