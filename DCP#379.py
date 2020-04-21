from itertools import combinations

class StringSubSequence():
    def __init__(self):
        self.inputString = input("What is your string??")
        self.combs = []

    def sequence_string(self):
        i = 1
        while i < len(self.inputString):
            comb = combinations(self.inputString, i)
            seqSub = list(comb)
            self.combs += seqSub
            i += 1
        return self.combs


obj = StringSubSequence()
print(obj.sequence_string())