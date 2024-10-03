class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        try:
            index = self._hash_function(key)
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
            raise KeyError(f"Key \'{key}\' not found")
        except KeyError as e:
            print(e)
            return None

    def delete(self, key):
        try:
            index = self._hash_function(key)
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return
            raise KeyError(f"Key \'{key}\' not found")
        except KeyError as e:
            print(e)

hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("cherry", 10)
hash_table.insert("strawberry", 3)
hash_table.insert("orange", 8)

print("banana: ", hash_table.get("banana"))
print("orange: ", hash_table.get("orange"))

hash_table.delete("banana")
print("banana: ", hash_table.get("banana"))
print("orange: ", hash_table.get("orange"))
print("cherry: ", hash_table.get("cherry"))
