"""Node Class."""

from __future__ import annotations
from typing import Optional


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the `data` attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> (Node | None):
        """Returns a linked list of every element minus the head."""
        if self.next is None:
            return None
        else:
            return Optional[Node]
    
    def last(self) -> int:
        """Returns the `data` of the *last* element in the linked list."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()