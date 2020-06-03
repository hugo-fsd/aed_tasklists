from aed_ds.dictionaries.hash_table import HashTable

class User:
    def __init__(self, user_name):
        self.name = user_name
        self.task_lists = HashTable()
    
    def get_name(self):
        return self.name
