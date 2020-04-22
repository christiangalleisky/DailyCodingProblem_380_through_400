class GapList():

    def __init__(self):
        self.list = [1, 2, 3, 5, 8, 12]
        self.missingNums = []

    def makeOriginList(self):
        print("DUH")

    def sortList(self):
        sorted(self.list)

    def findGaps(self):
        i = 0
        while i < len(self.list) - 1:
            if (self.list[i] + 1) != self.list[i+1]:
                diff = abs(self.list[i] - self.list[i+1]) - 1
                k = 0
                while k < diff:
                    num = self.list[i] + 1
                    self.missingNums.append(num + k)
                    k += 1
            i += 1
        return self.missingNums

obj = GapList()
print(obj.findGaps())