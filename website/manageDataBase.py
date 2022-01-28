import mysql.connector
from mysql.connector import Error
from flask import flash

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class CDbManager:
    _conn = None
    _cursor = None

    # Default constructor
    def __init__(self):
        # Init the connection to the database
        self.init_connection()

    # Connect to the database
    def init_connection(self):
        try:
            print('Connecting to hotel_manager...')
            self._conn = mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="lazaroiu5079",
                database="laza")
            if self._conn.is_connected():
                logging.info(' * Connection is UP')
                # If the connection is established, init the cursor
                self._cursor = self._conn.cursor()
            else:
                logging.info(' * Connection FAILED')
        except Error as e:
            logging.debug(" * " + e)

    # Check the connection
    def check_connection(self):
        if self._conn.is_connected():
            logging.info(' * Connection is UP')
        else:
            logging.info(' * Connection is DOWN')

    def get_all_rooms(self):
        rooms_data = None
        try:
            # Execute the query
            self._cursor.execute(("SELECT * FROM camere"))
            # Fetch all the data
            rooms_data = self._cursor.fetchall()
            # Check if the retrieved data is not empty
            if rooms_data != None:
                return rooms_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as err:
            logging.debug(" * SQL Error: {}".format(err))
            # Flash error message
            flash('SQL Error!', category='error')

