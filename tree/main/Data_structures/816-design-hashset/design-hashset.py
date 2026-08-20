class MyHashSet:

    def __init__(self):
        # Create 1000 buckets, each starting as an empty list
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]
        
    def _get_hash(self, key: int) -> int:
        # Instantly finds the correct bucket index for any number
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket = self.buckets[self._get_hash(key)]
        # Fix 1: Only add if it's not already there to prevent duplicates
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._get_hash(key)]
        # Fix 2: Check first so the code never crashes on missing keys
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._get_hash(key)]
        return key in bucket
