import random

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        current = self
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def display(self):
        current = self
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print('\n')

def reverse_list(head):
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

def sort_list(head):
    if not head or not head.next:
        return head

    list = ListNode(0)
    list.next = head
    prev_sorted = list.next
    current_unsorted = list.next.next

    while current_unsorted:
        if prev_sorted.val is not None and prev_sorted.val <= current_unsorted.val:
            prev_sorted = prev_sorted.next
        else:
            prev = list
            while prev.next.val is not None and prev.next.val <= current_unsorted.val:
                prev = prev.next

            prev_sorted.next = current_unsorted.next
            current_unsorted.next = prev.next
            prev.next = current_unsorted

        current_unsorted = prev_sorted.next

    return list.next


def merge_lists(l1, l2):
    list = ListNode(0)
    current = list

    while l1 and l2:
        if l1.val is not None and l2.val is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
        elif l1.val is None:
            current.next = l2
            l2 = l2.next
        else:
            current.next = l1
            l1 = l1.next

        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return list.next


def generate_list(list):
    for i in range(0, 10):
        list.append(random.randint(1, 50))
    return list

list1 = ListNode()
list1 = generate_list(list1)

list2 = ListNode()
list2 = generate_list(list2)

list3 = ListNode()
list3 = generate_list(list3)

print('\n')
print("1. Reversing")
print("List:")
list1.display()
print("Reversed list:")
reverse_list(list1).display()

print("2. Sorting")
print("List:")
list2.display()
print("Sorted list:")
sorted_list2 = sort_list(list2)
sorted_list2.display()

print("3. Merging")
print("Lists:")
sorted_list2.display()
sorted_list3 = sort_list(list3)
sorted_list3.display()
print("Merged list:")
merge_lists(sorted_list2, sorted_list3).display()
