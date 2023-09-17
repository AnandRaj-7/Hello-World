'''21. Merge Two Sorted Lists

"""""This works well on my personal computer""""


Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.'''
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 == None):
            return list2
        elif(list2 == None):
            return list1
        elif(list1.val == 0 and list1.next == None):
            return list2
        elif(list2.val == 0 and list2.next == None):
            return list1
        else:
            list3 = ListNode()
            p1 = list1
            p2 = list2
            p3 = list3
            while(p1.next != None and p2.next != None):
                if(p1.val <= p2.val):
                    p3.val = p1.val
                    p3.next = p1.next
                    p1 = p1.next
                else:
                    p3.val = p2.val
                    p3.next = p2.next
                    p2 = p2.next
                p3.next = ListNode()
                p3 = p3.next
            if(p1.next != None):
                p3.val = p1.val
                p3.next = p1.next
            elif(p2.next != None):
                p3.val = p2.val
                p3.next = p2.next
        return list3
    def addNodesToList(self,p, val):
        while(p.next != None):
            p = p.next
        p.val = val
        p.next = ListNode()
        p.next.val = val
    def printList(self, p):
        if(p.val == 0 and p.next == None):
            print("\n")
            return
        print("\n",p.val,end=" ")
        p = p.next
        while(p.next != None):
            print(p.val,end=" ")
            p = p.next 
        print()           
l1 = [1, 2, 5]
l2 = [1, 3, 4]
list1 = ListNode()
list2 = ListNode()
temp1 = list1
temp2 = list2
sol = Solution()
for number in l1:
    sol.addNodesToList(list1,number)
for number in l2:
    sol.addNodesToList(list2,number)
print("The first list is :")
sol.printList(list1)
print("The second list is :")
sol.printList(list2)
list3 = sol.mergeTwoLists(list1,list2)
print("The merged list is :")
sol.printList(list3)