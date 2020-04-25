class largest_range_inclusive():

    def __init__(self, arr):
        self.array_of_nums = arr

    def sortArray(self):
        sorted(self.array_of_nums)

    def find_differences(self):
        differenceList = []
        x, y, i = 0, 1, 0
        smallestNum, largestNum = self.array_of_nums[0], None
        while i < len(self.array_of_nums) - 1:
            if self.array_of_nums[x] == self.array_of_nums[y] - 1:
                largestNum = self.array_of_nums[y]
            elif self.array_of_nums[x] != self.array_of_nums[y] - 1:
                smallestNum = self.array_of_nums[y]
                largestNum = self.array_of_nums[y]
            i += 1
            x += 1
            y += 1
            differenceList.append((smallestNum, largestNum))
        return differenceList

    def find_largest_group(self, list):
        z = list[0][1] - list[0][0]
        j = list[0][0]
        for x, y in list:
            k = abs(x - y)
            if k > z:
                z = k
                j = x
        return z, j #max difference and starting integer

    def produce_sequence(self, max_diff, start_num):
        sequence = []
        i = 0
        while i <= max_diff:
            sequence.append(start_num + i)
            i += 1
        return sequence

obj = largest_range_inclusive([1, 2, 3, 5, 6, 8, 9, 10, 11, 12])
obj.sortArray()
diffList = obj.find_differences()
x, y = obj.find_largest_group(diffList) #x = max difference and y = starting number
seq = obj.produce_sequence(x, y)
print(seq)
