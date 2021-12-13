# Name: Bryan Gronberg
# OSU Email: gronberb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 7
# Due Date: 12/03/2021
# Description: This program implements a hash map class. The hashmap object has a hash function, size and capacity
# parameters, and uses a Dynamic Array and Linked Lists to store its data. Hash functions will provide the index
# of the Dynamic Array based on provided keys, and Linked Lists are used to store the data at any array position, to
# reduce complications from hash collisions. There are methods to return the load balance and also to resize the table
# as needed. See the individual class methods for me detail.


# Import pre-written DynamicArray and LinkedList classes
from a7_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the hash table by creating and assigning an empty Linked List for every array index (number determined
        by current table capacity).
        :return: None
        """
        for i in range(self.capacity):
            self.buckets[i] = LinkedList()
        self.size = 0

    def get(self, key: str) -> object:
        """
        The get function takes a key parameter and finds the associated value. If the table does not have the key,
        then the function returns None. If the key is in the hash table, the value is returned.
        :param key: a string
        :return: Value of the node, or None if the object is not found.
        """
        index = self.hash_function(key) % self.capacity
        linked_list = self.buckets.get_at_index(index)
        for node in linked_list:
            if node.key == key:
                return node.value

    def get_SLL(self, key: str) -> object:
        """
        Retrieve the node with the key matching the provided key parameter.
        :param key: a string
        :return: Value of the node, or None if the object is not found.
        """
        index = self.hash_function(key) % self.capacity
        return self.buckets.get_at_index(index)

    def put(self, key: str, value: object) -> None:
        """
        Takes a key and a value and creates a new node if the key is not in the table, or if the key already exists,
        updates the node with the provided value. If a new node is created, the hash table's size increases by 1.
        :param key: a string
        :param value: an object
        :return: None
        """
        # you need to check to see if there's already a node with the key provided
        # if so, replace that node's value with the new value
        # don't update the size, because the number of nodes is the same, otherwise +1
        linked_list = self.get_SLL(key)
        if self.contains_key(key):
            cur = linked_list.head
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
        else:
            linked_list.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        Attempts to remove the node with the provided key value. If the node is removed successfully, reduce size by 1.
        :param key: a string
        :return: None
        """
        linked_list = self.get_SLL(key)
        if linked_list.remove(key):
            self.size -= 1


    def contains_key(self, key: str) -> bool:
        """
        If the provided key matches the key of an existing node, return True, else False. If the table is empty,
        returns False.
        :param key: a string
        :return: True/False
        """
        if self.size == 0:
            return False
        if self.get(key) is not None:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        Return the count of empty buckets (spaces in the table with no entries)
        :return: Integer
        """
        empty_count = 0
        for i in range(0, self.capacity):
            if self.buckets.get_at_index(i).length() == 0:
                empty_count += 1
        return empty_count

    def table_load(self) -> float:
        """
        Calculates and returns the load factor of the hash table (size divided by capacity)
        :return: float
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Takes an integer value and then rehashes the table at the size provided
        :param new_capacity: integer, new capacity of table -- must be greater than 0
        :return: None
        """
        if new_capacity < 1:
            return
        newArray = DynamicArray()
        oldArray = self.buckets
        old_cap = self.capacity
        for i in range(new_capacity):
            newArray.append(LinkedList())
        self.buckets = newArray
        self.capacity = new_capacity
        self.size = 0
        for i in range(old_cap):
            cur = oldArray[i].head
            while cur:
                self.put(cur.key, cur.value)
                cur = cur.next

    def get_keys(self) -> DynamicArray:
        """
        Returns a new DynamicArray containing the keys from the table
        :return: DynamicArray
        """
        da = DynamicArray()
        for i in range(self.capacity):
            cur = self.buckets[i].head
            while cur:
                da.append(cur.key)
                cur = cur.next
        return da


# BASIC TESTING
if __name__ == "__main__":
    pass
    #
    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())
    #
    #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    #
    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')
    #
    #
    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    #
    #
    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    #
    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)
    #
    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')
    #
    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))
    #
    #
    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())
    #
    # m.resize_table(1)
    # print(m.get_keys())
    #
    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())
