class mailman():

    def __init__(self):
        self.timelist = [[1, 0, "pickup"], [1, 3, "dropoff"], [2, 2, "pickup"], [3, 3, "pickup"], [3, 4, "dropoff"], [2, 5, "dropoff"]]
        self.totalActiveTime = 0

    def calculate_Active_Time(self):
        x = 0
        while x < len(self.timelist):
            i = x + 1
            if self.timelist[x][2] == "pickup":
                while i < len(self.timelist):
                    if self.timelist[i][2] == "dropoff" and self.timelist[i][0] == self.timelist[x][0]:
                        self.totalActiveTime += self.timelist[i][1] - self.timelist[x][1]
                    i += 1
            x += 1
        return self.totalActiveTime

obj = mailman()
print(obj.calculate_Active_Time())