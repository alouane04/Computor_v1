# This to tell python to Interpret the | as unios type
from __future__ import annotations
from dataclasses import dataclass


# Linked list for the equation parts
@dataclass
class Parts:
    coefficient: float
    exponent: int
    next: "Parts" | None = None


class Parts_linkedList:
    def __init__(self) -> None:
        # Why avoid it: If you later try to access self.head.num, the editor assumes it is safe 
        # because you promised it was a Parts object. But if it is actually None, 
        # your program crashes with an AttributeError.
        # self.head: Parts = None
        self.head: Parts | None = None
        self.degree: int = 0
    

    def __str__(self):
        # if head have 0 coeffienct mean wherever after that dosn't matter
        # cause we already have order in place so
        if self.head is None:
            return "0 * X^0 = 0"
        
        current = self.head

        parts = []

        while current:
            if current.coefficient < 0:
                if current == self.head:
                    sign = ""
                    val = current.coefficient
                else:
                    sign = "- "
                    val = -current.coefficient
            else:
                sign = "+ " if parts else ""
                val = current.coefficient
            
            if val.is_integer():
                val = int(val)

            parts.append(f"{sign}{val} * X^{current.exponent} ")

            current = current.next
        
        return "".join(parts) + "= 0"


    def calculate_degree(self) -> int:
        current = self.head
        while current:
            if current.exponent > self.degree and current.coefficient != 0:
                self.degree = current.exponent
            current = current.next
        return self.degree


    def assign_term(self, coefficient, exponent):
        # Guardian
        # if coefficient == 0: # Comment this for now maybe forever
        #     return

        # if list is empty init head
        if self.head is None:
            self.head = Parts(coefficient, exponent)
            return
        
        current = self.head
        while current:
            if current.exponent == exponent:
                current.coefficient += coefficient
                return
            
            current = current.next

            # If we break mean we didn't find the same exponent
            if current is None:
                break
        
        # Now we need to find the right fit place for the exponent
        current = self.head
        while current:

            if current.exponent > exponent and self.head == current:
                self.head = Parts(coefficient, exponent, current)
                return
                
            elif current.exponent < exponent:
                if current.next:
                    # is it in Between 
                    if current.next.exponent > exponent:
                        tmp = current.next
                        current.next = Parts(coefficient, exponent, tmp)
                        return
                # the tail
                else:
                    current.next = Parts(coefficient, exponent)


            current = current.next
