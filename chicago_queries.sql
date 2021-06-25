-- Write your Queries here

DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees(
  id                    SERIAL PRIMARY KEY,
  first_name            VARCHAR(24) NOT NULL,
  last_name             VARCHAR(24) NOT NULL,
  job_title             VARCHAR(24) NOT NULL,
  full_or_part_time     CHAR(1) NOT NULL,
  department            VARCHAR(24) NOT NULL,
  annual_salary         INTEGER NOT NULL
);
