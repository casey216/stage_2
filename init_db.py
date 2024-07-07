import os
import cs50
import psycopg2

db = cs50.SQL("postgresql://stage_2_user:stage_2_user@localhost:5432/stage_2")

# Execute a command: this creates a new table
db.execute('CREATE TABLE IF NOT EXISTS Users (userId serial PRIMARY KEY UNIQUE NOT NULL,'
                                 'firstName varchar (150) NOT NULL,'
                                 'lastName varchar (150) NOT NULL,'
                                 'email varchar (150) UNIQUE NOT NULL,'
                                 'password varchar (150) NOT NULL,'
                                 'phone varchar (150));'
                                 )

db.execute('CREATE TABLE IF NOT EXISTS organisations (orgId serial PRIMARY KEY UNIQUE NOT NULL,'
                                 'name varchar (150) NOT NULL,'
                                 'description varchar (150));'
                                 )

db.execute('CREATE TABLE IF NOT EXISTS records (id serial PRIMARY KEY UNIQUE NOT NULL,'
                                 'user_id integer NOT NULL REFERENCES users (userid),'
                                 'org_id integer NOT NULL REFERENCES organisations (orgid));'
                                 )