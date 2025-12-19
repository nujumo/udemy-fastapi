from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # SQLite
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Fj6whzJk3W4pi3IS@localhost/ToDoApplicationDatabase' # postgres setup
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/ToDoApplicationDatabase' # mysql

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) # sqlite only
# engine = create_engine(SQLALCHEMY_DATABASE_URL) # postgresql and mysql

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
Production Database
===================
- This section will go over installing a production relational 
database for your application!
- The two Database Management Systems (DBMS) applications we 
will be going over are MySQL and PostgreSQL
- Both DBMS systems are used widely throughout enterprise 
applications, and you cannot go wrong with either one

Production DBMS vs SQLite
=========================
- SQLite3 strives to provide local data storage for 
individual applications and devices.
- SQLite3 emphasises economy, efficiency and simplicity.
- For most small / medium applications, SQLite3 will work perfectly.
- SQLite3 focuses on different concepts than a production Database Management System.

- MySQL and PostgreSQL focus on a big difference compared to SQLite3.
- These production DBMS focuses on scalability, concurrency and control.
- If your application is going to have 10s of thousands of users, 
it may be wise to switch to a production DBMS.
- If your application is only you, and a few others, SQLite3 will work great!

Production DBMS Key Notes
=========================
- SQLite3 runs in-memory or local disk, which allows development 
of a SQLite3 data to be easy, as it is part of your application!
- Production DBMS run on their own server and port. Which means 
you need to make sure the database is running, and have authentication
linking to the DBMS.
- (SQLite3) For deployment you can deploy a SQLite3 database along with
the application
- (Prod DBMS) For deployment you will need to also deploy the database 
separate from the application.


What is PostgreSQL?
===================
- Production ready
- Open-source relational database management system (RDBMS)
- Secure
- Requires a server
- Scalable

What is MySQL?
===================
- Open-source relational database management system (RDBMS)
- Requires a server
- Production ready

What is Alembic?
================
- Lightweight database migration tool for when using SQLAlchemy
- Migration tools allow us to plan, transfer, and upgrade resources within databases
- Alembic allows you to change a SQLAlchemy database table after it has been created.
- Currently SQLAlchemy will only create new database tables for us, not enhance any.

How does Alembic work?
======================
- Alembic provides the creation and invocation of change management scripts
- This allows you to be able to create migration environments and be able to change data how you like
- Alembic is a powerful migration tool that allows us to modify our database schemas
- As our application evolves, our database will need to evolve as well
- Alembic helps us be able to keep modifying our database to keep up with rapid development requirements
- We will be using Alembic on tables that already have data. This allows us to be able to continually 
create additional content that works within our application!

Alembic commands
================
alembic init <folder name> - Initialises a new, generic environment
alembic revision -m <message> - Creates a new revision of the environment
alembic upgrade <review #> - Run our upgrade migration to our database
alembic downgrade -1 - Run our downgrade migration to our database

Alembic.ini file
================
- File that alembic looks for when invoked
- Contains a bunch of configuration information for Alembic that we are able to change to match our project

Alembic Directory
=================
- Has all the environmental properties for alembic
- Holds all revisions of your application
- Where you can call the migrations for upgrading
- Where you can call the migrations for downgrading

Alembic Revision?
=================
- Alembic revision is how we create a new alembic file where we can add some type of database upgrade
- When we run > 
    alembic revision -m "create phone number col on users table"
- This will create a new file where we can write the upgrade code
- Each new revision will have a Revision Id

Alembic Upgrade?
================
 - Alembic upgrade is how we actually run the migration
 
 def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

- This upgrade function will enhance our database to now have a new column within our 
users table called 'phone_number' (the values of which are all set to null)
- Previous data within the database does not change

- To run the upgrade migration, run >
    alembic upgrade <revision id>
- This will successfully implement the change within the upgrade functionality

Alembic Downgrade?
==================
- Alembic downgrade is how we revert a migration

def downgrade() -> None:
    op.drop_column('users', 'phone_number')

- This downgrade function will revert our database to remove the last migration change
- Previous data within the database does not change unless it was on the column 
'phone_number' because we deleted it.

- To run the downgrade migration, run >
    alembic downgrade -1
    
- This code will revert the last migration
"""