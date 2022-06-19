
#  See if there is a duplicate in the array of numbers 
#  Brute force or Sort
#  
#  Brute force:
#  Time O(n log n) 
#  Space O(1)
#  
#  Sort using Hash set to detect duplicates 
#  Q2A: Does a certain value exist?
#  Once a number is in the hashset, the next time it shows up it is a duplicafte
#  
# Time and Space: O(n)


#leetcode can be real sensitive about the indentation 
# 
# Method 1: 
# Applying hashtables 


class Solution(object):
    def containsDuplicate(self, nums):
        hashNum = {}
        for i in nums:
            if i not in hashNum:
                hashNum[i] = 1
            else:
                return True
        return False
        
  
  
  