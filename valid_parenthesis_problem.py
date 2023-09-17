'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        check = True
        check_dict = {')':'(', '}':'{' , ']':'['}
        open_br = 0
        close_br = 0
        for i in range(0,len(s)):
            if s[i] in ['(','{','[']:
                list1.append(s[i])
                open_br = open_br + 1
            else:
                close_br = close_br + 1
                if len(list1)>0:
                    if (list1[len(list1)-1] == check_dict[s[i]]):
                        list1.pop(len(list1)-1)
        if((open_br - close_br)==0 and len(list1) == 0):
            ckeck = True
        else:
            check = False
        return check
#class __main__ :
solution = Solution()
s = "()[]{}"
t = "()]{}"
u = "({["
v = "})]"
w = "({)}[]"
x = "({[]})"
y = "(){[]}"
if (solution.isValid(s)):
    print("The string "+ s + " contains a valid parentheses sequence.")
else :
    print("parentheses sequence " + s + " is invalid!!!")
if (solution.isValid(t)):
    print("The string contains "+ t +" a valid parentheses sequence.")
else :
    print("parentheses sequence "+ t +" is invalid!!!")
if (solution.isValid(u)):
    print("The string contains "+ u +"  a valid parentheses sequence.")
else :
    print("parentheses sequence "+ u +"  is invalid!!!")
if (solution.isValid(v)):
    print("The string contains  "+ v +" a valid parentheses sequence.")
else :
    print("parentheses sequence  "+ v +" is invalid!!!")
if (solution.isValid(w)):
    print("The string contains  "+ w +" a valid parentheses sequence.")
else :
    print("parentheses sequence  "+ w +" is invalid!!!")
if (solution.isValid(x)):
    print("The string contains  "+ x +" a valid parentheses sequence.")
else :
    print("parentheses sequence  "+ x +" is invalid!!!")
if (solution.isValid(y)):
    print("The string contains  "+ y +" a valid parentheses sequence.")
else :
    print("parentheses sequence  "+ y +" is invalid!!!")