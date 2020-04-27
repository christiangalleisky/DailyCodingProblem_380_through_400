class anagram_match():

    def __init__(self):
        self.arr_x = []

    def sort(self, arr):
        z = 0
        while z < len(arr):
            x = str(arr[z])
            y = ''.join(sorted(x))
            y = y.strip("\"\'[]")
            self.arr_x.append([y, arr[z]])
            z += 1
        self.arr_x.sort()
        print(self.arr_x[0][0])#second parameter 1 is unsorted 0 is sorted

    def generate_list(self):
        handle = self.arr_x[0][0]
        i = 0
        returnable = []
        while i < len(self.arr_x):
            if handle != self.arr_x[i][0]:
                handle = self.arr_x[i][0]
            returnable.append(self.arr_x[i][0])
            i += 1
        return returnable


words = [['eat'], ['ate'], ['apt'], ['pat'], ['tea'], ['now']]
obj = anagram_match()
obj.sort(words)
print(obj.generate_list())