from LinkedList import LinkedList


class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        """
        Uses a map lambda function to instantiate LinkedList object, which is populated with
        None * size, before returning it all as a list
        Note: I don't know exactly how this works but I just messed with this example until it worked
             https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
        Returns:
            list: a list of nodes
        """
        return list(map(lambda z: LinkedList(), [None] * size))

    def hash_func(self, key):
        """
        Simple hash function which mods the length of a string key
        Returns:
             int
        """
        return len(key) % self.size

    def insert(self, key, value):
        """
        Calculates index with key_hash, before iterating through each node
        checking for matching keys. If found, increment the count by 1,
        if not found then append to the end of the list.
        """
        key_hash = self.hash_func(key)
        word_pair = [key, value]

        nodeCheck = self.arr[key_hash].head

        while nodeCheck != None:
            if nodeCheck.data[0] == key:
                nodeCheck.data[1] += value
                return
            else:
                nodeCheck = nodeCheck.next

        self.arr[key_hash].append(word_pair)

    def print_key_values(self):
        """
        Iterate through the list printing each node until None, at which point move on to the next link
        """
        for link in self.arr:
            if link.head:
                pass

            currentNode = link.head
            while currentNode != None:
                print(currentNode.data)
                currentNode = currentNode.next
