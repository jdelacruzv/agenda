import sqlite3


class Agenda:
    """ Class that performs basic queries to the phonebook database (works as the application model) """
    def __init__(self):
        self.db_filename = 'phonebook.db'


    def execute_db_query(self, query, parameters=()):
        """ Query the database """
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result


    def create_contact(self, name, telephone, birthdate, email, country):
        """ Save contacts """
        query = 'INSERT INTO contacts VALUES(?, ?, ?, ?, ?)'
        parameters = (name, telephone, birthdate, email, country)
        self.execute_db_query(query, parameters)
        self.read_contact()


    def read_contact(self):
        """ Read contact """
        query = 'SELECT * FROM contacts ORDER BY name asc'
        return self.execute_db_query(query)


    def update_contact(self, telephone, email, country, birthdate, name):
        """ Update contact """
        query = 'UPDATE contacts SET telephone=?, email=?, country=? WHERE birthdate=? AND name=?'
        parameters = (telephone, email, country, birthdate, name)
        self.execute_db_query(query, parameters)
        self.read_contact()


    def delete_contact(self, name):
        """ Delete contact """
        query = 'DELETE FROM contacts WHERE name = ?'
        self.execute_db_query(query, (name,))
        self.read_contact()
