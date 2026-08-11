# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nod_start = None
        nod_lista1 = list1
        nod_lista2 = list2
        if nod_lista1 == None and nod_lista2 == None:
            return nod_start
        #Alegem punctul de start
        if nod_lista1 == None and nod_lista2 != None:
            nod_start = nod_lista2
        elif nod_lista1 != None and nod_lista2 == None:
            nod_start = nod_lista1
        else:
            if nod_lista1.val < nod_lista2.val:
                nod_start = nod_lista1
            else:
                nod_start = nod_lista2
        nod_curent = nod_start
        #Constructia listei
        while nod_lista1 or nod_lista2:
            #Verificam si actualizam nodul care Nu a fost ales ca start
            if nod_curent == nod_lista1:
                nod_lista1 = nod_lista1.next
            else:
                nod_lista2 = nod_lista2.next
            #Selectam nodul urmator
            if nod_lista1 == None and nod_lista2 != None:
                nod_curent.next = nod_lista2
                nod_curent = nod_lista2
            elif nod_lista1 != None and nod_lista2 == None:
                nod_curent.next = nod_lista1
                nod_curent = nod_lista1
            elif nod_lista1 != None and nod_lista2 != None:
                if nod_lista1.val < nod_lista2.val:
                    nod_curent.next = nod_lista1
                    nod_curent = nod_lista1
                else:
                    nod_curent.next = nod_lista2
                    nod_curent = nod_lista2
            else:
                nod_curent = None
        return nod_start

        