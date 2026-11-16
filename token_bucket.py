"""A small token bucket used by the public review pilot."""

from __future__ import annotations


class TokenBucket:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.tokens = capacity

    def take(self, count: int = 1) -> bool:
        if self.tokens >= count:
            self.tokens -= count
            return True
        return False
