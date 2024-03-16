class Solution(object):
    def getConcatenation(self, nums):
       nums.extend(nums)
       return nums

class Solution(object):
    def buildArray(self, nums):
        mylist = []
        for i in range(len(nums)):
            mylist.append(nums[nums[i]])
        return mylist