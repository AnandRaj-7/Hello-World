class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        i = 0
        while(i<len(nums)):
            if nums[i] == '_':
                break
            if val == nums[i]:
                nums[0:len(nums)] = nums[0:i]+nums[i+1:len(nums)] + ['_']
                print(nums)
            else:
                k = k + 1
                i = i + 1
        print(nums)
        return k
nums = [3,2,2,3]
val = 3
'''num1 = [0,1,2,2,3,0,4,2]
val1 = 2'''
solution = Solution()
key = solution.removeElement(nums,val)
print("The original list is: ", nums)
print(f"The number of element after removing {val} is {key}")
print("The list after modification is ",nums)
'''key = solution.removeElement(num1,val1)
print("The original list is: ", num1)
print(f"The number of element after removing {val1} is {key}")
print("The list after modification is ",num1)'''
#print("the list after slicing : ",nums[0:1])
#print("the original list is : ",nums)