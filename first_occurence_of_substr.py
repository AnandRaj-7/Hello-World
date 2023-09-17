'''28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_size = len(needle)
        h_size = len(haystack)
        i = 0
        index = -1
        if n_size > h_size:
            return index
        else:
            while(i<h_size):
                count = 0
                j = 0
                chars = haystack[i:i+n_size]
                if len(chars)<n_size:
                    return index
                while j < n_size:
                    if needle[j] != chars[j]:
                        break
                    else:
                        count = count + 1
                        if count == n_size:
                            index = i
                            return index
                    j = j + 1
                i = i + 1
            return index        
haystack = "mississippi"
needle = "issipi"
s = Solution()
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")
haystack = "sadbutsad"
needle = "sad"
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")
haystack = "ssadbutsad"
needle = "sad"
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")
haystack = "abcdefgh"
needle = "issipi"
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")
haystack = "aaa"
needle = "aaaa"
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")
haystack = "thisissad"
needle = "sad"
ix = s.strStr(haystack,needle)
print("Haystack : ",haystack)
print("Needle : ",needle)
print(f"The Needle {needle} is present at index {ix} in Haystack {haystack}")