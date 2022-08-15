from sqlite3 import *

#connects to db 
db = connect("elements.db")
cursor = db.cursor()

#main elements class
class element(object):
    def __init__(self, number):
        self.atomic_number = number
    #getters ask te databas for the given input
    def get_atomic_number(self):
        return int(self.atomic_number)
    def get_from_db(self, value):
        cursor.execute(f"SELECT {value}  FROM elements WHERE Atomic_Number = {self.get_atomic_number()}")
        return cursor.fetchone()[0].strip()
    
    
    
     



if __name__ == "__main__":
    #unit test for elelemnts class and elements
    for i in range(1, 118):
        foo = element(i)
        print(f"Element {foo.get_atomic_number()} is {foo.get_from_db('Name')} ({foo.get_from_db('Symbol')}) and has a charge of {foo.get_from_db('Most_stable')}")

db.close()
