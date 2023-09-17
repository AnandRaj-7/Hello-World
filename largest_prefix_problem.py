'''14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sortest = strs[0]
        prefix = ''
        chars = ''
        result = False
        for i in range(1,len(strs)):
            if (len(strs[i])<len(sortest)):
                sortest = strs[i]
            else:
                continue
        prefix = sortest
        for string in strs:
            chars = ''
            i = 0
            for letter in prefix:
                if letter == string[i]:
                    chars = chars + letter
                    i = i + 1
                else:
                    break
            if len(chars)<len(prefix):
                prefix = chars
        return prefix
strs = ["flower","flow","flight"]
strs1 = ["Dog", "Cat", "Car"]
strs2 = ["Dominic","Dog", "Dogly"]
solution = Solution()
print("The string list is ",strs)
print("The longet common prefix is "+solution.longestCommonPrefix(strs))
print("The string list is ",strs1)
print("The longet common prefix is "+solution.longestCommonPrefix(strs1))
print("The string list is ",strs2)
print("The longet common prefix is "+solution.longestCommonPrefix(strs2))