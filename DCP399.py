class threePartitions():

    def __init__(self, nums):
        self.nums = nums


    def getIndices(self, iteration):
        indices= []
        i, x, y = 0, iteration, 1 #i is index var, x and y are functino vars
        while(i < iteration):
            if(iteration + 1 == x + y):
                indices.append((x, y))# 1,1/2,1-1,2/3,1-2,2-1,3 pattern
            x -= 1
            y += 1
            i += 1
        return indices #return list of tuples

    def generateSplicesAndCompareSums(self):
        i = 1
        while i < len(self.nums) - 1 :
            arr = self.getIndices(i)#Iterate through all possible combinations
            for a, b in arr:
                li = len(self.nums) - a - b
                left = self.nums[0: li: 1]#sub array
                ri = len(self.nums) - a
                center = self.nums[li: ri: 1] #sub array
                right = self.nums[ri: len(self.nums): 1] #sub array
                left_sum = 0
                center_sum = 0
                right_sum = 0
                for x in left:
                    left_sum += x
                for x in center:
                    center_sum += x
                for x in right:
                    right_sum += x
                if(left_sum == center_sum and left_sum == right_sum):
                    return left, center, right
            i += 1
        return None, None, None


x = [0, 1, 2, 3, 4, 2, 6]
print(x)

obj = threePartitions(x)
left, center, right = obj.generateSplicesAndCompareSums()
print(left)
print(center)
print(right)
