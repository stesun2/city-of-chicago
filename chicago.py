# Your code goes here!
import psycopg2
import os
import csv
import ipdb



# Connect to Database
def connect_to_database():
    connection = psycopg2.connect(f"dbname=chicago_salaries_db user={os.getlogin()}")

    cursor = connection.cursor()
