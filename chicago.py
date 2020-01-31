# Your code goes here!
import psycopg2
import os
import csv

# annual_salary. Note: If an employee is an hourly employee, calculate their annual salary by this equation: hours_per_week * hourly_salary * 50 (50 weeks a year)

drop_employees_table = "DROP TABLE IF EXISTS employees CASCADE;"

chicgo_salaries_table_creation = """
  CREATE TABLE employees (
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    job_title varchar(255) NOT NULL,
    full_or_part_time varchar(1) NOT NULL,
    department varchar(255) NOT NULL,
    annual_salary integer NOT NULL
  )
"""

connection = psycopg2.connect(f'dbname=chicago_salaries_3 user={os.getlogin()}')
cursor = connection.cursor()
cursor.execute(drop_employees_table)
cursor.execute(chicgo_salaries_table_creation)

def clean_data(row):
  cleaned = {}
  name = row['Name'].split(', ')
  cleaned['first_name'] = name[1]
  cleaned['last_name'] = name[0]
  cleaned['job_title'] = row['Job Titles']
  cleaned['full_or_part_time'] = row['Full or Part-Time']
  cleaned['department'] = row['Department']
  if row['Salary or Hourly'] == 'Hourly':
    hours_per_week = float(row['Typical Hours'])
    hourly_salary = float(row['Hourly Rate'])
    cleaned['annual_salary'] = round(hours_per_week * hourly_salary * 50)
  elif row['Salary or Hourly'] == 'Salary':
    salary = float(row['Annual Salary'])
    cleaned['annual_salary'] = round(salary)
  return cleaned

with open('current_chicago_salaries.csv') as salaries_csv:
  csv_reader = csv.DictReader(salaries_csv)
  for row in csv_reader:
    cleaned_data = clean_data(row)
    cursor.execute("""
      INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%(first_name)s,%(last_name)s,%(job_title)s,%(full_or_part_time)s,%(department)s,%(annual_salary)s)""", cleaned_data)
  print('Successfully added data...')








connection.commit()
connection.close()
