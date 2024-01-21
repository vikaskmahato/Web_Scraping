# Import the create_engine method
from sqlalchemy import create_engine
 
# The database URL must be in a specific format
db_url = "mysql+mysqlconnector://{USER}:{PWD}@{HOST}/{DBNAME}"
# Replace the values below with your own
# DB username, password, host and database name
db_url = db_url.format(
    USER = "root",
    PWD = "PasswordForMySQL",
    HOST = "localhost:3306",
    DBNAME = "test"
)
# Create the DB engine instance. We'll use
# this engine to connect to the database
engine = create_engine(db_url, echo=False)