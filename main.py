class Sequence:

    def __init__(self, seq):
        self.__sequence = seq

    def getlength(self):
        return len(self.__sequence)

    def setSequence(self, seq):
        self.__sequence = seq

    def getSequence(self):
        return self.__sequence


class Protein(Sequence):

    def __init__(self, seq):
        self.setSequence(seq)
        super().__init__(self.__sequence)
        #super is hetzelfde als Sequence

    def setSequence(self, seq):
        match = "re.search([BJOUXZ][0-9]", seq)



def main():



main()
