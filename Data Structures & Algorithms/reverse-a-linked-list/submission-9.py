# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodul_precedent = None
        nod_curent = head
        while nod_curent != None:
            #Salvez urmatorul nod de accesat
            urmatorul_nod = nod_curent.next
            #Actualizam next-ul nodului curent
            nod_curent.next = nodul_precedent
            #Actualizam nodul predent cu nodul actual
            nodul_precedent = nod_curent
            #Trecem la urmatorul nod
            nod_curent = urmatorul_nod
        return nodul_precedent


 


