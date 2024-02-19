from data_structures.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current = bucket.head

        while current:
            candidate_drop = current.value
            if candidate_drop[0] == key:
                candidate_drop[1] = value
                return

        drop = [key, value]
        bucket.insert(drop)

    def get(self, key):
        index = self._hash(key)

        bucket = self._buckets[index]

        if bucket is None:
            return None

        current = bucket.head

        while current:
            drop = current.value
            if drop[0] == key:
                return drop[1]

            current = current.next

        return None

    def keys(self):
        """
        return list of keys
        """
        key_list = []  

        for bucket in self._buckets:
            if bucket:
                current = bucket.head
                while current:
                    drop = current.value
                    key_list.append(drop[0])
                    current = current.next

        return key_list

    def has(self, key):
        for bucket in self._buckets:
            if bucket:
                current = bucket.head 
                while current:
                    drop = current.value
                    if drop[0] == key:
                        return True

                    current = current.next

        return False

    def _hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self._size

        return index
