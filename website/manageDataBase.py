import mysql.connector
from mysql.connector import Error
from flask import flash

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class CDbManager:
    connection = None
    cursor = None

    # Default constructor
    def __init__(self):
        # Init the connection to the database
        self.init_connection()

    # Connect to the database
    def init_connection(self):
        try:
            print('Connecting to hotel_manager...')
            self.connection = mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="lazaroiu5079",
                database="laza")
            if self.connection.is_connected():
                logging.info("<< Connection is UP >>")
                # If the connection is established, init the cursor
                self.cursor = self.connection.cursor()
            else:
                logging.info("<< Connection FAILED >>")
        except Error as e:
            logging.debug(" * " + e)

    # Check the connection
    def check_connection(self):
        if self.cursor.is_connected():
            logging.info('<< Connection is UP >>')
        else:
            logging.info('<< Connection is DOWN >>')

    def get_all_rooms(self):
        rooms_data = None
        try:
            # Execute the query
            self.cursor.execute(("SELECT * FROM camere"))
            # Fetch all the data
            rooms_data = self.cursor.fetchall()
            # Check if the retrieved data is not empty
            if rooms_data != "":
                return rooms_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as e:
            logging.debug(" * SQL Error: {}".format(e))
            # Flash error message
            flash('SQL Error!', category='error')

    def get_all_hotels(self):
        try:
            self.cursor.execute(("SELECT * FROM hoteluri"))
            # Fetch all the data
            hotels_data = self.cursor.fetchall()
            # Check if the retrieved data is not empty
            if hotels_data != "":
                return hotels_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as e:
            logging.debug(" * SQL Error: {}".format(e))
            # Flash error message
            flash('SQL Error!', category='error')

    def get_all_rezervations(self):
        try:
            self.cursor.execute(("SELECT * FROM rezervare"))
            # Fetch all the data
            hotels_data = self.cursor.fetchall()
            # Check if the retrieved data is not empty
            if hotels_data != "":
                return hotels_data
            else:
                logging.debug(" * Rooms Data is NULL!!! Please DEBUG!!")
        except mysql.connector.IntegrityError as e:
            logging.debug(" * SQL Error: {}".format(e))
            # Flash error message
            flash('SQL Error!', category='error')