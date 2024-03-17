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
        
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                count += 1
        return count