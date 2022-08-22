from sqlite3 import *

# connects to db
db = connect("database.db", check_same_thread=False)
cursor = db.cursor()

# main elements class


class element(object):
    def __init__(self, number):
        self.atomic_number = number
    # getters ask te databas for the given input

    def get_atomic_number(self):
        return int(self.atomic_number)

    def get_from_db(self, value):
        cursor.execute(
            f"SELECT {value}  FROM elements WHERE Atomic_Number = {self.get_atomic_number()}")
        return cursor.fetchone()[0].strip()

    def lookup(self):
        return f"<tr><button id='{self.get_from_db('Atomic_number')}' class='btn Default'>{self.get_from_db('Name')}, <span>{self.get_from_db('Symbol')}</span></button></tr>"
    
    def get_element_info(self):
        return f"<div id='elements_info_div'><div id='Atomic_number'>{self.get_from_db('Atomic_number')}</div><div id='element_symbol'>{self.get_from_db('Symbol')}</div><div id='element_name'>{self.get_from_db('Name')}</div></div>"


# function that ask the db for any elements that are like query by symbol or name
def lookup_element(q):
    # formats query
    q = "%" +  str(q).lower() + "%"
    rtn = []
    
    #look through database for matching elements by name or by symbol 
    cursor.execute(
        ("SELECT Atomic_number FROM elements WHERE Name LIKE ? OR Symbol LIKE ? LIMIT 10"), (q,q ))

    # adds to list
    rtn.append(cursor.fetchall())

    form_rtn = []
    # formats rtn data before return
    for num in rtn[0].copy():
        form_rtn.append(int(num[0]))

    # return list of possible atomic #'s
    return form_rtn


if __name__ == "__main__":
    # unit test for elelemnts class and elements
    # for i in range(1, 118):
    # foo = element(i)
    # print(f"Element {foo.get_atomic_number()} is {foo.get_from_db('Name')} ({foo.get_from_db('Symbol')}) and has a charge of {foo.get_from_db('Most_stable')}")
    # unit test for lookup_elemeent
    print(lookup_element("l"))
    print(lookup_element("lith"))
    print(lookup_element("lithium"))
