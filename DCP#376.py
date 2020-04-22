class manhattenDistance():

    def __init__(self):
        print("How many coins would you like?")
        self.coins = int(input())
        self.coinTuple = ()
        self.tockenCoordinates = ()
        self.eachDistance = []
        i = 0
        while i < self.coins:
            print("x coordinate of coin")
            x = int(input())
            print("y coordinate of coin")
            y = int(input())
            self.coinTuple += (x, y)
            i += 1
        print("x coordinate of main token")
        x = int(input())
        print("y coordinate of main token")
        y = int(input())
        self.tokenCoordinates= (x, y)

    def getDistances(self):
        i= 0
        while i < (len(self.coinTuple)) // 2:
            x = abs(self.coinTuple[2*i] - self.tokenCoordinates[0])
            y = abs(self.coinTuple[2*i + 1] - self.tokenCoordinates[1])
            self.eachDistance.append(x + y)
            i += 1
        s = min(self.eachDistance)
        return s


obj = manhattenDistance()
print(obj.getDistances())