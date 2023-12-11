from typing import Optional

from src.Merge_Two_Sorted_Lists.ListNode import ListNode


class MergeTwoSortedLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        placeholder = ListNode()
        curr = placeholder

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if not list1:
            curr.next = list2
        elif not list2:
            curr.next = list1

        return placeholder.next


